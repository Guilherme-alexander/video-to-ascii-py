import cv2
import pygame
import time
import sys
import os
import json
from datetime import datetime
from pathlib import Path
import argparse
from moviepy.editor import VideoFileClip

# python main.py video.mp4 -w 115 --fps 35 -s 15 --chars "0123456789"
# python main.py video.mp4 -w 130 --fps 35 -s 15 --chars ".:-=+*#%@"
# [FULLSCREEN] python main.py video.mp4 -w 120 --fps 40 -s 10 --chars "01"

def extract_audio(video_path):
    audio_path = Path("audio.wav")
    if audio_path.exists():
        print("Usando audio.wav existente.")
        return audio_path
    print("Extraindo áudio do vídeo...")
    video = VideoFileClip(str(video_path))
    video.audio.write_audiofile(str(audio_path))
    print("Áudio extraído com sucesso!")
    return audio_path

def frame_to_ascii(frame, width, chars, aspect_correction=0.45):
    h, w = frame.shape[:2]
    height = int(h * width / w * aspect_correction)
    small = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
    
    lines = []
    for y in range(height):
        line = ""
        for x in range(width):
            b, g, r = small[y, x]
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            idx = int(lum * (len(chars) - 1) / 255)
            char = chars[idx]
            line += f"\033[38;2;{r};{g};{b}m{char}"
        lines.append(line + "\033[0m")
    return lines, height

def play_in_terminal(video_path, width=65, fps_target=60, seconds=120, skip_frames=15, audio_delay=5.0, chars=" 0123456789", frames_all=False, save=False):
    # Extrai áudio automaticamente
    audio_path = extract_audio(video_path)
    # Inicializa pygame para áudio
    pygame.mixer.init()
    pygame.mixer.music.load(str(audio_path))
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        print("Erro ao abrir vídeo.")
        return
    # Detecta FPS real
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 15
    if fps_target:
        fps = fps_target
    frame_time = 1.0 / fps
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    max_frames = total_frames if frames_all else (int(seconds * fps) if seconds else total_frames)
    skip_frames = 1 if frames_all else skip_frames
    duration_sec = max_frames / fps
    print("\033[?25l", end="", flush=True) # Esconde cursor
    print(f"Reproduzindo: {video_path.name}")
    print(f"FPS usado: {fps:.1f} | Duração: {duration_sec:.1f} seg | Frames: {max_frames}")
    print(f"Pulando frames: {skip_frames} em {skip_frames} | Delay áudio: {audio_delay:.1f} seg")
    print("Pressione Ctrl+C para parar\n")
    start_time = time.time()
    frame_count = 0
    # Calcula altura fixa uma vez (do primeiro frame)
    ret, first_frame = cap.read()
    if not ret:
        print("Erro no primeiro frame.")
        return
    _, fixed_height = frame_to_ascii(first_frame, width, chars)
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset para início
    # Config para save
    output_dir = None
    config = None
    saved_frame_idx = 0
    if save:
        output_dir = f"ascii_frames_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs(output_dir, exist_ok=True)
        config = {
            "video": str(video_path),
            "width": width,
            "fps": fps,
            "seconds": seconds,
            "skip_frames": skip_frames,
            "audio_delay": audio_delay,
            "chars": chars,
            "start_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)),
            "total_frames_saved": 0,
            "fixed_height": fixed_height
        }
        print(f"Salvando frames em: {output_dir}")
    # Inicia áudio com delay
    time.sleep(audio_delay)
    pygame.mixer.music.play()
    try:
        while cap.isOpened() and frame_count < max_frames:
            ret, frame = cap.read()
            if not ret:
                break
            # Pula frames conforme configurado
            frame_count += 1
            if frame_count % skip_frames != 1:
                continue
            ascii_lines, _ = frame_to_ascii(frame, width, chars)
            # Preenche com linhas vazias se necessário (para altura fixa)
            while len(ascii_lines) < fixed_height:
                ascii_lines.append("")
            # Re-desenhar sem clear total: move cursor para topo e apaga abaixo
            print("\033[H\033[J", end="", flush=True)  # Move para topo + erase below
            print("\n".join(ascii_lines), flush=True)
            # Ajuste de tempo para manter FPS
            expected_time = frame_count * frame_time
            elapsed = time.time() - start_time
            sleep_time = expected_time - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)
            # Save se ativado
            if save:
                txt_path = os.path.join(output_dir, f"frame_{saved_frame_idx:06d}.txt")
                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(ascii_lines))
                saved_frame_idx += 1
    except KeyboardInterrupt:
        print("\nParado pelo usuário")
    finally:
        cap.release()
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        print("\033[?25h\033[0m", end="", flush=True) # Mostra cursor e reseta cores
        if save and config:
            config["total_frames_saved"] = saved_frame_idx
            with open(os.path.join(output_dir, "config.json"), "w") as f:
                json.dump(config, f, indent=4)
            print(f"Salvo {saved_frame_idx} frames + config.json em {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vídeo → ASCII art no terminal com áudio e opções avançadas")
    parser.add_argument("video", help="Caminho do vídeo")
    parser.add_argument("-w", "--width", type=int, default=115, help="Largura em caracteres")
    parser.add_argument("--fps", type=int, default=34, help="FPS alvo (usa FPS do vídeo por padrão)")
    parser.add_argument("--seconds", type=int, default=180, help="Duração máxima em segundos")
    parser.add_argument("-s", "--skip-frames", type=int, default=15, help="Pular frames (ex: 2 = pula de 2 em 2, 3 = de 3 em 3)")
    parser.add_argument("-d", "--audio-delay", type=float, default=5.0, help="Delay em segundos para iniciar o áudio (positivo = atrasar música, negativo = adiantar)")
    parser.add_argument("--chars", default="0123456789", help="Caracteres (escuro → claro)")
    parser.add_argument("--frames-all", action="store_true", help="Usa todos os frames (ignora --skip-frames e --seconds)")
    parser.add_argument("--save", action="store_true", help="Salva todos os frames ASCII em pasta + json com config")
    args = parser.parse_args()
    if args.skip_frames < 1:
        print("Erro: --skip-frames deve ser >= 1")
        sys.exit(1)
    video_path = Path(args.video)
    if not video_path.is_file():
        print(f"Arquivo não encontrado: {video_path}")
        sys.exit(1)
    play_in_terminal(video_path, args.width, args.fps, args.seconds, args.skip_frames, args.audio_delay, args.chars, args.frames_all, args.save)
