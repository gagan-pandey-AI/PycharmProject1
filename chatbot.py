"""
Project: Talking AI For You
Author: Gagan Pandey
Course: BCA AI
"""

import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import openai
import threading
import datetime

# ==============================
# 🔐 ADD YOUR OPENAI API KEY HERE
# ==============================
openai.api_key = "PASTE_YOUR_OPENAI_API_KEY_HERE"

# ==============================
# 🎤 Speech Recognition Setup
# ==============================
recognizer = sr.Recognizer()

# ==============================
# 🔊 Text To Speech Setup
# ==============================
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    """
    Convert text to speech
    """
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        update_chat_window(f"[SYSTEM] Speech Error: {e}")

def listen():
    """
    Listen from microphone and convert speech to text
    """
    try:
        with sr.Microphone() as source:
            update_chat_window("[SYSTEM] Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        update_chat_window(f"You: {text}")
        return text

    except sr.UnknownValueError:
        update_chat_window("[SYSTEM] Could not understand audio.")
    except sr.RequestError:
        update_chat_window("[SYSTEM] Internet connection error.")
    except Exception as e:
        update_chat_window(f"[SYSTEM] Microphone Error: {e}")

    return None

def generate_response(user_text):
    """
    Send text to OpenAI and get AI response
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and intelligent AI assistant."},
                {"role": "user", "content": user_text}
            ]
        )

        ai_text = response["choices"][0]["message"]["content"]
        return ai_text

    except Exception as e:
        return f"AI Error: {e}"

def update_chat_window(message):
    """
    Update chat window and save conversation
    """
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, message + "\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    # Save to file
    with open("conversation_history.txt", "a", encoding="utf-8") as file:
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{time_stamp}] {message}\n")

def process_voice():
    """
    Full pipeline: Listen → AI → Speak
    """
    user_text = listen()
    if user_text:
        ai_response = generate_response(user_text)
        update_chat_window(f"AI: {ai_response}")
        speak(ai_response)

def start_listening():
    """
    Run in separate thread (prevents GUI freezing)
    """
    threading.Thread(target=process_voice).start()

# ==============================
# 🖥 MODERN GUI SETUP
# ==============================

root = tk.Tk()
root.title("Talking AI For You - Gagan Pandey")
root.geometry("700x550")
root.configure(bg="#1e1e2f")

# Header
header = tk.Label(
    root,
    text="🤖 Talking AI For You",
    font=("Segoe UI", 18, "bold"),
    bg="#111122",
    fg="white",
    pady=10
)
header.pack(fill=tk.X)

# Chat Area Frame
chat_frame = tk.Frame(root, bg="#1e1e2f")
chat_frame.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

chat_area = scrolledtext.ScrolledText(
    chat_frame,
    wrap=tk.WORD,
    state=tk.DISABLED,
    font=("Segoe UI", 11),
    bg="#2b2b3c",
    fg="white",
    insertbackground="white",
    relief=tk.FLAT
)
chat_area.pack(fill=tk.BOTH, expand=True)

# Button Frame
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=15)

start_button = tk.Button(
    button_frame,
    text="🎤 Start Listening",
    font=("Segoe UI", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    padx=20,
    pady=8,
    bd=0,
    command=start_listening
)
start_button.pack()

# Startup Greeting
startup_message = "Hello, I am your Talking AI. How can I help you?"
update_chat_window("AI: " + startup_message)
speak(startup_message)

root.mainloop()