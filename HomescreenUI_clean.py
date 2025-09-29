# Moonveil: Sleep Habit App (Tkinter GUI)
import tkinter as tk
from tkinter import messagebox
import math

# Store sleep times
declare_times = {"wake": "", "sleep": ""}

def open_settings():
    messagebox.showinfo("Settings", "This would open the app settings.")

def open_profile():
    messagebox.showinfo("Profile", "This would show the user profile.")

def open_soundscapes():
    messagebox.showinfo("Soundscapes", "This would open the soundscapes.")

def open_schedule():
    messagebox.showinfo("Schedule", "This would open the schedule.")

def open_reminders():
    messagebox.showinfo("Reminders", "This would open the reminders.")

def block_apps():
    messagebox.showinfo("App Blocking", f"Apps will be blocked from {declare_times['sleep']} to {declare_times['wake']}.")


def open_clock_screen(container, home_screen):
    clock_screen = tk.Frame(container)
    clock_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    clock_screen.lift()

    def go_back():
        clock_screen.destroy()
        home_screen.lift()
    back_btn = tk.Button(clock_screen, text="←", bg="#df43c8", font=("Arial", 16), command=go_back)
    back_btn.place(x=10, y=10, width=90, height=50)

    fwd_btn = tk.Button(clock_screen, text="→", font=("Arial", 16), state="disabled")
    fwd_btn.place(x=500, y=10, width=90, height=50)

    canvas = tk.Canvas(clock_screen, width=600, height=500, bg="white", highlightthickness=0)
    canvas.place(x=0, y=70)
    canvas.create_oval(50, 20, 550, 520, width=2)
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = 300 + 220 * math.sin(angle)
        y1 = 270 - 220 * math.cos(angle)
        x2 = 300 + 250 * math.sin(angle)
        y2 = 270 - 250 * math.cos(angle)
        canvas.create_line(x1, y1, x2, y2, width=3)
    canvas.create_line(300, 270, 370, 170, width=10, fill="black", capstyle=tk.ROUND)
    canvas.create_line(300, 270, 500, 270, width=6, fill="black", capstyle=tk.ROUND)
    canvas.create_oval(285, 255, 315, 285, fill="black", outline="black")

    wake_frame = tk.Frame(clock_screen, highlightbackground="black", highlightthickness=2)
    wake_frame.place(x=60, y=540, width=480, height=60)
    wake_entry = tk.Entry(wake_frame, font=("Arial", 24), width=6, justify="center", bd=0)
    wake_entry.place(x=10, y=10, width=180, height=40)
    wake_label = tk.Label(wake_frame, text="Wake Up", font=("Arial", 20), bg="white")
    wake_label.place(x=250, y=10)

    sleep_frame = tk.Frame(clock_screen, highlightbackground="black", highlightthickness=2)
    sleep_frame.place(x=60, y=610, width=480, height=60)
    sleep_entry = tk.Entry(sleep_frame, font=("Arial", 24), width=6, justify="center", bd=0)
    sleep_entry.place(x=10, y=10, width=180, height=40)
    sleep_label = tk.Label(sleep_frame, text="Fall Asleep", font=("Arial", 20), bg="white")
    sleep_label.place(x=250, y=10)

    def valid_time(t):
        import re
        return re.match(r"^([01]?\d|2[0-3]):[0-5]\d$", t)

    def save_times():
        wake = wake_entry.get().strip()
        sleep = sleep_entry.get().strip()
        if not valid_time(wake) or not valid_time(sleep):
            messagebox.showerror("Invalid Time", "Please enter times in HH:MM format (24-hour). Example: 22:30")
            return
        declare_times["wake"] = wake
        declare_times["sleep"] = sleep
        messagebox.showinfo("App Blocking", f"Apps will be blocked from {sleep} to {wake}.")

    save_btn = tk.Button(clock_screen, text="Block Apps During This Time", font=("Arial", 16), command=save_times)
    save_btn.place(x=180, y=690, width=240, height=50)


def main():
    root = tk.Tk()
    root.title("Moonveil Home Screen")
    root.geometry("600x700")
    root.resizable(False, False)

    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    home_screen = tk.Frame(container)
    home_screen.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn_settings = tk.Button(home_screen, text="⚙️", command=open_settings)
    btn_settings.place(x=10, y=10, width=50, height=50)

    btn_profile = tk.Button(home_screen, text="○", command=open_profile)
    btn_profile.place(x=540, y=10, width=50, height=50)

    btn_clock = tk.Button(home_screen, text="Clock", font=("Arial", 16),
                          command=lambda: open_clock_screen(container, home_screen))
    btn_clock.place(x=90, y=150, width=180, height=180)

    btn_sound = tk.Button(home_screen, text="Soundscapes", font=("Arial", 16), command=open_soundscapes)
    btn_sound.place(x=330, y=150, width=180, height=180)

    btn_schedule = tk.Button(home_screen, text="Schedule", font=("Arial", 16), command=open_schedule)
    btn_schedule.place(x=90, y=380, width=180, height=180)
    btn_reminders = tk.Button(home_screen, text="Reminders", font=("Arial", 16), command=open_reminders)
    btn_reminders.place(x=330, y=380, width=180, height=180)

    tk.Label(home_screen, text='Home screen').pack()
    home_screen.lift()
    root.mainloop()

if __name__ == "__main__":
    main()
