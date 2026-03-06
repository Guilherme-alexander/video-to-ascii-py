# 🎬 ASCII Video Player (Terminal)

Reproduz vídeos diretamente no **terminal como ASCII Art colorido**, sincronizado com **áudio extraído automaticamente do vídeo**.

O projeto converte cada frame do vídeo em caracteres ASCII coloridos usando ANSI escape codes e reproduz o áudio simultaneamente.

O vídeo aparece como uma animação ASCII colorida dentro do terminal.

<br/>

## 🚀 Features

- 🎥 **ASCII art colorido** com cores originais do vídeo
- 🔊 **Extração automática de áudio** (moviepy + FFmpeg)
- 🎵 **Sincronização perfeita** com pygame mixer
- 📏 **Controle preciso de altura** (`--height`) para qualquer terminal
- ⚡ **FPS configurável** + skip inteligente de frames
- 🖥️ **Detecção automática** do tamanho do terminal
- 💾 **Salvar frames ASCII** com metadata JSON
- 🎛️ **Caracteres 100% customizáveis**
- 🔧 **Performance otimizada** para vídeos longos
- 📱 **Multiplataforma**: Windows/Linux/macOS
- 🎯 **Sem scrollback** - experiência limpa e imersiva

<br/>

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/ascii-video-player.git
cd ascii-video-player
```

Instale as dependências Python:

```bash
pip install -r requirements.txt
```

<br/>

## 📦 Dependências

### Python 3.8+
  
* **opencv-python** - Processamento de frames do vídeo
* **pygame** - Reprodução de áudio
* **moviepy** - Extração de áudio do vídeo

<br/>

## 🎧 Instalando FFmpeg

O projeto também depende do **FFmpeg** para manipulação de áudio.
FFmpeg é usado internamente pelo moviepy para extrair o áudio do vídeo.

1. Baixe o FFmpeg: [Download FFmpeg](https://ffmpeg.org/download.html)
2. Extraia o arquivo zip
3. Adicione a pasta `bin` ao PATH do sistema

<br/>

## 📁 Estrutura do Projeto

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

## 📌 Como Usar

### ▶️ Exemplo básico

```bash
python main.py video.mp4
```

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

### ▶️ Controle de altura do terminal

```bash
python main.py video.mp4 --height 40 -w 100
```

### ▶️ Salvar todos os frames ASCII

```bash
python main.py video.mp4 --save

OUTPUT:
ascii_frames_YYYYMMDD_HHMMSS/
    frame_000001.txt
    frame_000002.txt
    frame_000003.txt
    ...
    config.json              # Metadados da renderização
```

<br/>

## ⚙️ Parâmetros

| Parâmetro          | Descrição                               | Padrão     |
| ------------------ | --------------------------------------- | ---------- |
| `video`            | Caminho do vídeo                        | Obrigatório|
| `-w --width`       | Largura da renderização ASCII           | `115`      |
| `--height`         | Altura máxima em linhas do terminal     | `29`       |
| `--fps`            | FPS alvo da reprodução                  | `34`       |
| `--seconds`        | Tempo máximo de reprodução (segundos)   | `180`      |
| `-s --skip-frames` | Pular frames para performance           | `15`       |
| `-d --audio-delay` | Delay para sincronizar áudio (segundos) | `5.0`      |
| `--chars`          | Conjunto de caracteres ASCII            | ` .:-=+*#%@`|
| `--frames-all`     | Usar todos os frames (ignora skip)      | `False`    |
| `--save`           | Salvar frames ASCII em arquivos         | `False`    |

<br/>

## 🎯 Performance

O player é otimizado para vídeos longos através de:
- **Skip de frames** configurável
- **Resize inteligente** dos frames
- **Cache de altura** do primeiro frame
- **Renderização eficiente** com ANSI codes
- **Controle preciso** de timing via pygame

<br/>

## 🐛 Solução de Problemas

### Áudio não sincroniza
Ajuste o parâmetro `-d` ou `--audio-delay`:
```bash
python main.py video.mp4 -d 3.0
```

### Terminal pequeno demais
Use `--height` para limitar a altura:
```bash
python main.py video.mp4 --height 20
```

### Performance lenta
Aumente o skip de frames:
```bash
python main.py video.mp4 -s 30
```

### Caracteres estranhos
Teste diferentes conjuntos de caracteres:
```bash
python main.py video.mp4 --chars "█▓▒░ "
```

<br/>

## 📝 Notas de Versão

### Versão 1.5.0
- ✨ Novo parâmetro `--height` para controle preciso da altura
- 🔧 Melhorias na detecção do terminal
- ⚡ Otimização de renderização
- 🐛 Correção de bugs no scrollback
- 📁 Salvamento com metadados JSON

<br/>

---

**Desenvolvido com ❤️ para a comunidade de desenvolvimento** <br/>

*Versão Atual: 1.5.0 | Compatível com: Windows, Linux, macOS*