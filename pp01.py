import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Ancient India Information Portal")
root.geometry("700x500")
root.config(bg="#f4e7d3")

# Login Credentials
USERNAME = "admin"
PASSWORD = "1234"

# -------- Login Function --------
def login():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == USERNAME and pwd == PASSWORD:
        login_frame.pack_forget()
        welcome_screen()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# -------- Logout Function --------
def logout():
    welcome_frame.pack_forget()
    login_frame.pack(pady=100)

# -------- Welcome Screen --------
def welcome_screen():
    global welcome_frame
    welcome_frame = tk.Frame(root, bg="#f4e7d3")

    title = tk.Label(
        welcome_frame,
        text="Welcome to Ancient India Portal",
        font=("Arial", 20, "bold"),
        bg="#f4e7d3",
        fg="#5b3a29"
    )
    title.pack(pady=20)

    info_text = """
Ancient India was one of the greatest civilizations in history.

• Indus Valley Civilization (2500 BCE)
  - Well planned cities like Harappa and Mohenjo-Daro
  - Advanced drainage system

• Vedic Period
  - Composition of Vedas
  - Development of Hindu philosophy

• Maurya Empire
  - Emperor Ashoka promoted peace and Buddhism

• Gupta Empire
  - Known as the Golden Age of India
  - Major achievements in science and mathematics

India gave the world:
  - Zero (0)
  - Ayurveda
  - Yoga
  with my name is gagan pandey i am creating this portfolio website for desining and testing  a large amount of data
"""

    info_label = tk.Label(
        welcome_frame,
        text=info_text,
        font=("Arial", 12),
        bg="#f4e7d3",
        justify="left"
    )
    info_label.pack(padx=20)

    logout_btn = tk.Button(
        welcome_frame,
        text="Logout",
        font=("Arial", 12, "bold"),
        bg="#8b0000",
        fg="white",
        command=logout
    )
    logout_btn.pack(pady=20)

    welcome_frame.pack(fill="both", expand=True)

# -------- Login Frame --------
login_frame = tk.Frame(root, bg="#f4e7d3")

title_label = tk.Label(
    login_frame,
    text="Login - Ancient India Portal",
    font=("Arial", 18, "bold"),
    bg="#f4e7d3",
    fg="#5b3a29"
)
title_label.pack(pady=20)

tk.Label(login_frame, text="Username", font=("Arial", 12), bg="#f4e7d3").pack()
username_entry = tk.Entry(login_frame, font=("Arial", 12))
username_entry.pack(pady=5)

tk.Label(login_frame, text="Password", font=("Arial", 12), bg="#f4e7d3").pack()
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

login_btn = tk.Button(
    login_frame,
    text="Login",
    font=("Arial", 12, "bold"),
    bg="#5b3a29",
    fg="white",
    command=login
)
login_btn.pack(pady=20)

login_frame.pack(pady=100)

root.mainloop()