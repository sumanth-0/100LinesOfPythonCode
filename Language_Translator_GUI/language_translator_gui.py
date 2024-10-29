import tkinter as tk
from tkinter import messagebox, scrolledtext, font
from googletrans import Translator

def translate_text():
    translator = Translator()
    text = input_text.get("1.0", tk.END).strip()
    dest_language = lang_code_entry.get().strip()

    if text and dest_language:
        try:
            detected_lang = translator.detect(text).lang
            language_format = f"{detected_lang.upper()} -> {dest_language.upper()}"
            detected_lang_label.config(text=language_format) 
            translated = translator.translate(text, dest=dest_language)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, f" {translated.text}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please enter text and target language code.")

def display_language_codes():
    lang_codes = "\nCommon Language Codes:\n"
    lang_codes += " - 'en' : English\n"
    lang_codes += " - 'es' : Spanish\n"
    lang_codes += " - 'fr' : French\n"
    lang_codes += " - 'de' : German\n"
    lang_codes += " - 'it' : Italian\n"
    lang_codes += " - 'zh-cn' : Chinese (Simplified)\n"
    lang_codes += " - 'ja' : Japanese\n"
    lang_codes += " - 'ko' : Korean\n"
    lang_codes += " - 'hi' : Hindi\n"
    lang_codes += " - 'ar' : Arabic\n"
    lang_codes += " - 'ru' : Russian\n"
    lang_codes += " - 'pt' : Portuguese"
    
    messagebox.showinfo("Language Codes", lang_codes)

# GUI setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x500")
root.config(bg="#f5f5f5")
custom_font = font.Font(family="Helvetica", size=12)

# Input text box
input_label = tk.Label(root, text="Enter text to translate:", bg="#f5f5f5", font=custom_font)
input_label.pack(pady=(10, 5))
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=5, font=custom_font)
input_text.pack(pady=(0, 10))

# Language code input
lang_code_label = tk.Label(root, text="Enter target language code:", bg="#f5f5f5", font=custom_font)
lang_code_label.pack(pady=(10, 5))
lang_code_entry = tk.Entry(root, width=20, font=custom_font)
lang_code_entry.pack(pady=(0, 10))

# Show language codes button
lang_codes_button = tk.Button(root, text="Show Language Codes", command=display_language_codes, bg="#2196F3", fg="white", font=custom_font)
lang_codes_button.pack(pady=(5, 10))

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=custom_font)
translate_button.pack(pady=(10, 5))

# Detected language label
detected_lang_label = tk.Label(root, text="", bg="#f5f5f5", font=custom_font)
detected_lang_label.pack(pady=(10, 5))

# Output
output_label = tk.Label(root, text="Translated text:", bg="#f5f5f5", font=custom_font)
output_label.pack(pady=(10, 5))
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=5, font=custom_font)
output_text.pack(pady=(0, 10))


root.mainloop()
