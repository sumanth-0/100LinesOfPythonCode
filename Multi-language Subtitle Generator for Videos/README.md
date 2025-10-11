# Multi-language Subtitle Generator for Videos

A Python script that automatically generates English subtitles from video audio using Whisper AI and translates them into multiple languages using Google Translate.

## Features

- 🎬 Extract audio and transcribe from video files automatically
- 🗣️ Generate accurate English subtitles using OpenAI's Whisper model
- 🌍 Translate subtitles into multiple languages simultaneously
- 📝 Export subtitles in standard SRT format
- 🚀 Simple command-line interface
- 📦 Uses only open-source libraries

## Requirements

- Python 3.7+
- FFmpeg (required by Whisper for audio processing)

## Installation

1. Install FFmpeg:
   ```bash
   # On Ubuntu/Debian
   sudo apt install ffmpeg
   
   # On macOS
   brew install ffmpeg
   
   # On Windows
   # Download from https://ffmpeg.org/download.html
   ```

2. Install required Python packages:
   ```bash
   pip install openai-whisper googletrans==4.0.0-rc1 srt
   ```

## Usage

### Basic Usage (English subtitles only)
```bash
python subtitle_generator.py video.mp4
```

### Generate subtitles in multiple languages
```bash
python subtitle_generator.py video.mp4 es fr de ja
```

This will generate:
- `video_subtitles/video_en.srt` - English subtitles
- `video_subtitles/video_es.srt` - Spanish subtitles
- `video_subtitles/video_fr.srt` - French subtitles
- `video_subtitles/video_de.srt` - German subtitles
- `video_subtitles/video_ja.srt` - Japanese subtitles

## Supported Languages

The script supports all languages available in Google Translate. Common language codes:
- `es` - Spanish
- `fr` - French
- `de` - German
- `ja` - Japanese
- `zh-cn` - Chinese (Simplified)
- `ko` - Korean
- `ar` - Arabic
- `hi` - Hindi
- `pt` - Portuguese
- `ru` - Russian

## How It Works

1. **Audio Transcription**: Uses OpenAI's Whisper model to transcribe audio from the video
2. **Subtitle Generation**: Converts the transcription with timestamps into SRT format
3. **Translation**: Uses Google Translate API to translate subtitles into target languages
4. **Output**: Saves all subtitles in a dedicated folder

## Whisper Model Sizes

By default, the script uses the "base" model. You can modify this in the code:
- `tiny` - Fastest, least accurate
- `base` - Good balance (default)
- `small` - Better accuracy
- `medium` - High accuracy
- `large` - Best accuracy, slowest

## Example

```bash
# Generate English and Spanish subtitles
python subtitle_generator.py my_video.mp4 es

# Output:
# Loading Whisper model: base...
# Transcribing: my_video.mp4...
# English subtitles saved: my_video_subtitles/my_video_en.srt
# Translating to es...
# Translated subtitles saved: my_video_subtitles/my_video_es.srt
#
# All subtitles generated in: my_video_subtitles
```

## Notes

- First run will download the Whisper model (~140MB for base model)
- Processing time depends on video length and selected Whisper model
- Internet connection required for translation
- Supports most common video formats (mp4, avi, mov, etc.)

## License

This project is open source and available for educational purposes.

## Contributing

Issue: #635 - Multi-language Subtitle Generator for Videos
