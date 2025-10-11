import os
import sys
from pathlib import Path

try:
    import whisper
    from googletrans import Translator
    import srt
    from datetime import timedelta
except ImportError as e:
    print(f"Missing required library: {e}")
    print("Install with: pip install openai-whisper googletrans==4.0.0-rc1 srt")
    sys.exit(1)

def extract_audio_and_transcribe(video_path, model_size="base"):
    """Extract audio and transcribe using Whisper."""
    print(f"Loading Whisper model: {model_size}...")
    model = whisper.load_model(model_size)
    
    print(f"Transcribing: {video_path}...")
    result = model.transcribe(str(video_path), task="transcribe")
    return result

def create_srt_subtitles(segments, output_path):
    """Create SRT subtitle file from segments."""
    subtitles = []
    for i, segment in enumerate(segments, start=1):
        start = timedelta(seconds=segment['start'])
        end = timedelta(seconds=segment['end'])
        text = segment['text'].strip()
        subtitle = srt.Subtitle(index=i, start=start, end=end, content=text)
        subtitles.append(subtitle)
    
    srt_content = srt.compose(subtitles)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(srt_content)
    print(f"English subtitles saved: {output_path}")
    return subtitles

def translate_subtitles(subtitles, target_lang, output_path):
    """Translate subtitles to target language."""
    translator = Translator()
    translated_subs = []
    
    print(f"Translating to {target_lang}...")
    for subtitle in subtitles:
        try:
            translated = translator.translate(subtitle.content, dest=target_lang)
            new_subtitle = srt.Subtitle(
                index=subtitle.index,
                start=subtitle.start,
                end=subtitle.end,
                content=translated.text
            )
            translated_subs.append(new_subtitle)
        except Exception as e:
            print(f"Translation error for segment {subtitle.index}: {e}")
            translated_subs.append(subtitle)
    
    srt_content = srt.compose(translated_subs)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(srt_content)
    print(f"Translated subtitles saved: {output_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python subtitle_generator.py <video_path> [languages]")
        print("Example: python subtitle_generator.py video.mp4 es fr de")
        sys.exit(1)
    
    video_path = Path(sys.argv[1])
    if not video_path.exists():
        print(f"Error: Video file not found: {video_path}")
        sys.exit(1)
    
    target_languages = sys.argv[2:] if len(sys.argv) > 2 else []
    
    # Transcribe video to English
    result = extract_audio_and_transcribe(video_path)
    
    # Create output directory
    output_dir = video_path.parent / f"{video_path.stem}_subtitles"
    output_dir.mkdir(exist_ok=True)
    
    # Save English subtitles
    en_output = output_dir / f"{video_path.stem}_en.srt"
    subtitles = create_srt_subtitles(result['segments'], en_output)
    
    # Translate to other languages
    for lang in target_languages:
        lang_output = output_dir / f"{video_path.stem}_{lang}.srt"
        translate_subtitles(subtitles, lang, lang_output)
    
    print(f"\nAll subtitles generated in: {output_dir}")

if __name__ == "__main__":
    main()
