# Moonveil: Sleep Habit App (Tkinter GUI)
# This version uses Tkinter to create a simple graphical home screen.
# Each button opens a pop-up with the same info as the text version.

import tkinter as tk
from tkinter import messagebox

def show_user_info():
    messagebox.showinfo("User Information", "Name: [Your Name Here]\nSleep Goal: 8 hours/night\nNotifications: ON")

def open_settings():
    messagebox.showinfo("Settings", "1. Change sleep goal\n2. Toggle notifications\n3. Back to Home")

def play_soundscapes():
    messagebox.showinfo("Soundscapes", "Choose a sound to play:\n1. Rain\n2. Ocean\n3. White Noise")

def view_reminders():
    messagebox.showinfo("Reminders", "1. Avoid caffeine after 3 PM\n2. Wind down by 9:30 PM\n3. Put phone away by 10 PM")

def show_clock():
    messagebox.showinfo("Clock", "Current time: [Add real time later]\nBedtime countdown: [Add timer later]")

def view_schedule():
    messagebox.showinfo("Schedule", "App blocking starts at: 10:00 PM\nWake-up time: 7:00 AM")

def main():
    root = tk.Tk()
    root.title("Moonveil: Sleep Habit App")
    root.geometry("400x500")
    root.resizable(False, False)

    # Top row (small buttons)
    btn_settings = tk.Button(root, text="⚙️", width=4, height=2, command=open_settings)
    btn_settings.place(x=10, y=10)
    btn_user = tk.Button(root, text="👤", width=4, height=2, command=show_user_info)
    btn_user.place(x=340, y=10)

    # Big grid buttons
    btn_clock = tk.Button(root, text="Clock", width=16, height=6, command=show_clock)
    btn_clock.place(x=30, y=80)
    btn_sound = tk.Button(root, text="Soundscapes", width=16, height=6, command=play_soundscapes)
    btn_sound.place(x=210, y=80)
    btn_schedule = tk.Button(root, text="Schedule", width=16, height=6, command=view_schedule)
    btn_schedule.place(x=30, y=250)
    btn_reminders = tk.Button(root, text="Reminders", width=16, height=6, command=view_reminders)
    btn_reminders.place(x=210, y=250)

    # Exit button
    btn_exit = tk.Button(root, text="Exit", width=10, command=root.destroy)
    btn_exit.place(x=160, y=430)

    root.mainloop()

if __name__ == "__main__":
    main()
