# Piano Music Generator

A creative Python project that transforms images into piano music by mapping pixel brightness to musical notes. Convert visual art into auditory experiences!

## Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Security](#security)
- [How to Contribute](#how-to-contribute)
- [What's Next](#whats-next)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Author](#author)

## About

Piano Music Generator is an experimental project that bridges the gap between visual and audio art. By analyzing pixel data from images and converting brightness values to musical notes, this tool creates unique piano compositions based on visual input. Whether you're exploring creative coding, data sonification, or just having fun with Python, this project offers an accessible entry point into multimedia processing.

## Features

- 🎨 **Image to Music Conversion**: Transform any image into a piano composition
- 🎵 **MIDI Export**: Generate playable MIDI files from images
- 🔊 **Music21 Integration**: Generate proper music notation using music21
- ⚡ **Efficient Processing**: Samples pixels intelligently to create manageable compositions
- 🎹 **Customizable Mappings**: Adjust sampling rates, note ranges, and base octaves
- 🔄 **Flexible**: Works with any image format supported by Pillow

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.x |
| **Image Processing** | Pillow (PIL) |
| **Music Notation** | music21 |
| **Format Support** | PNG, JPG, BMP, GIF, and more |

## Architecture

The application follows a simple pipeline architecture:

```
Input Image
    ↓
Grayscale Conversion (Luminance Values: 0-255)
    ↓
Pixel Data Extraction & Sampling
    ↓
Pixel-to-Note Mapping (Formula: Note = 60 + pixel//15)
    ↓
Music Stream Creation
    ↓
Output/Display
```

**Key Processing Steps:**
1. **Image Loading**: Opens image file using Pillow
2. **Grayscale Conversion**: Normalizes to single-channel luminance
3. **Sampling**: Extracts every Nth pixel (configurable)
4. **Mapping**: Converts brightness to MIDI note values
5. **Composition**: Builds a musical stream with music21
6. **Rendering**: Displays as text notation or exports

## Project Structure

```
PianoMusicGenerator/
├── run.py                      # Main script - entry point
├── README.md                   # This file
├── SyntronicLabsStandup.png    # Example image
├── output.mid                  # Generated MIDI file (created after running script)
└── requirements.txt            # Python dependencies (optional)
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the repository**:
   ```bash
   git clone https://github.com/JackSawyerWATX/PianoMusicGenerator.git
   cd PianoMusicGenerator
   ```

2. **Install dependencies**:
   ```bash
   pip install Pillow music21
   ```

   Or create a requirements file:
   ```bash
   pip install -r requirements.txt
   ```

### Quick Start

1. **Prepare an image**: Place your image file in the project directory
2. **Update the filename** in `run.py`:
   ```python
   img = Image.open("your_image.png").convert("L")
   ```
3. **Run the script**:
   ```bash
   python run.py
   ```
4. **Play the result**: A MIDI file `output.mid` is generated and ready to play!

### Basic Example

```python
from PIL import Image
from music21 import stream, note, instrument

# Load and convert image to grayscale
img = Image.open("SyntronicLabsStandup.png").convert("L")

# Create a music stream and add piano instrument
s = stream.Stream()
s.append(instrument.Piano())

# Convert pixels to notes
pixels = list(img.getdata())
for pixel in pixels[::500]:  # Sample every 500th pixel
    n = note.Note(60 + pixel//15)  # Map brightness to note
    s.append(n)

# Export to MIDI file
s.write('midi', fp='output.mid')
print("✓ MIDI file saved as 'output.mid'")
```

## Playing the Generated Music

After running the script, `output.mid` is created and ready to play:

**Option 1: Play with Media Player**
- Double-click `output.mid` in Windows File Explorer
- Opens with your default media player (VLC, Windows Media Player, etc.)

**Option 2: Open in Music Notation Software**
- MuseScore (free): https://musescore.org/
- Finale, Sibelius, or other notation software
- View the sheet music and listen to playback

**Option 3: Playback Online**
- Use online MIDI players (search "MIDI player online")
- Upload your `output.mid` file
- Listen in your browser

## Configuration

Customize the output by adjusting these parameters in `run.py`:

| Parameter | Description | Default | Example |
|-----------|-------------|---------|---------|
| `[::500]` | Pixel sampling interval | 500 | `[::250]` (more notes), `[::1000]` (fewer notes) |
| `60` | Base MIDI note value | 60 (Middle C) | `48` (lower), `72` (higher) |
| `15` | Brightness scaling factor | 15 | `10` (wider range), `20` (narrower range) |

### Examples

**More notes with wider range**:
```python
for pixel in pixels[::250]:
    n = note.Note(48 + pixel//10)
    s.append(n)
```

**Fewer, higher notes**:
```python
for pixel in pixels[::1000]:
    n = note.Note(72 + pixel//20)
    s.append(n)
```

## Security

- ✅ **File Input**: Only opens image files from specified paths
- ✅ **No External API Calls**: All processing is local
- ✅ **Safe Dependencies**: Uses well-maintained open-source libraries
- ⚠️ **File Permissions**: Ensure read access to image files
- ⚠️ **Memory Usage**: Large images may consume significant memory during processing

**Best Practices:**
- Validate image file paths before processing
- Test with small images first
- Monitor resource usage with large datasets

## How to Contribute

We welcome contributions! Here's how you can help:

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/PianoMusicGenerator.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** and test thoroughly

4. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: description of changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Submit a Pull Request** with a description of your changes

### Areas for Contribution

- 🎨 RGB/Color-aware note mapping
- 🔊 Direct audio playback (in-app)
- 📈 Performance optimization for large images
- 📖 Additional documentation and examples
- 🧪 Unit tests and test coverage
- 🐛 Bug fixes and improvements

## What's Next

Future enhancements and roadmap items:

- [x] **MIDI Export**: Generate MIDI files directly ✅
- [ ] **Color Mapping**: Map RGB channels to different instruments
- [ ] **WAV Export**: Generate WAV files with sound synthesis
- [ ] **Web Interface**: Browser-based image-to-music converter
- [ ] **Real-time Preview**: Live audio playback during generation
- [ ] **Advanced Filters**: Edge detection, contrast adjustment
- [ ] **Batch Processing**: Convert multiple images at once
- [ ] **Multiple Instruments**: Use different instruments per color channel
- [ ] **Tempo Control**: Adjust speed of generated compositions
- [ ] **CLI Tool**: Command-line interface for easier usage
- [ ] **Performance Metrics**: Benchmark and optimize processing speed
- [ ] **Video Tutorials**: Step-by-step guides

## License

This project is open source and available under the MIT License. See `LICENSE` file for details (if present).

## Acknowledgements

- **Pillow Team**: For the excellent image processing library
- **music21**: MIT License - For comprehensive music notation capabilities
- **Python Community**: For the amazing open-source ecosystem
- **Creative Coding Community**: For inspiration and support

Special thanks to all contributors and users who help improve this project!

## Author

**Jack Sawyer**
- GitHub: [@JackSawyerWATX](https://github.com/JackSawyerWATX)
- Repository: [Piano Music Generator](https://github.com/JackSawyerWATX/PianoMusicGenerator)

Feel free to reach out with questions, suggestions, or collaboration ideas!

---

**Last Updated**: June 2026

**Version**: 1.0.0
