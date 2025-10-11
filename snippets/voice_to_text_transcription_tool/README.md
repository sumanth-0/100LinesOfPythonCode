# Voice-to-Text Transcription Tool with Speaker Identification

A Python script that transcribes audio files to text and identifies different speakers using silence-based segmentation.

## Features

- **Multi-format Support**: Converts MP3, WAV, M4A, FLAC audio files to text
- **Speaker Identification**: Simple speaker detection using silence-based segmentation
- **Timestamp Generation**: Automatic timestamps for each speech segment
- **Multiple Export Formats**: Export transcriptions in TXT, SRT, or JSON format
- **Multiple Recognition Engines**: Support for Google Speech Recognition and CMU Sphinx
- **Audio Preprocessing**: Automatic conversion to WAV format when needed

## Requirements

```bash
pip install SpeechRecognition pydub
```

Additionally, you'll need FFmpeg installed on your system for audio format conversion:
- **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
- **macOS**: `brew install ffmpeg`
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

For offline recognition with Sphinx:
```bash
pip install pocketsphinx
```

## Usage

### Basic Usage

```bash
python voice_to_text_transcription.py input_audio.mp3
```

### Specify Output Format

```bash
# Text format (default)
python voice_to_text_transcription.py input.mp3 -o output -f txt

# SRT subtitle format
python voice_to_text_transcription.py input.mp3 -o output -f srt

# JSON format
python voice_to_text_transcription.py input.mp3 -o output -f json
```

### Choose Recognition Engine

```bash
# Use Google Speech Recognition (default, requires internet)
python voice_to_text_transcription.py input.mp3 -e google

# Use CMU Sphinx (offline)
python voice_to_text_transcription.py input.mp3 -e sphinx
```

## Command Line Options

- `input`: Input audio file path (required)
- `-o, --output`: Output file name (default: 'transcription')
- `-f, --format`: Output format - txt, srt, or json (default: txt)
- `-e, --engine`: Speech recognition engine - google or sphinx (default: google)

## Output Formats

### TXT Format
```
[0.50s - 3.20s] Speaker_1: Hello, how are you?
[3.80s - 5.60s] Speaker_2: I'm doing great, thanks!
```

### SRT Format
```
1
00:00:00,500 --> 00:00:03,200
Speaker_1: Hello, how are you?

2
00:00:03,800 --> 00:00:05,600
Speaker_2: I'm doing great, thanks!
```

### JSON Format
```json
[
  {
    "speaker": "Speaker_1",
    "start": 0.5,
    "end": 3.2,
    "text": "Hello, how are you?"
  },
  {
    "speaker": "Speaker_2",
    "start": 3.8,
    "end": 5.6,
    "text": "I'm doing great, thanks!"
  }
]
```

## How It Works

1. **Audio Conversion**: Converts input audio to WAV format if needed
2. **Speaker Detection**: Uses silence detection to segment audio into speaker turns
3. **Transcription**: Each segment is transcribed using the selected speech recognition engine
4. **Export**: Results are formatted and exported in the chosen format

## Limitations

- Speaker identification is based on simple silence detection, not voice characteristics
- Accuracy depends on audio quality and clarity
- Google Speech Recognition requires internet connection
- Sphinx works offline but may have lower accuracy

## Example

```bash
# Transcribe a podcast interview to SRT subtitle format
python voice_to_text_transcription.py podcast_interview.mp3 -o podcast_transcript -f srt

# Output: podcast_transcript.srt with speaker-labeled subtitles
```

## Issue Reference

This project addresses issue #628 from the 100LinesOfPythonCode repository.
