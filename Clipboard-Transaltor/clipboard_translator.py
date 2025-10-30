import pyperclip
import time
from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException
import threading

class ClipboardTranslator:
    def __init__(self):
        self.previous_text = ""
        self.translator_cache = {}
        
    def get_translator(self, source_lang):
        """Cache translator instances for faster subsequent translations"""
        if source_lang not in self.translator_cache:
            self.translator_cache[source_lang] = GoogleTranslator(source=source_lang, target='en')
        return self.translator_cache[source_lang]
    
    def translate_to_english(self, text):
        """
        Translate text to English using Google Translate API
        
        Args:
            text: Text to translate
            
        Returns:
            Translated text and detected language
        """
        try:
            # Quick length check
            if len(text) > 5000:
                return None, None, "Text too long (max 5000 characters)"
            
            # Detect language
            detected_lang = detect(text)
            
            # Skip if already in English
            if detected_lang == 'en':
                return None, 'en', None
            
            # Use cached translator
            translator = self.get_translator(detected_lang)
            translation = translator.translate(text)
            
            return translation, detected_lang, None
            
        except LangDetectException:
            return None, None, "Could not detect language"
        except Exception as e:
            return None, None, str(e)
    
    def process_clipboard(self, text):
        """Process clipboard text in a separate thread"""
        print("-" * 60)
        print(f"Detected text: {text[:100]}{'...' if len(text) > 100 else ''}")
        print("Translating...")
        
        # Translate the text
        translated, lang, error = self.translate_to_english(text)
        
        if error:
            print(f"❌ Error: {error}")
        elif translated:
            print(f"\n✓ Detected language: {lang}")
            print(f"✓ Translation (EN): {translated[:200]}{'...' if len(translated) > 200 else ''}")
            print("\n✓ Translation copied to clipboard!")
            
            # Copy translation back to clipboard
            pyperclip.copy(translated)
        else:
            if lang == 'en':
                print("✓ Text is already in English - no translation needed.")
            else:
                print("❌ Could not translate text.")
        
        print("-" * 60 + "\n")
    
    def monitor_clipboard(self):
        """
        Continuously monitor clipboard for changes and translate new text
        """
        print("=" * 60)
        print("🚀 Fast Clipboard Translator Started!")
        print("=" * 60)
        print("📋 Copy any text to automatically translate it to English.")
        print("⌨️  Press Ctrl+C to stop.\n")
        
        try:
            while True:
                # Get current clipboard content
                try:
                    current_text = pyperclip.paste()
                except:
                    current_text = ""
                
                # Check if clipboard content has changed
                if current_text != self.previous_text and current_text.strip():
                    self.previous_text = current_text
                    
                    # Process in a separate thread for non-blocking operation
                    thread = threading.Thread(target=self.process_clipboard, args=(current_text,))
                    thread.daemon = True
                    thread.start()
                
                # Check clipboard every 0.3 seconds (faster polling)
                time.sleep(0.3)
                
        except KeyboardInterrupt:
            print("\n" + "=" * 60)
            print("👋 Clipboard translator stopped.")
            print("=" * 60)

if __name__ == "__main__":
    # Required packages:
    # pip install pyperclip deep-translator langdetect
    
    translator = ClipboardTranslator()
    translator.monitor_clipboard()