# Moonveil: Sleep Habit App (Tkinter GUI)
import tkinter as tk
from tkinter import messagebox
import math

# Store sleep times
declare_times = {"wake": "", "sleep": ""}

def open_settings():
    messagebox.showinfo("Settings", "This would open the app settings.")

def open_profile():
    # This function is now unused; see open_profile_screen for the real screen.
    pass

def open_profile_screen(container, home_screen):
    profile_screen = tk.Frame(container)
    profile_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    profile_screen.lift()

    def go_back():
        profile_screen.destroy()
        home_screen.lift()

    # Back button (top left)
    back_btn = tk.Button(profile_screen, text="←", font=("Arial", 20), command=go_back)
    back_btn.place(x=10, y=10, width=110, height=50)


    # Slightly smaller circle in the center
    circle_diam = 320
    # Add padding to ensure the oval is not clipped by the canvas border
    pad = 8
    canvas = tk.Canvas(profile_screen, width=circle_diam+2*pad, height=circle_diam+2*pad, highlightthickness=0)
    canvas.place(x=(600-circle_diam)//2 - pad, y=90 - pad)
    canvas.create_oval(pad, pad, circle_diam+pad, circle_diam+pad, width=2)

    # Bottom navigation bar with three buttons
    nav_y = 480
    nav_w = 600
    nav_h = 60
    nav_btn_w = nav_w // 3
    nav_frame = tk.Frame(profile_screen, highlightbackground="black", highlightthickness=2)
    nav_frame.place(x=0, y=nav_y, width=nav_w, height=nav_h)

    # Area to fill with soundscapes/habits/graph when a nav button is clicked (now below nav bar)
    soundscapes_area_height = 420
    soundscapes_area = tk.Frame(profile_screen, width=520, height=soundscapes_area_height)
    soundscapes_area.place(x=40, y=nav_y+nav_h+10, width=520, height=soundscapes_area_height)


    def show_favorite_sounds():
        # Clear area first
        for widget in soundscapes_area.winfo_children():
            widget.destroy()
        # Draw 5 soundscape rows as in the wireframe
        for i in range(5):
            y = i * 80
            row = tk.Frame(soundscapes_area, highlightbackground="black", highlightthickness=2)
            row.place(x=0, y=y, width=520, height=70)
            # Left square (icon placeholder)
            icon = tk.Canvas(row, width=50, height=50, highlightthickness=1, highlightbackground="black")
            icon.place(x=8, y=7)
            # Horizontal line (stationary)
            line_canvas = tk.Canvas(row, width=200, height=10, highlightthickness=0)
            line_canvas.place(x=70, y=30)
            line_canvas.create_line(0, 5, 200, 5, width=3)
            # Play/pause button (stationary, not overlapping)
            play_canvas = tk.Canvas(row, width=50, height=25, highlightthickness=0)
            play_canvas.place(x=150, y=38)
            play_canvas.create_polygon(5, 7, 25, 15, 5, 23, fill="black")
            play_canvas.create_rectangle(32, 7, 37, 23, fill="black")
            play_canvas.create_rectangle(40, 7, 45, 23, fill="black")
            # Two smaller circles on the right, vertically aligned
            right1 = tk.Canvas(row, width=24, height=24, highlightthickness=0)
            right1.place(x=470, y=10)
            right1.create_oval(2, 2, 22, 22, width=2)
            right1.create_oval(11, 6, 13, 8, fill="white")
            right1.create_oval(11, 10, 13, 12, fill="white")
            right1.create_oval(11, 14, 13, 16, fill="white")
            right1.create_line(9, 15, 12, 20, fill="black", width=1)
            right1.create_line(15, 15, 12, 20, fill="black", width=1)
            right2 = tk.Canvas(row, width=24, height=24, highlightthickness=0)
            right2.place(x=470, y=38)
            right2.create_oval(2, 2, 22, 22, width=2)

    def show_sleep_tracker():
        # Clear area first
        for widget in soundscapes_area.winfo_children():
            widget.destroy()
        # Example sleep data (hours per day)
        sleep_data = [7, 6, 8, 5, 7.5, 6.5, 8]
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        max_sleep = 10
        width = 520
        height = 220
        margin = 40
        bar_w = 40
        gap = (width - 2*margin - bar_w*len(sleep_data)) // (len(sleep_data)-1)
        graph = tk.Canvas(soundscapes_area, width=width, height=height, bg="white", highlightthickness=0)
        graph.place(x=0, y=0)
        # Y axis
        graph.create_line(margin, margin, margin, height-margin, width=2)
        # X axis
        graph.create_line(margin, height-margin, width-margin, height-margin, width=2)
        # Bars
        for i, hours in enumerate(sleep_data):
            x0 = margin + i*(bar_w+gap)
            x1 = x0 + bar_w
            y1 = height-margin
            y0 = y1 - (hours/max_sleep)*(height-2*margin)
            graph.create_rectangle(x0, y0, x1, y1, fill="#7ec8e3", outline="#333", width=2)
            graph.create_text((x0+x1)//2, y1+15, text=days[i], font=("Arial", 12))
            graph.create_text((x0+x1)//2, y0-10, text=f"{hours}", font=("Arial", 10))
        # Y axis labels
        for h in range(0, max_sleep+1, 2):
            y = height-margin - (h/max_sleep)*(height-2*margin)
            graph.create_text(margin-15, y, text=str(h), font=("Arial", 10))

    def show_habits():
        # Clear area first
        for widget in soundscapes_area.winfo_children():
            widget.destroy()
        # Example list of habits
        habits = [
            "Go to bed before 11pm",
            "No screens 30 min before bed",
            "Read for 10 minutes",
            "Meditate before sleep",
            "Wake up at the same time"
        ]
        habits_label = tk.Label(soundscapes_area, text="Your Habits to Implement:", font=("Arial", 16, "bold"))
        habits_label.place(x=20, y=10)
        for i, habit in enumerate(habits):
            habit_label = tk.Label(soundscapes_area, text="• " + habit, font=("Arial", 14), anchor="w", justify="left")
            habit_label.place(x=40, y=50 + i*36)

    btn1 = tk.Button(nav_frame, text="Favorite sounds", font=("Arial", 16), command=show_favorite_sounds)
    btn1.place(x=0, y=0, width=nav_btn_w, height=nav_h)
    btn2 = tk.Button(nav_frame, text="Sleep Tracker", font=("Arial", 16), command=show_sleep_tracker)
    btn2.place(x=nav_btn_w, y=0, width=nav_btn_w, height=nav_h)
    btn3 = tk.Button(nav_frame, text="Habits", font=("Arial", 16), command=show_habits)
    btn3.place(x=2*nav_btn_w, y=0, width=nav_btn_w, height=nav_h)

def open_soundscapes(container, home_screen):
    sound_screen = tk.Frame(container)
    sound_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    sound_screen.lift()

    def go_back():
        sound_screen.destroy()
        home_screen.lift()

    back_btn = tk.Button(sound_screen, text="←", font=("Arial", 20), command=go_back)
    back_btn.place(x=10, y=10, width=90, height=50)

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

    # Draw 10 schedule rows as in the wireframe (with lines and dots)
    for i in range(10):
        y = 80 + i * 70
        row = tk.Frame(schedule_screen, highlightbackground="black", highlightthickness=2)
        row.place(x=40, y=y, width=520, height=60)

        # Left: label with lines and dots (time placeholder)
        label = tk.Label(row, text="\n_ _:_ _", font=("Courier", 16), justify="left")
        label.place(x=10, y=5)

        # Right: main square (checkbox placeholder)
        box = tk.Canvas(row, width=30, height=30, highlightthickness=1, highlightbackground="black")
        box.place(x=470, y=12)
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

    # Draw 4 speech bubble reminders as text message bubbles
    for i in range(4):
        y = 80 + i * 120
        canvas = tk.Canvas(reminders_screen, width=520, height=100, highlightthickness=0)
        canvas.place(x=40, y=y)
        # Draw rounded rectangle (bubble) with filled corners
        r = 25  # corner radius
        # Main body
        #canvas.create_rectangle(30+r, 10, 490-r, 80, width=0, fill="#f8f8f8", outline="")
        #canvas.create_rectangle(30, 10+r, 490, 80-r, width=0, fill="#f8f8f8", outline="")
        # Four corners
        #canvas.create_arc(30, 10, 30+2*r, 10+2*r, start=90, extent=90, style=tk.PIESLICE, width=0, fill="#f8f8f8")
        #canvas.create_arc(490-2*r, 10, 490, 10+2*r, start=0, extent=90, style=tk.PIESLICE, width=0, fill="#f8f8f8")
        #canvas.create_arc(30, 80-2*r, 30+2*r, 80, start=180, extent=90, style=tk.PIESLICE, width=0, fill="#f8f8f8")
        #canvas.create_arc(490-2*r, 80-2*r, 490, 80, start=270, extent=90, style=tk.PIESLICE, width=0, fill="#f8f8f8")
        # Outline for rounded rectangle
        canvas.create_arc(30, 10, 30+2*r, 10+2*r, start=90, extent=90, style=tk.ARC, width=2, outline="#333")
        canvas.create_arc(490-2*r, 10, 490, 10+2*r, start=0, extent=90, style=tk.ARC, width=2, outline="#333")
        canvas.create_arc(30, 80-2*r, 30+2*r, 80, start=180, extent=90, style=tk.ARC, width=2, outline="#333")
        canvas.create_arc(490-2*r, 80-2*r, 490, 80, start=270, extent=90, style=tk.ARC, width=2, outline="#333")
        canvas.create_line(30+r, 10, 490-r, 10, fill="#333", width=2)
        canvas.create_line(30+r, 80, 490-r, 80, fill="#333", width=2)
        canvas.create_line(30, 10+r, 30, 80-r, fill="#333", width=2)
        canvas.create_line(490, 10+r, 490, 80-r, fill="#333", width=2)
        # Draw tail (triangle)
        canvas.create_polygon(60, 80, 80, 100, 100, 80, fill="#f8f8f8", outline="#333", width=2)
        # Time label (dots and dashes)
        canvas.create_text(470, 95, text="_ _:_ _", font=("Courier", 14), anchor="se")

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


    # Slightly bigger clock
    canvas = tk.Canvas(clock_screen, width=420, height=420, highlightthickness=0)
    canvas.place(x=90, y=60)
    canvas.create_oval(30, 30, 390, 390, width=2)
    center_x, center_y = 210, 210
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = center_x + 150 * math.sin(angle)
        y1 = center_y - 150 * math.cos(angle)
        x2 = center_x + 180 * math.sin(angle)
        y2 = center_y - 180 * math.cos(angle)
        canvas.create_line(x1, y1, x2, y2, width=3)
    # Hour hand
    canvas.create_line(center_x, center_y, center_x + 40, center_y - 85, width=4, fill="black", capstyle=tk.ROUND)
    # Minute hand
    canvas.create_line(center_x, center_y, center_x + 130, center_y, width=4, fill="black", capstyle=tk.ROUND)
    # Center dot (smaller)
    canvas.create_oval(center_x-7, center_y-7, center_x+7, center_y+7, fill="black", outline="black")

    wake_frame = tk.Frame(clock_screen, highlightbackground="black", highlightthickness=2)
    wake_frame.place(x=60, y=540, width=480, height=60)
    wake_entry = tk.Entry(wake_frame, font=("Arial", 24), width=6, justify="center", bd=0)
    #wake_entry.place(x=10, y=10, width=180, height=40)
    wake_label = tk.Label(wake_frame, text="Wake Up", font=("Arial", 20))
    wake_label.place(x=355, y=10)
    # Add time placeholder next to Wake Up
    wake_time_placeholder = tk.Label(wake_frame, text="_ _:_ _", font=("Courier", 20),)
    wake_time_placeholder.place(x=70, y=15)

    sleep_frame = tk.Frame(clock_screen, highlightbackground="black", highlightthickness=2)
    sleep_frame.place(x=60, y=610, width=480, height=60)
    sleep_entry = tk.Entry(sleep_frame, font=("Arial", 24), width=6, justify="center", bd=0)
    #sleep_entry.place(x=10, y=10, width=180, height=40)
    sleep_lable_placeholder = tk.Label(sleep_frame, text="_ _:_ _", font=("Courier", 20),)
    sleep_lable_placeholder.place(x=70, y=15)
    sleep_label = tk.Label(sleep_frame, text="Fall Asleep", font=("Arial", 20))
    sleep_label.place(x=350, y=10)

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
    root.geometry("600x800")
    root.resizable(True, True)

    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    home_screen = tk.Frame(container)
    home_screen.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn_settings = tk.Button(home_screen, text="⚙️", command=open_settings)
    btn_settings.place(x=10, y=10, width=50, height=50)

    btn_profile = tk.Button(home_screen, text="○", command=lambda: open_profile_screen(container, home_screen))
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
