#!/usr/bin/env python3


import speech_recognition as sr

import sys, time


class SpeechCommandRecognizer:
    """Recognizes and processes basic voice commands"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.is_running = False
        self.is_paused = False
        self.commands = {
            'start': lambda: self.set_state(True, False, "START", "🚀 System started!"),
            'stop': lambda: self.set_state(False, False, "STOP", "🛑 System stopped!"),
            'pause': lambda: self.set_state(self.is_running, True, "PAUSE", "⏸️  System paused!"),
            'resume': lambda: self.set_state(self.is_running, False, "RESUME", "▶️  System resumed!"),
            'exit': self.exit,
            'quit': self.exit,
            'help': self.help
        }
        print("🎤 Calibrating microphone for ambient noise...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
        print("✓ Calibration complete!")
    
    def listen(self):
        try:
            with self.microphone as source:
                print("\n🎧 Listening... (speak a command)")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=3)
            print("🔄 Processing...")
            return self.recognizer.recognize_google(audio).lower()
        except sr.WaitTimeoutError:
            print("⏱️  No speech detected (timeout)"); return None
        except sr.UnknownValueError:
            print("❌ Could not understand audio"); return None
        except sr.RequestError as e:
            print(f"❌ API error: {e}"); return None
        except Exception as e:
            print(f"❌ Error: {e}"); return None
    
    def parse_command(self, text):
        if not text: return None
        for cmd in self.commands:
            if cmd in text: return cmd
        return None
    
    def set_state(self, running, paused, label, msg):
        print(f"✅ {label} command received!")
        self.is_running, self.is_paused = running, paused
        print(msg)
    def exit(self):
        print("✅ EXIT command received!\n👋 Goodbye!"); sys.exit(0)
    def help(self):
        print("\n📋 Commands: start, stop, pause, resume, exit, quit, help")
    def get_status(self):
        return "🟢 Running" if self.is_running and not self.is_paused else ("🟡 Paused" if self.is_paused else "⚪ Stopped")
    
    def run(self):
        print("\n🎤 Speech Command Recognizer\nSpeak: start, stop, pause, resume, exit, help\nPress Ctrl+C to quit\n")
        try:
            while True:
                print(f"Status: {self.get_status()}")
                text = self.listen()
                if text:
                    print(f'💬 You said: "{text}"')
                    cmd = self.parse_command(text)
                    if cmd:
                        print(f"🎯 Command: {cmd.upper()}"); self.commands[cmd]()
                    else:
                        print("❓ No valid command found. Say 'help'.")
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("\n⚠️  Interrupted by user\n👋 Goodbye!")


if __name__ == "__main__":
    try:
        SpeechCommandRecognizer().run()
    except Exception as e:
        print(f"❌ Fatal error: {e}"); sys.exit(1)
