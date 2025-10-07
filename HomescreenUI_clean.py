# Moonveil: Sleep Habit App (Tkinter GUI)
import tkinter as tk
from tkinter import messagebox
import math

# Store sleep times
declare_times = {"wake": "", "sleep": ""}

def open_settings(container, home_screen):
    settings_screen = tk.Frame(container, bg="#ffefc5")
    settings_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    settings_screen.lift()

    def go_back():
        settings_screen.destroy()
        home_screen.lift()
        if hasattr(home_screen, 'draw_home_boxes'):
            home_screen.draw_home_boxes()

    # Back button (top left)
    back_btn = tk.Canvas(settings_screen, width=110, height=50, bg="#e0dcaa", highlightthickness=0)
    back_btn.place(x=10, y=10)
    # Draw colored arrow
    back_btn.create_line(35, 25, 75, 25, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(35, 25, 50, 15, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(35, 25, 50, 35, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.bind("<Button-1>", lambda e: go_back())

    # Settings options
    options = [
        ("Edit Profile", "circle"),
        ("Notification Preference", ">"),
        ("Blocked Apps", ">"),
        ("Share App", ">"),
        ("About", ">"),
        ("Language", ">"),
        ("Help", ">"),
        ("LogOut", None)
    ]
    y_start = 90
    box_h = 60
    box_w = 600 - 80
    x_start = 40
    for i, (label, icon) in enumerate(options):
        y = y_start + i * (box_h + 12)
        frame = tk.Frame(settings_screen, highlightbackground="black", highlightthickness=2, bg="white")
        frame.place(x=x_start, y=y, width=box_w, height=box_h)
        if label == "LogOut":
            lbl = tk.Label(frame, text=label, font=("Courier", 18), anchor="w", fg="#b94a48", bg="white")
        else:
            lbl = tk.Label(frame, text=label, font=("Courier", 18), anchor="w", bg="white")
        lbl.place(x=12, y=10, width=box_w-60, height=box_h-20)
        if icon == ">":
            arrow = tk.Canvas(frame, width=40, height=40, highlightthickness=0, bg=frame.cget('bg'))
            arrow.place(x=box_w-50, y=10)
            # Draw a sharp arrowhead where both lines meet at (32,20), color #cd725d
            arrow.create_line(12, 10, 32, 20, width=4, capstyle=tk.ROUND, fill="#cd725d")
            arrow.create_line(12, 30, 32, 20, width=4, capstyle=tk.ROUND, fill="#cd725d")
        elif icon == "circle":
            circ = tk.Canvas(frame, width=40, height=40, highlightthickness=0, bg=frame.cget('bg'))
            circ.place(x=box_w-50, y=10)
            circ.create_oval(10, 10, 30, 30, width=3)

def open_profile():
    # This function is now unused; see open_profile_screen for the real screen.
    pass

def open_profile_screen(container, home_screen):
    profile_screen = tk.Frame(container, bg="#ffefc5")
    profile_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    profile_screen.lift()

    def go_back():
        profile_screen.destroy()
        home_screen.lift()

    # Back button (top left)
    back_btn = tk.Canvas(profile_screen, width=110, height=50, bg="#e0dcaa", highlightthickness=0)
    back_btn.place(x=10, y=10)
    back_btn.create_line(35, 25, 75, 25, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(35, 25, 50, 15, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(35, 25, 50, 35, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.bind("<Button-1>", lambda e: go_back())


    # Slightly smaller circle in the center
    circle_diam = 320
    # Add padding to ensure the oval is not clipped by the canvas border
    pad = 8
    canvas = tk.Canvas(profile_screen, width=circle_diam+2*pad, height=circle_diam+2*pad, highlightthickness=0, bg="#ffefc5")
    canvas.place(x=(600-circle_diam)//2 - pad, y=90 - pad)
    # Fill the whole canvas with #ffefc5
    canvas.create_rectangle(0, 0, circle_diam+2*pad, circle_diam+2*pad, fill="#ffefc5", outline="")
    # Draw a white-filled circle with #ffefc5 outline
    canvas.create_oval(pad, pad, circle_diam+pad, circle_diam+pad, width=2, outline="#ffefc5", fill="white")

    # Bottom navigation bar with three buttons
    nav_y = 480
    nav_w = 600
    nav_h = 60
    nav_btn_w = nav_w // 3
    nav_frame = tk.Frame(profile_screen, highlightbackground="black", highlightthickness=2)
    nav_frame.place(x=0, y=nav_y, width=nav_w, height=nav_h)

    # Area to fill with soundscapes/habits/graph when a nav button is clicked (now below nav bar)
    soundscapes_area_height = 420
    soundscapes_area = tk.Frame(profile_screen, width=520, height=soundscapes_area_height, bg="#ffefc5")
    soundscapes_area.place(x=40, y=nav_y+nav_h+10, width=520, height=soundscapes_area_height)


    def show_favorite_sounds():
        # Clear area first
        for widget in soundscapes_area.winfo_children():
            widget.destroy()
        for i in range(5):
            y = i * 80
            row = tk.Frame(soundscapes_area, highlightbackground="black", highlightthickness=2, bg="#e99d75")
            row.place(x=0, y=y, width=520, height=70)
            # Left square (icon placeholder)
            icon = tk.Canvas(row, width=50, height=50, highlightthickness=1, highlightbackground="black", bg="white")
            icon.place(x=8, y=7)
            # Horizontal line (stationary)
            line_canvas = tk.Canvas(row, width=200, height=10, highlightthickness=0, bg="#e99d75")
            line_canvas.place(x=70, y=30)
            line_canvas.create_line(0, 5, 200, 5, width=3, fill="#f5b928")
            # Play/pause button (stationary, not overlapping)
            play_canvas = tk.Canvas(row, width=50, height=25, highlightthickness=0, bg="#e99d75")
            play_canvas.place(x=150, y=38)
            play_canvas.create_polygon(5, 7, 25, 15, 5, 23, fill="#f5b928")
            play_canvas.create_rectangle(32, 7, 37, 23, fill="#f5b928", outline="")
            play_canvas.create_rectangle(40, 7, 45, 23, fill="#f5b928", outline="")
            # Two smaller circles on the right, vertically aligned
            right1 = tk.Canvas(row, width=24, height=24, highlightthickness=0, bg="#e99d75")
            right1.place(x=470, y=10)
            right1.create_oval(1, 1, 23, 23, width=1, fill="black", outline="black")
            right1.create_oval(10, 5, 14, 9, fill="white")
            right1.create_oval(10, 9, 14, 13, fill="white")
            right1.create_oval(10, 13, 14, 17, fill="white")
            right1.create_line(8, 16, 12, 20, fill="white", width=1)
            right1.create_line(16, 16, 12, 20, fill="white", width=1)
            right2 = tk.Canvas(row, width=24, height=24, highlightthickness=0, bg="#e99d75")
            right2.place(x=470, y=38)
            # Draw a heart shape (always filled #b94a48)
            right2.create_oval(4, 4, 13, 14, fill="#b94a48", outline="")
            right2.create_oval(11, 4, 20, 14, fill="#b94a48", outline="")
            right2.create_polygon(4, 11, 12, 22, 20, 11, fill="#b94a48", outline="")

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
            graph.create_text((x0+x1)//2, y1+15, text=days[i], font=("Courier", 12))
            graph.create_text((x0+x1)//2, y0-10, text=f"{hours}", font=("Courier", 10))
        # Y axis labels
        for h in range(0, max_sleep+1, 2):
            y = height-margin - (h/max_sleep)*(height-2*margin)
            graph.create_text(margin-15, y, text=str(h), font=("Courier", 10))

    def show_habits():
        # Clear area first
        for widget in soundscapes_area.winfo_children():
            widget.destroy()
        soundscapes_area.config(bg="#ffefc5")
        # Example list of habits
        habits = [
            "Go to bed before 11pm",
            "No screens 30 min before bed",
            "Read for 10 minutes",
            "Meditate before sleep",
            "Wake up at the same time"
        ]
        habits_label = tk.Label(soundscapes_area, text="Your Habits to Implement:", font=("Courier", 16, "bold"), bg="#ffefc5")
        habits_label.place(x=20, y=10)
        for i, habit in enumerate(habits):
            habit_label = tk.Label(soundscapes_area, text="• " + habit, font=("Courier", 14), anchor="w", justify="left", bg="#ffefc5")
            habit_label.place(x=40, y=50 + i*36)

    # Clickable colored box for Favorite sounds
    fav_box = tk.Canvas(nav_frame, width=nav_btn_w, height=nav_h, bg="#e99d75", highlightthickness=0)
    fav_box.place(x=0, y=0)
    fav_box.create_rectangle(0, 0, nav_btn_w, nav_h, fill="#e99d75", outline="#cd725d", width=3)
    fav_box.create_text(nav_btn_w//2, nav_h//2, text="Favorite sounds", font=("Courier", 16), fill="black")
    fav_box.bind("<Button-1>", lambda e: show_favorite_sounds())
    sleep_box = tk.Canvas(nav_frame, width=nav_btn_w, height=nav_h, bg="#e0dcaa", highlightthickness=0)
    sleep_box.place(x=nav_btn_w, y=0)
    sleep_box.create_rectangle(0, 0, nav_btn_w, nav_h, fill="#e0dcaa", outline="#cd725d", width=3)
    sleep_box.create_text(nav_btn_w//2, nav_h//2, text="Sleep Tracker", font=("Courier", 16), fill="black")
    sleep_box.bind("<Button-1>", lambda e: show_sleep_tracker())
    habits_box = tk.Canvas(nav_frame, width=nav_btn_w, height=nav_h, bg="#f5b928", highlightthickness=0)
    habits_box.place(x=2*nav_btn_w, y=0)
    habits_box.create_rectangle(0, 0, nav_btn_w, nav_h, fill="#f5b928", outline="#cd725d", width=3)
    habits_box.create_text(nav_btn_w//2, nav_h//2, text="Habits", font=("Courier", 16), fill="black")
    habits_box.bind("<Button-1>", lambda e: show_habits())

def open_soundscapes(container, home_screen):
    sound_screen = tk.Frame(container, bg="#ffefc5")
    sound_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    sound_screen.lift()

    def go_back():
        sound_screen.destroy()
        home_screen.lift()

    back_btn = tk.Canvas(sound_screen, width=90, height=50, bg="#e0dcaa", highlightthickness=0)
    back_btn.place(x=10, y=10)
    back_btn.create_line(30, 25, 70, 25, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(30, 25, 45, 15, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(30, 25, 45, 35, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.bind("<Button-1>", lambda e: go_back())

    filled_indices = {0, 3, 7}
    for i in range(8):
        y = 80 + i * 80
        row = tk.Frame(sound_screen, highlightbackground="black", highlightthickness=2, bg="#e99d75")
        row.place(x=40, y=y, width=520, height=70)

        # Left square (icon placeholder)
        icon = tk.Canvas(row, width=50, height=50, highlightthickness=1, highlightbackground="black", bg="white")
        icon.place(x=8, y=7)

        # Horizontal line (stationary)
        line_canvas = tk.Canvas(row, width=200, height=10, highlightthickness=0, bg="#e99d75")
        line_canvas.place(x=70, y=30)
        line_canvas.create_line(0, 5, 200, 5, width=3, fill="#f5b928")

        # Play/pause button (stationary, not overlapping)
        play_canvas = tk.Canvas(row, width=50, height=25, highlightthickness=0, bg="#e99d75")
        play_canvas.place(x=150, y=38)
        # Play triangle (left)
        play_canvas.create_polygon(5, 7, 25, 15, 5, 23, fill="#f5b928")
        # Pause bars (right, spaced apart, no outline)
        play_canvas.create_rectangle(32, 7, 37, 23, fill="#f5b928", outline="")
        play_canvas.create_rectangle(40, 7, 45, 23, fill="#f5b928", outline="")

        # Two smaller circles on the right, vertically aligned
        right1 = tk.Canvas(row, width=24, height=24, highlightthickness=0, bg="#e99d75")
        right1.place(x=470, y=10)
        right1.create_oval(1, 1, 23, 23, width=1, fill="black", outline="black")
        # Dotted arrow pointing down
        # Dots
        right1.create_oval(10, 5, 14, 9, fill="white")
        right1.create_oval(10, 9, 14, 13, fill="white")
        right1.create_oval(10, 13, 14, 17, fill="white")
        # Arrow head
        right1.create_line(8, 16, 12, 20, fill="white", width=1)
        right1.create_line(16, 16, 12, 20, fill="white", width=1)

        right2 = tk.Canvas(row, width=24, height=24, highlightthickness=0, bg="#e99d75")
        right2.place(x=470, y=38)
        # Draw a heart shape
        if i in filled_indices:
            # Filled heart
            right2.create_oval(4, 4, 13, 14, fill="#b94a48", outline="")
            right2.create_oval(11, 4, 20, 14, fill="#b94a48", outline="")
            right2.create_polygon(4, 11, 12, 22, 20, 11, fill="#b94a48", outline="")
        else:
            # Unfilled heart (filled white with colored outline)
            right2.create_oval(4, 4, 13, 14, fill="white", outline="#fff", width=2)
            right2.create_oval(11, 4, 20, 14, fill="white", outline="#fff", width=2)
            right2.create_polygon(4, 11, 12, 22, 20, 11, fill="white", outline="#fff", width=2)
        #right2.create_arc(6, 10, 18, 20, start=0, extent=270, style=tk.ARC, width=2)
        #right2.create_line(16, 16, 20, 12, width=2)

def open_schedule(container, home_screen):
    schedule_screen = tk.Frame(container, bg="#ffefc5")
    schedule_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    schedule_screen.lift()

    def go_back():
        schedule_screen.destroy()
        home_screen.lift()

    back_btn = tk.Canvas(schedule_screen, width=90, height=50, bg="#e0dcaa", highlightthickness=0)
    back_btn.place(x=10, y=10)
    back_btn.create_line(30, 25, 70, 25, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(30, 25, 45, 15, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(30, 25, 45, 35, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.bind("<Button-1>", lambda e: go_back())

    # Draw 10 schedule rows as in the wireframe (with lines and dots)
    for i in range(10):
        y = 80 + i * 70
        row = tk.Frame(schedule_screen, highlightbackground="black", highlightthickness=2, bg="white")
        row.place(x=40, y=y, width=520, height=60)

        # Left: label with lines and dots (time placeholder)
        if i == 0:
            label = tk.Label(row, text="6:30am", font=("Courier", 30), justify="left", bg="white")
            label.place(x=25, y=9)
        elif i == 1:
            label = tk.Label(row, text="7:00am", font=("Courier", 30), justify="left", bg="white")
            label.place(x=25, y=9)
        elif i == 2:
            label = tk.Label(row, text="7:30am", font=("Courier", 30), justify="left", bg="white")
            label.place(x=25, y=9)
        elif i == 3:
            label = tk.Label(row, text="12:00pm", font=("Courier", 30), justify="left", bg="white")
            label.place(x=10, y=9)
        elif i == 4:
            label = tk.Label(row, text="2:00pm", font=("Courier", 30), justify="left", bg="white")
            label.place(x=25, y=9)
        elif i == 5:
            label = tk.Label(row, text="5:00pm", font=("Courier", 30), justify="left", bg="white")
            label.place(x=25, y=9)
        elif i == 6:
            label = tk.Label(row, text="6:00pm", font=("Courier", 30), justify="left", bg="white")
            label.place(x=25, y=9)
        elif i == 7:
            label = tk.Label(row, text="8:00pm", font=("Courier", 30), justify="left", bg="white")
            label.place(x=25, y=9)
        elif i == 8:
            label = tk.Label(row, text="9:00pm", font=("Courier", 30), justify="left", bg="white")
            label.place(x=25, y=9)
        elif i == 9:
            label = tk.Label(row, text="11:00pm", font=("Courier", 30), justify="left", bg="white")
            label.place(x=10, y=9)

        # Right: main square (checkbox placeholder)
        box = tk.Canvas(row, width=30, height=30, highlightthickness=1, highlightbackground="white", bg="white")
        box.place(x=470, y=12)
        # Draw the rectangle, fill #cd725d for box seven (i==6) and nine (i==8), else white
        if i == 5 or i == 8:
            box.create_rectangle(2, 2, 28, 28, width=2, fill="#cd725d", outline="#cd725d")
        else:
            box.create_rectangle(2, 2, 28, 28, width=2, fill="white", outline="black")

        # Add a separate transparent Text widget for each schedule row
        if i == 0:
            text_box_1 = tk.Text(row, font=("Courier", 23), bg="white", bd=0, height=2, width=40, relief="flat", highlightthickness=0)
            text_box_1.place(x=145, y=16, width=320, height=30)
            text_box_1.insert("1.0", "Wake Up")
            text_box_1.config(state="disabled")
        elif i == 1:
            text_box_2 = tk.Text(row, font=("Courier", 23), bg="white", bd=0, height=2, width=40, relief="flat", highlightthickness=0)
            text_box_2.place(x=145, y=16, width=320, height=30)
            text_box_2.insert("1.0", "Start using electronics")
            text_box_2.config(state="disabled")
        elif i == 2:
            text_box_3 = tk.Text(row, font=("Courier", 23), bg="white", bd=0, height=2, width=40, relief="flat", highlightthickness=0)
            text_box_3.place(x=145, y=16, width=300, height=30)
            text_box_3.insert("1.0", "Breakfast")
            text_box_3.config(state="disabled")
        elif i == 3:
            text_box_4 = tk.Text(row, font=("Courier", 23), bg="white", bd=0, height=2, width=40, relief="flat", highlightthickness=0)
            text_box_4.place(x=145, y=16, width=320, height=30)
            text_box_4.insert("1.0", "Lunch")
            text_box_4.config(state="disabled")
        elif i == 4:
            text_box_5 = tk.Text(row, font=("Courier", 23), bg="white", bd=0, height=2, width=40, relief="flat", highlightthickness=0)
            text_box_5.place(x=145, y=16, width=320, height=30)
            text_box_5.insert("1.0", "Snack")
            text_box_5.config(state="disabled")
        elif i == 5:
            text_box_6 = tk.Text(row, font=("Courier", 23), bg="white", bd=0, height=2, width=40, relief="flat", highlightthickness=0)
            text_box_6.place(x=145, y=16, width=320, height=30)
            text_box_6.insert("1.0", "Last cup of caffeine")
            text_box_6.config(state="disabled")
        elif i == 6:
            text_box_7 = tk.Text(row, font=("Courier", 23), bg="white", bd=0, height=2, width=40, relief="flat", highlightthickness=0)
            text_box_7.place(x=145, y=16, width=320, height=30)
            text_box_7.insert("1.0", "Dinner")
            text_box_7.config(state="disabled")
        elif i == 7:
            text_box_8 = tk.Text(row, font=("Courier", 23), bg="white", bd=0, height=2, width=40, relief="flat", highlightthickness=0)
            text_box_8.place(x=145, y=16, width=320, height=30)
            text_box_8.insert("1.0", "Limit Blue Light")
            text_box_8.config(state="disabled")
        elif i == 8:
            text_box_9 = tk.Text(row, font=("Courier", 23), bg="white", bd=0, height=2, width=40, relief="flat", highlightthickness=0)
            text_box_9.place(x=145, y=16, width=320, height=30)
            text_box_9.insert("1.0", "Stop using electronics")
            text_box_9.config(state="disabled")
        elif i == 9:
            text_box_10 = tk.Text(row, font=("Courier", 23), bg="white", bd=0, height=2, width=40, relief="flat", highlightthickness=0)
            text_box_10.place(x=145, y=16, width=300, height=30)
            text_box_10.insert("1.0", "Go to Sleep")
            text_box_10.config(state="disabled")

        # Add Entry widget for typing in each schedule row
        #entry = tk.Entry(row, font=("Courier", 14), bg="white", bd=0, relief="flat", highlightthickness=0)
        #entry.place(x=120, y=15, width=380, height=30)

        # Small box in the right corner of the big box
        #small_box = tk.Canvas(row, width=16, height=16,) #highlightthickness=1, #highlightbackground="white")
        #small_box.place(x=500, y=10)
        #small_box.create_rectangle(2, 2, 14, 14, width=2)

        # Right: main square (checkbox placeholder)
        #box = tk.Canvas(row, width=30, height=30, highlightthickness=1, highlightbackground="black", bg="white")
        #box.place(x=470, y=12)
        #box.create_rectangle(2, 2, 28, 28, width=2)

def open_reminders(container, home_screen):
    reminders_screen = tk.Frame(container, bg="#ffefc5")
    reminders_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    reminders_screen.lift()

    def go_back():
        reminders_screen.destroy()
        home_screen.lift()

    back_btn = tk.Canvas(reminders_screen, width=90, height=50, bg="#e0dcaa", highlightthickness=0)
    back_btn.place(x=10, y=10)
    back_btn.create_line(30, 25, 70, 25, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(30, 25, 45, 15, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(30, 25, 45, 35, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.bind("<Button-1>", lambda e: go_back())

    # Draw 4 speech bubble reminders as text message bubbles
    for i in range(4):
        y = 80 + i * 120
        canvas = tk.Canvas(reminders_screen, width=520, height=100, highlightthickness=0)
        canvas.place(x=40, y=y)
        # Draw rounded rectangle (bubble) with filled corners
        r = 25  # corner radius
        canvas.create_arc(30, 10, 30+2*r, 10+2*r, start=90, extent=90, style=tk.ARC, width=2, outline="#333")
        canvas.create_arc(490-2*r, 10, 490, 10+2*r, start=0, extent=90, style=tk.ARC, width=2, outline="#333")
        canvas.create_arc(30, 80-2*r, 30+2*r, 80, start=180, extent=90, style=tk.ARC, width=2, outline="#333")
        canvas.create_arc(490-2*r, 80-2*r, 490, 80, start=270, extent=90, style=tk.ARC, width=2, outline="#333")
        canvas.create_line(30+r, 10, 490-r, 10, fill="#333", width=2)
        # Split bottom line for speech bubble tail
        # Left segment: from left arc end to left side of tail
        canvas.create_line(30+r, 80, 70, 80, fill="#333", width=2)
        # Right segment: from right side of tail to right arc end
        canvas.create_line(100, 80, 490-r, 80, fill="#333", width=2)
        canvas.create_line(30, 10+r, 30, 80-r, fill="#333", width=2)
        canvas.create_line(490, 10+r, 490, 80-r, fill="#333", width=2)
        # Draw tail as an arrow with two lines
        canvas.create_line(69, 80, 85, 95, fill="#333", width=2)
        canvas.create_line(101, 80, 85, 95, fill="#333", width=2)
        # Time label (dots and dashes)
        canvas.create_text(470, 95, text="_ _:_ _", font=("Courier", 14), anchor="se")

def block_apps():
    messagebox.showinfo("App Blocking", f"Apps will be blocked from {declare_times['sleep']} to {declare_times['wake']}.")


def open_clock_screen(container, home_screen):
    clock_screen = tk.Frame(container, bg="#ffefc5")
    clock_screen.place(relx=0, rely=0, relwidth=1, relheight=1)
    clock_screen.lift()

    def go_back():
        clock_screen.destroy()
        home_screen.lift()
    back_btn = tk.Canvas(clock_screen, width=90, height=50, bg="#e0dcaa", highlightthickness=0)
    back_btn.place(x=10, y=10)
    back_btn.create_line(30, 25, 70, 25, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(30, 25, 45, 15, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.create_line(30, 25, 45, 35, width=5, fill="#cd725d", capstyle=tk.ROUND)
    back_btn.bind("<Button-1>", lambda e: go_back())


    # Slightly bigger clock
    canvas = tk.Canvas(clock_screen, width=420, height=420, highlightthickness=0, bg="#ffefc5")
    canvas.place(x=90, y=60)
    # Draw only the outline of the clock, not a filled oval
    canvas.create_oval(30, 30, 390, 390, width=2, outline="black", fill="#f8f8f8")
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

    wake_frame = tk.Frame(clock_screen, highlightbackground="black", highlightthickness=2, bg="white")
    wake_frame.place(x=60, y=540, width=480, height=60)
    wake_entry = tk.Entry(wake_frame, font=("Courier", 24), width=6, justify="center", bd=0)
    #wake_entry.place(x=10, y=10, width=180, height=40)
    wake_label = tk.Label(wake_frame, text="Wake Up", font=("Courier", 20), bg="white")
    wake_label.place(x=345, y=13)
    # Add time placeholder next to Wake Up
    wake_time_placeholder = tk.Label(wake_frame, text="6:30am", font=("Courier", 40), bg="white")
    wake_time_placeholder.place(x=70, y=5)

    sleep_frame = tk.Frame(clock_screen, highlightbackground="black", highlightthickness=2, bg="white")
    sleep_frame.place(x=60, y=610, width=480, height=60)
    sleep_entry = tk.Entry(sleep_frame, font=("Courier", 24), width=6, justify="center", bd=0)
    #sleep_entry.place(x=10, y=10, width=180, height=40)
    sleep_lable_placeholder = tk.Label(sleep_frame, text="11:00pm", font=("Courier", 40), bg="white")
    sleep_lable_placeholder.place(x=50, y=5)
    sleep_label = tk.Label(sleep_frame, text="Fall Asleep", font=("Courier", 20), bg="white")
    sleep_label.place(x=320, y=13)

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

    save_btn = tk.Button(clock_screen, text="Block Apps During This Time", font=("Courier", 16), command=save_times)
    save_btn.place(x=180, y=690, width=240, height=50)


def main():
    root = tk.Tk()
    root.title("Moonveil Home Screen")
    root.geometry("600x800")
    root.resizable(True, True)

    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    home_screen = tk.Frame(container, bg="#ffefc5")
    home_screen.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Custom settings button with #e0dcaa background and #cd725d cog
    settings_canvas = tk.Canvas(home_screen, width=50, height=50, bg="#e0dcaa", highlightthickness=0)
    settings_canvas.place(x=10, y=10)
    # Draw cog (simple gear shape)
    center_x, center_y, r = 25, 25, 13
    for angle in range(0, 360, 45):
        x1 = center_x + r * math.cos(math.radians(angle))
        y1 = center_y + r * math.sin(math.radians(angle))
        x2 = center_x + (r+7) * math.cos(math.radians(angle))
        y2 = center_y + (r+7) * math.sin(math.radians(angle))
        settings_canvas.create_line(x1, y1, x2, y2, width=4, fill="#cd725d")
    settings_canvas.create_oval(center_x-r, center_y-r, center_x+r, center_y+r, outline="#cd725d", width=4)
    settings_canvas.create_oval(center_x-5, center_y-5, center_x+5, center_y+5, fill="#cd725d", outline="")
    settings_canvas.bind("<Button-1>", lambda e: open_settings(container, home_screen))

    # Custom profile button with #e0dcaa background
    profile_canvas = tk.Canvas(home_screen, width=50, height=50, bg="#e0dcaa", highlightthickness=0)
    profile_canvas.place(x=540, y=10)
    # Draw user icon (circle)
    profile_canvas.create_oval(10, 10, 40, 40, outline="#cd725d", width=4)
    #profile_canvas.create_oval(20, 20, 30, 30, fill="#cd725d", outline="")
    profile_canvas.bind("<Button-1>", lambda e: open_profile_screen(container, home_screen))

    # Four big buttons with white background and horizontal #e99d75 line
    def add_button_with_line(parent, text, x, y, command):
        frame = tk.Frame(parent, bg="white", highlightbackground="#e99d75", highlightthickness=0)
        frame.place(x=x, y=y, width=180, height=180)
        btn = tk.Button(frame, text=text, font=("Courier", 16), bg="white", relief="flat", command=command)
        btn.place(x=0, y=0, width=180, height=180)
        line = tk.Canvas(frame, width=180, height=40, bg="white", highlightthickness=0)
        line.place(x=0, y=70)
        line_id = line.create_line(0, 20, 180, 20, width=38, fill="#e99d75")
        def on_line_click(event):
            command()
        line.tag_bind(line_id, '<Button-1>', on_line_click)
        # Add Entry (text box) on top of the line
        entry = tk.Entry(frame, font=("Courier", 16), bg="#e99d75", fg="black", bd=0, highlightthickness=0, relief="flat", justify="center")
        entry.place(x=20, y=78, width=140, height=28)
        return btn

    def add_box_with_text(parent, text, x, y, command, box_color):
        box = tk.Canvas(parent, width=180, height=180, bg=box_color, highlightthickness=0)
        box.place(x=x, y=y)
        box.create_rectangle(0, 0, 180, 180, fill=box_color, outline="#e99d75", width=0)
        line_id = box.create_line(0, 90, 180, 90, width=38, fill="#e99d75")
        box.create_text(90, 90, text=text, font=("Courier", 16, "bold"), fill="black")
        def on_line_click(event):
            command()
        box.tag_bind(line_id, '<Button-1>', on_line_click)
        box.bind("<Button-1>", lambda e: command())
        return box

    def draw_home_boxes():
        # Remove any existing boxes (if re-drawing)
        for widget in home_screen.winfo_children():
            # Don't destroy settings/profile icons
            if isinstance(widget, tk.Canvas) and widget not in [settings_canvas, profile_canvas]:
                widget.destroy()
        add_box_with_text(home_screen, "Clock", 90, 150, lambda: open_clock_screen(container, home_screen), box_color="white")
        add_box_with_text(home_screen, "Soundscapes", 330, 150, lambda: open_soundscapes(container, home_screen), box_color="white")
        add_box_with_text(home_screen, "Schedule", 90, 380, lambda: open_schedule(container, home_screen), box_color="white")
        add_box_with_text(home_screen, "Reminders", 330, 380, lambda: open_reminders(container, home_screen), box_color="white")

    home_screen.draw_home_boxes = draw_home_boxes
    draw_home_boxes()

    tk.Label(home_screen, text='Home screen').pack()
    home_screen.lift()
    root.mainloop()

if __name__ == "__main__":
    main()
