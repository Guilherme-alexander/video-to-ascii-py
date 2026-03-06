# 🎬 ASCII Video Player (Terminal)

Reproduz vídeos diretamente no **terminal como ASCII Art colorido**, sincronizado com **áudio extraído automaticamente do vídeo**.

O projeto converte cada frame do vídeo em caracteres ASCII coloridos usando ANSI escape codes e reproduz o áudio simultaneamente.

O vídeo aparece como uma animação ASCII colorida dentro do terminal.

<br/>

## 🚀 Features

- 🎥 Reprodução de vídeo em **ASCII art colorido**
- 🔊 **Extração automática de áudio** do vídeo
- 🎵 Reprodução sincronizada com **pygame**
- ⚡ Controle de FPS
- 🎚️ Skip de frames para performance
- 🖥️ Suporte a **fullscreen terminal**
- 💾 Opção de **salvar todos os frames ASCII**
- 🎛️ Personalização completa de caracteres ASCII
- 📦 Compatível com **Linux / Windows / Mac**

<br/>

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/ascii-video-player.git
cd ascii-video-player
```

```bash
pip install -r requirements.txt
```

<br/>

## 📦 dependências:

### Python 3.8+
  
* **opencv-python**
* **pygame**
* **moviepy**

<br/>

## 🎧 Instalando FFmpeg
O projeto também depende do **FFmpeg** para manipulação de áudio.
FFmpeg é usado internamente pelo moviepy para extrair o áudio do vídeo.

Baixe o FFmpeg: ["FFmpeg Download"](https://ffmpeg.org/download.html)

1. Baixe o FFmpeg
2. Extraia o zip
3. Adicione a pasta bin ao PATH.

## 📁 Estrutura

```cmd
video-to-ascii-py
│
├── main.py
├── video.mp4
├── ffmpeg.exe
├── ffplay.exe
├── ffprobe.exe
├── requirements.txt
└── README.md
```

<br/>

##  📌 Como Usar

### ▶️ ASCII estilo matrix

```bash
python main.py video.mp4 -w 120 --fps 40 --chars "01"
```

### ▶️ ASCII detalhado

```bash
python main.py video.mp4 -w 130 --fps 35 -s 15 --chars ".:-=+*#%@"
```

### ▶️ ASCII numérico

```bash
python main.py video.mp4 -w 115 --fps 35 -s 15 --chars "0123456789"
```

<br/>

### ▶️ Salvar todos os frames ASCII

```bash
python main.py video.mp4 --save

OUTPUT:
ascii_frames_YYYYMMDD_HHMMSS/
    frame_000001.txt
    frame_000002.txt
    frame_000003.txt
    ...
    config.json
```

<br/>

## ⚙️ Parâmetros

| Parâmetro          | Descrição                     |
| ------------------ | ----------------------------- |
| `video`            | Caminho do vídeo              |
| `-w --width`       | Largura da renderização ASCII |
| `--fps`            | FPS alvo                      |
| `--seconds`        | Tempo máximo de reprodução    |
| `-s --skip-frames` | Pular frames para performance |
| `-d --audio-delay` | Delay para sincronizar áudio  |
| `--chars`          | Conjunto de caracteres ASCII  |
| `--frames-all`     | Usar todos os frames          |
| `--save`           | Salvar frames ASCII           |

---

**Desenvolvido com ❤️ para a comunidade de desenvolvimento** <br/>

*Versão Atual: 1.5.0 | Compatível com: Windows, Linux, macOS*
