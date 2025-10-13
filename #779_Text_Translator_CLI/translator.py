"""
Text Translation Tool using Googletrans
A Hacktoberfest project for translating text between multiple languages
"""

from googletrans import Translator, LANGUAGES
import argparse
import sys
import json

class TextTranslator:
    def __init__(self):
        self.translator = Translator()
        self.supported_languages = LANGUAGES
    
    def get_language_code(self, language_input):
        """
        Convert language name to code, or validate if already a code
        """
        language_input = language_input.lower().strip()
        
        # If it's already a valid language code
        if language_input in self.supported_languages:
            return language_input
        
        # Search for language name and return code
        for code, name in self.supported_languages.items():
            if language_input == name.lower():
                return code
        
        return None
    
    def detect_language(self, text):
        """
        Detect the language of the input text
        """
        try:
            detection = self.translator.detect(text)
            return detection.lang, detection.confidence
        except Exception as e:
            print(f"Error detecting language: {e}")
            return None, None
    
    def translate_text(self, text, dest_lang, src_lang='auto'):
        """
        Translate text to target language
        """
        try:
            translation = self.translator.translate(
                text, 
                dest=dest_lang, 
                src=src_lang
            )
            
            return {
                'original_text': text,
                'translated_text': translation.text,
                'source_language': translation.src,
                'target_language': translation.dest,
                'pronunciation': translation.pronunciation
            }
        except Exception as e:
            print(f"Translation error: {e}")
            return None
    
    def batch_translate(self, texts, dest_lang, src_lang='auto'):
        """
        Translate multiple texts at once
        """
        try:
            translations = self.translator.translate(
                texts, 
                dest=dest_lang, 
                src=src_lang
            )
            
            results = []
            for translation in translations:
                results.append({
                    'original_text': translation.origin,
                    'translated_text': translation.text,
                    'source_language': translation.src,
                    'target_language': translation.dest,
                    'pronunciation': translation.pronunciation
                })
            
            return results
        except Exception as e:
            print(f"Batch translation error: {e}")
            return None
    
    def list_supported_languages(self, search_term=None):
        """
        List all supported languages, optionally filtered by search term
        """
        print("\n🌍 Supported Languages:")
        print("-" * 40)
        
        languages_list = []
        for code, name in self.supported_languages.items():
            if search_term and search_term.lower() not in name.lower():
                continue
            languages_list.append((code, name))
            print(f"{code:>5} - {name}")
        
        return languages_list
    
    def interactive_mode(self):
        """
        Interactive mode for continuous translation
        """
        print("🚀 Interactive Translation Mode")
        print("Type 'quit' to exit, 'list' to see languages, 'detect' to detect language")
        print("-" * 50)
        
        while True:
            text = input("\nEnter text to translate: ").strip()
            
            if text.lower() == 'quit':
                break
            elif text.lower() == 'list':
                self.list_supported_languages()
                continue
            elif text.lower() == 'detect':
                detect_text = input("Enter text to detect language: ")
                lang, confidence = self.detect_language(detect_text)
                if lang:
                    lang_name = self.supported_languages.get(lang, 'Unknown')
                    print(f"Detected: {lang_name} ({lang}) with {confidence:.2%} confidence")
                continue
            
            target_lang = input("Enter target language (code or name): ").strip()
            lang_code = self.get_language_code(target_lang)
            
            if not lang_code:
                print("❌ Invalid language. Type 'list' to see supported languages.")
                continue
            
            source_lang = input("Enter source language (or 'auto' for detection): ").strip()
            src_code = 'auto'
            if source_lang and source_lang.lower() != 'auto':
                src_code = self.get_language_code(source_lang)
                if not src_code:
                    print("❌ Invalid source language. Using auto-detection.")
                    src_code = 'auto'
            
            result = self.translate_text(text, lang_code, src_code)
            
            if result:
                self.display_translation(result)
    
    def display_translation(self, result):
        """
        Display translation results in a formatted way
        """
        print("\n" + "="*50)
        print("📝 TRANSLATION RESULT")
        print("="*50)
        print(f"Original ({result['source_language']}): {result['original_text']}")
        print(f"Translated ({result['target_language']}): {result['translated_text']}")
        if result['pronunciation']:
            print(f"Pronunciation: {result['pronunciation']}")
        print("="*50)

def main():
    parser = argparse.ArgumentParser(description='Text Translation Tool using Googletrans')
    parser.add_argument('--text', '-t', help='Text to translate')
    parser.add_argument('--dest', '-d', help='Target language code or name')
    parser.add_argument('--src', '-s', help='Source language code or name (default: auto)', default='auto')
    parser.add_argument('--file', '-f', help='File containing text to translate')
    parser.add_argument('--batch', '-b', nargs='+', help='Multiple texts to translate')
    parser.add_argument('--detect', help='Detect language of given text')
    parser.add_argument('--list-langs', action='store_true', help='List all supported languages')
    parser.add_argument('--search-langs', help='Search for languages by name')
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive mode')
    parser.add_argument('--output', '-o', help='Output file for results')
    
    args = parser.parse_args()
    translator = TextTranslator()
    
    # List supported languages
    if args.list_langs:
        translator.list_supported_languages()
        return
    
    # Search languages
    if args.search_langs:
        translator.list_supported_languages(args.search_langs)
        return
    
    # Detect language
    if args.detect:
        lang, confidence = translator.detect_language(args.detect)
        if lang:
            lang_name = translator.supported_languages.get(lang, 'Unknown')
            print(f"Detected language: {lang_name} ({lang})")
            print(f"Confidence: {confidence:.2%}")
        return
    
    # Interactive mode
    if args.interactive:
        translator.interactive_mode()
        return
    
    # File translation
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read().strip()
            args.text = text
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    
    # Batch translation
    if args.batch and args.dest:
        lang_code = translator.get_language_code(args.dest)
        if not lang_code:
            print("❌ Invalid target language")
            return
        
        src_code = 'auto'
        if args.src and args.src.lower() != 'auto':
            src_code = translator.get_language_code(args.src)
            if not src_code:
                print("❌ Invalid source language. Using auto-detection.")
                src_code = 'auto'
        
        results = translator.batch_translate(args.batch, lang_code, src_code)
        
        if results:
            for i, result in enumerate(results):
                print(f"\n--- Translation {i+1} ---")
                translator.display_translation(result)
            
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    json.dump(results, f, indent=2, ensure_ascii=False)
                print(f"\n✅ Results saved to {args.output}")
        return
    
    # Single text translation
    if args.text and args.dest:
        lang_code = translator.get_language_code(args.dest)
        if not lang_code:
            print("❌ Invalid target language")
            return
        
        src_code = 'auto'
        if args.src and args.src.lower() != 'auto':
            src_code = translator.get_language_code(args.src)
            if not src_code:
                print("❌ Invalid source language. Using auto-detection.")
                src_code = 'auto'
        
        result = translator.translate_text(args.text, lang_code, src_code)
        
        if result:
            translator.display_translation(result)
            
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
                print(f"\n✅ Result saved to {args.output}")
        return
    
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        print("\n💡 Try --interactive for interactive mode")

if __name__ == "__main__":
    main()