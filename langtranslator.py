import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from gtts import gTTS
from playsound import playsound
import os

background_color = "#336eff"

translator = Translator()

def translate_text():
    source_lang_name = source_lang_combo.get()
    target_lang_name = target_lang_combo.get()
    text_to_translate = source_text.get("1.0", tk.END).strip()

    if not text_to_translate:
        messagebox.showerror("Error", "Please enter text to translate")
        return

    try:
        source_lang = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(source_lang_name)]
        target_lang = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_lang_name)]

        translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
        translated_text.delete("1.0", tk.END)
        translated_text.insert(tk.END, translation.text)

        tts = gTTS(translation.text, lang=target_lang)
        audio_file = 'translated_audio.mp3'
        tts.save(audio_file)
        playsound(audio_file)
        os.remove(audio_file)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")

def clear_text():
    source_text.delete("1.0", tk.END)
    translated_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Language Translator")
root.geometry("900x800")
root.configure(bg=background_color)

title_label = tk.Label(root, text="Language Translator", font=("Helvetica", 22, "bold"), fg="#34495E", bg=background_color)
title_label.pack(pady=20)

frame = tk.Frame(root, bg=background_color)
frame.pack(pady=10)

source_lang_label = tk.Label(frame, text="Source Language:", font=("Arial", 12), bg=background_color, fg="#2C3E50")
source_lang_label.grid(row=0, column=0, padx=10, pady=10)

source_lang_combo = ttk.Combobox(frame, width=25, state="readonly", font=("Arial", 11))
source_lang_combo["values"] = list(LANGUAGES.values())
source_lang_combo.grid(row=0, column=1, padx=10, pady=10)
source_lang_combo.current(21)

target_lang_label = tk.Label(frame, text="Target Language:", font=("Arial", 12), bg=background_color, fg="#2C3E50")
target_lang_label.grid(row=1, column=0, padx=10, pady=10)
target_lang_combo = ttk.Combobox(frame, width=25, state="readonly", font=("Arial", 11))
target_lang_combo["values"] = list(LANGUAGES.values())
target_lang_combo.grid(row=1, column=1, padx=10, pady=10)
target_lang_combo.current(38)

source_text_label = tk.Label(root, text="Enter Text to Translate:", font=("Arial", 12), bg=background_color, fg="#2C3E50")
source_text_label.pack(pady=5)

source_text = tk.Text(root, height=5, width=60, font=("Arial", 12), bg="#ECF0F1", fg="#34495E", bd=0, highlightthickness=1, highlightbackground="#BDC3C7")
source_text.pack(pady=10)

translate_button = tk.Button(root, text="Translate and Speak", command=translate_text, bg="#1ABC9C", fg="white", font=("Arial", 14, "bold"), width=20)
translate_button.pack(pady=5)

translated_text_label = tk.Label(root, text="Translated Text:", font=("Arial", 12), bg=background_color, fg="#2C3E50")
translated_text_label.pack(pady=5)

translated_text = tk.Text(root, height=5, width=60, font=("Arial", 12), bg="#ECF0F1", fg="#34495E", bd=0, highlightthickness=1, highlightbackground="#BDC3C7")
translated_text.pack(pady=10)

clear_button = tk.Button(root, text="Clear Text", command=clear_text, bg="#E74C3C", fg="white", font=("Arial", 14, "bold"), width=20)
clear_button.pack(pady=10)

root.mainloop()