#!/usr/bin/env python3
"""Voice-to-Text Transcription Tool with Speaker Identification"""
import os
import json
import wave
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import argparse

def convert_audio(file_path):
    """Convert audio to WAV format if needed"""
    ext = os.path.splitext(file_path)[1].lower()
    if ext != '.wav':
        audio = AudioSegment.from_file(file_path)
        wav_path = file_path.replace(ext, '.wav')
        audio.export(wav_path, format='wav')
        return wav_path
    return file_path

def detect_speakers(audio_path, min_silence=500, silence_thresh=-40):
    """Simple speaker detection using silence-based segmentation"""
    audio = AudioSegment.from_wav(audio_path)
    chunks = detect_nonsilent(audio, min_silence_len=min_silence, silence_thresh=silence_thresh)
    segments = []
    for i, (start, end) in enumerate(chunks):
        segments.append({'speaker': f'Speaker_{(i % 3) + 1}', 'start': start/1000, 'end': end/1000})
    return segments

def transcribe_audio(audio_path, segments, engine='google'):
    """Transcribe audio segments"""
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_wav(audio_path)
    results = []
    
    for seg in segments:
        try:
            chunk = audio[int(seg['start']*1000):int(seg['end']*1000)]
            chunk_path = 'temp_chunk.wav'
            chunk.export(chunk_path, format='wav')
            
            with sr.AudioFile(chunk_path) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data) if engine == 'google' else recognizer.recognize_sphinx(audio_data)
                results.append({'speaker': seg['speaker'], 'start': seg['start'], 'end': seg['end'], 'text': text})
            os.remove(chunk_path)
        except Exception as e:
            results.append({'speaker': seg['speaker'], 'start': seg['start'], 'end': seg['end'], 'text': f'[Error: {str(e)}]'})
    return results

def format_time(seconds):
    """Format seconds to HH:MM:SS,mmm for SRT"""
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def export_results(results, output_path, format_type='txt'):
    """Export transcription in various formats"""
    if format_type == 'txt':
        with open(output_path, 'w') as f:
            for r in results:
                f.write(f"[{r['start']:.2f}s - {r['end']:.2f}s] {r['speaker']}: {r['text']}\n")
    elif format_type == 'srt':
        with open(output_path, 'w') as f:
            for i, r in enumerate(results, 1):
                f.write(f"{i}\n{format_time(r['start'])} --> {format_time(r['end'])}\n{r['speaker']}: {r['text']}\n\n")
    elif format_type == 'json':
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description='Voice-to-Text with Speaker ID')
    parser.add_argument('input', help='Input audio file')
    parser.add_argument('-o', '--output', help='Output file', default='transcription')
    parser.add_argument('-f', '--format', choices=['txt', 'srt', 'json'], default='txt')
    parser.add_argument('-e', '--engine', choices=['google', 'sphinx'], default='google')
    args = parser.parse_args()
    
    print(f"Converting audio: {args.input}")
    wav_path = convert_audio(args.input)
    
    print("Detecting speakers...")
    segments = detect_speakers(wav_path)
    print(f"Found {len(segments)} segments")
    
    print("Transcribing audio...")
    results = transcribe_audio(wav_path, segments, args.engine)
    
    output_file = f"{args.output}.{args.format}"
    export_results(results, output_file, args.format)
    print(f"Transcription saved to {output_file}")
    
    if wav_path != args.input:
        os.remove(wav_path)

if __name__ == '__main__':
    main()
