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

def open_soundscapes(container, home_screen):
    sound_screen = tk.Frame(container)
    sound_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    sound_screen.lift()

    def go_back():
        sound_screen.destroy()
        home_screen.lift()

    back_btn = tk.Button(sound_screen, text="←", font=("Arial", 20), command=go_back)
    back_btn.place(x=10, y=10, width=90, height=50)
    fwd_btn = tk.Button(sound_screen, text="→", font=("Arial", 20), state="disabled")
    fwd_btn.place(x=500, y=10, width=90, height=50)

    # Draw 8 soundscape rows as in the wireframe
    for i in range(8):
        y = 80 + i * 80
        row = tk.Frame(sound_screen, highlightbackground="black", highlightthickness=2)
        row.place(x=40, y=y, width=520, height=70)

        # Left square (icon placeholder)
        icon = tk.Canvas(row, width=50, height=50, highlightthickness=1, highlightbackground="black")
        icon.place(x=8, y=7)

        # Horizontal line (stationary)
        line_canvas = tk.Canvas(row, width=200, height=10, highlightthickness=0,)
        line_canvas.place(x=70, y=30)
        line_canvas.create_line(0, 5, 200, 5, width=3)

        # Play/pause button (stationary, not overlapping)
        play_canvas = tk.Canvas(row, width=50, height=25, highlightthickness=0)
        play_canvas.place(x=150, y=38)
        # Play triangle (left)
        play_canvas.create_polygon(5, 7, 25, 15, 5, 23, fill="black")
        # Pause bars (right, spaced apart)
        play_canvas.create_rectangle(32, 7, 37, 23, fill="black")
        play_canvas.create_rectangle(40, 7, 45, 23, fill="black")

        # Two smaller circles on the right, vertically aligned
        right1 = tk.Canvas(row, width=24, height=24, highlightthickness=0)
        right1.place(x=470, y=10)
        right1.create_oval(2, 2, 22, 22, width=2)
        # Dotted arrow pointing down
        # Dots
        right1.create_oval(11, 6, 13, 8, fill="white")
        right1.create_oval(11, 10, 13, 12, fill="white")
        right1.create_oval(11, 14, 13, 16, fill="white")
        # Arrow head
        right1.create_line(9, 15, 12, 20, fill="black", width=1)
        right1.create_line(15, 15, 12, 20, fill="black", width=1)

        right2 = tk.Canvas(row, width=24, height=24, highlightthickness=0)
        right2.place(x=470, y=38)
        right2.create_oval(2, 2, 22, 22, width=2)
        #right2.create_arc(6, 10, 18, 20, start=0, extent=270, style=tk.ARC, width=2)
        #right2.create_line(16, 16, 20, 12, width=2)

def open_schedule(container, home_screen):
    schedule_screen = tk.Frame(container)
    schedule_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    schedule_screen.lift()

    def go_back():
        schedule_screen.destroy()
        home_screen.lift()

    back_btn = tk.Button(schedule_screen, text="←", font=("Arial", 20), command=go_back)
    back_btn.place(x=10, y=10, width=90, height=50)
    fwd_btn = tk.Button(schedule_screen, text="→", font=("Arial", 20), state="disabled")
    fwd_btn.place(x=500, y=10, width=90, height=50)

    # Draw 10 schedule rows as in the wireframe (with lines and dots)
    for i in range(10):
        y = 80 + i * 70
        row = tk.Frame(schedule_screen, highlightbackground="black", highlightthickness=2)
        row.place(x=40, y=y, width=520, height=60)

        # Left: label with lines and dots (time placeholder)
        label = tk.Label(row, text="\n_ _ : _ _", font=("Courier", 16), justify="left")
        label.place(x=10, y=5)

        # Right: main square (checkbox placeholder)
        box = tk.Canvas(row, width=30, height=30, highlightthickness=1, highlightbackground="black")
        box.place(x=470, y=10)
        #box.create_rectangle(2, 2, 28, 28, width=2)

        # Small box in the right corner of the big box
        #small_box = tk.Canvas(row, width=16, height=16,) #highlightthickness=1, #highlightbackground="white")
        #small_box.place(x=500, y=10)
        #small_box.create_rectangle(2, 2, 14, 14, width=2)

def open_reminders(container, home_screen):
    reminders_screen = tk.Frame(container)
    reminders_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    reminders_screen.lift()

    def go_back():
        reminders_screen.destroy()
        home_screen.lift()

    back_btn = tk.Button(reminders_screen, text="←", font=("Arial", 20), command=go_back)
    back_btn.place(x=10, y=10, width=90, height=50)
    fwd_btn = tk.Button(reminders_screen, text="→", font=("Arial", 20), state="disabled")
    fwd_btn.place(x=500, y=10, width=90, height=50)

    # Draw 4 speech bubble reminders as in the wireframe
    for i in range(4):
        y = 80 + i * 150
        canvas = tk.Canvas(reminders_screen, width=520, height=120, bg="white", highlightthickness=2, highlightbackground="black")
        canvas.place(x=40, y=y)
        # Draw rounded rectangle (bubble)
        canvas.create_oval(10, 10, 50, 50, width=2)
        canvas.create_oval(470, 10, 510, 50, width=2)
        canvas.create_rectangle(30, 10, 490, 110, width=2)
        canvas.create_arc(10, 10, 50, 50, start=90, extent=180, style=tk.ARC, width=2)
        canvas.create_arc(470, 10, 510, 50, start=270, extent=180, style=tk.ARC, width=2)
        # Draw tail (triangle)
        canvas.create_polygon(30, 90, 10, 110, 50, 110, fill="white", outline="black", width=2)
        # Time label (dots and dashes)
        canvas.create_text(470, 100, text=". . :\n_ _ - _ _", font=("Courier", 12), anchor="se")

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

    btn_sound = tk.Button(home_screen, text="Soundscapes", font=("Arial", 16), command=lambda: open_soundscapes(container, home_screen))
    btn_sound.place(x=330, y=150, width=180, height=180)

    btn_schedule = tk.Button(home_screen, text="Schedule", font=("Arial", 16), command=lambda: open_schedule(container, home_screen))
    btn_schedule.place(x=90, y=380, width=180, height=180)
    btn_reminders = tk.Button(home_screen, text="Reminders", font=("Arial", 16), command=lambda: open_reminders(container, home_screen))
    btn_reminders.place(x=330, y=380, width=180, height=180)

    tk.Label(home_screen, text='Home screen').pack()
    home_screen.lift()
    root.mainloop()

if __name__ == "__main__":
    main()
