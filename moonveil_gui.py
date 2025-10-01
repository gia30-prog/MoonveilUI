# Moonveil: Sleep Habit App (Tkinter GUI)
# This version uses Tkinter to create a simple graphical home screen.
# Each button opens a pop-up with the same info as the text version.


import tkinter as tk
from tkinter import messagebox

from HomescreenUI import open_schedule

# Global sleep_times dictionary for storing wake/sleep times
sleep_times = {"wake": "", "sleep": ""}

def show_user_info():
    messagebox.showinfo("User Information", "Name: [Your Name Here]\nSleep Goal: 8 hours/night\nNotifications: ON")

def open_settings():
    messagebox.showinfo("Settings", "1. Change sleep goal\n2. Toggle notifications\n3. Back to Home")

def play_soundscapes():
    messagebox.showinfo("Soundscapes", "Choose a sound to play:\n1. Rain\n2. Ocean\n3. White Noise")

def view_reminders():
    messagebox.showinfo("Reminders", "1. Avoid caffeine after 3 PM\n2. Wind down by 9:30 PM\n3. Put phone away by 10 PM")

#commented out for now, as we have a dedicated clock screen
def show_clock():
    messagebox.showinfo("Clock", "Current time: [Add real time later]\nBedtime countdown: [Add timer later]")
def open_clock_screen(root, home_screen):
    pass
    import math
    # Hide home screen
    home_screen.pack_forget()
    clock_screen = tk.Frame(root)
    clock_screen.pack(fill="both", expand=True)

    # Back button (top left)
    back_btn = tk.Button(clock_screen, text="←", bg="#efb6e6", font=("Arial", 16), command=lambda: [clock_screen.pack_forget(), home_screen.pack(fill='both', expand=True)])
    back_btn.place(x=10, y=10, width=90, height=50)

    # Forward button (top right, optional, not functional)
    fwd_btn = tk.Button(clock_screen, text="→", font=("Arial", 16), state="disabled")
    fwd_btn.place(x=500, y=10, width=90, height=50)

    # Draw analog clock (static, as in image)
    canvas = tk.Canvas(clock_screen, width=600, height=500, bg="white", highlightthickness=0)
    canvas.place(x=0, y=70)
    # Draw outer circle
    canvas.create_oval(50, 20, 550, 520, width=2)
    # Draw hour marks
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = 300 + 220 * math.sin(angle)
        y1 = 270 - 220 * math.cos(angle)
        x2 = 300 + 250 * math.sin(angle)
        y2 = 270 - 250 * math.cos(angle)
        canvas.create_line(x1, y1, x2, y2, width=3)
    # Draw hour hand (static, 2 o'clock)
    canvas.create_line(300, 270, 370, 170, width=10, fill="black", capstyle=tk.ROUND)
    # Draw minute hand (static, 3 o'clock)
    canvas.create_line(300, 270, 500, 270, width=6, fill="black", capstyle=tk.ROUND)
    # Draw center dot
    canvas.create_oval(285, 255, 315, 285, fill="black", outline="black")

    # Wake Up input
    wake_frame = tk.Frame(clock_screen, highlightbackground="black", highlightthickness=2)
    wake_frame.place(x=60, y=540, width=480, height=60)
    wake_entry = tk.Entry(wake_frame, font=("Arial", 24), width=6, justify="center", bd=0)
    wake_entry.place(x=10, y=10, width=180, height=40)
    wake_label = tk.Label(wake_frame, text="Wake Up", font=("Arial", 20), bg="white")
    wake_label.place(x=250, y=10)

    # Fall Asleep input
    sleep_frame = tk.Frame(clock_screen, highlightbackground="black", highlightthickness=2)
    sleep_frame.place(x=60, y=610, width=480, height=60)
    sleep_entry = tk.Entry(sleep_frame, font=("Arial", 24), width=6, justify="center", bd=0)
    sleep_entry.place(x=10, y=10, width=180, height=40)
    sleep_label = tk.Label(sleep_frame, text="Fall Asleep", font=("Arial", 20), bg="white")
    sleep_label.place(x=250, y=10)

    # Helper: validate time format (HH:MM, 24h)
    def valid_time(t):
        import re
        return re.match(r"^([01]?\d|2[0-3]):[0-5]\d$", t)

    # Save and block apps (placeholder)
    def save_times():
        wake = wake_entry.get().strip()
        sleep = sleep_entry.get().strip()
        if not valid_time(wake) or not valid_time(sleep):
            messagebox.showerror("Invalid Time", "Please enter times in HH:MM format (24-hour). Example: 22:30")
            return
        sleep_times["wake"] = wake
        sleep_times["sleep"] = sleep
        # Placeholder for app blocking logic
        messagebox.showinfo("App Blocking", f"Apps will be blocked from {sleep} to {wake}.")
        # Here you would add real app blocking code for your OS

    save_btn = tk.Button(clock_screen, text="Block Apps During This Time", font=("Arial", 16), command=save_times)
    save_btn.place(x=180, y=690, width=240, height=50)

def main():
    root = tk.Tk()
    root.title("Moonveil Home Screen")
    root.geometry("600x700")
    root.resizable(False, False)

    home_screen = tk.Frame(root)
    home_screen.pack(fill="both", expand=True)

    # Top small left: Settings
    btn_settings = tk.Button(home_screen, text="⚙️", command=open_settings)
    btn_settings.place(x=10, y=10, width=50, height=50)

    # Top small right: Profile
    btn_profile = tk.Button(home_screen, text="○", command=show_user_info)
    btn_profile.place(x=540, y=10, width=50, height=50)

    # Big grid (2x2)
    btn_clock = tk.Button(home_screen, text="Clock", font=("Arial", 16),
                          command=lambda: open_clock_screen(root, home_screen))
    btn_clock.place(x=90, y=150, width=180, height=180)

    btn_sound = tk.Button(home_screen, text="Soundscapes", font=("Arial", 16), command=play_soundscapes)
    btn_sound.place(x=330, y=150, width=180, height=180)

    btn_schedule = tk.Button(home_screen, text="Schedule", font=("Arial", 16), command=open_schedule)
    btn_schedule.place(x=90, y=380, width=180, height=180)

    btn_reminders = tk.Button(home_screen, text="Reminders", font=("Arial", 16), command=view_reminders)
    btn_reminders.place(x=330, y=380, width=180, height=180)

    root.mainloop()

if __name__ == "__main__":
    main()

def view_schedule():
    messagebox.showinfo("Schedule", "App blocking starts at: 10:00 PM\nWake-up time: 7:00 AM")