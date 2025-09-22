# Moonveil: Sleep Habit App
# This is the home screen that links to different parts of the app

# Function to show user information
def show_user_info():
    print("\n--- User Information ---")
    print("Name: [Your Name Here]")
    print("Sleep Goal: 8 hours/night")
    print("Notifications: ON")

# Function to open settings
def open_settings():
    print("\n--- Settings ---")
    print("1. Change sleep goal")
    print("2. Toggle notifications")
    print("3. Back to Home")

# Function to play soundscapes
def play_soundscapes():
    print("\n--- Soundscapes ---")
    print("Choose a sound to play:")
    print("1. Rain")
    print("2. Ocean")
    print("3. White Noise")

# Function to view reminders
def view_reminders():
    print("\n--- Reminders ---")
    print("1. Avoid caffeine after 3 PM")
    print("2. Wind down by 9:30 PM")
    print("3. Put phone away by 10 PM")

# Function to show clock
def show_clock():
    print("\n--- Clock ---")
    print("Current time: [Add real time later]")
    print("Bedtime countdown: [Add timer later]")

# Function to view schedule
def view_schedule():
    print("\n--- Schedule ---")
    print("App blocking starts at: 10:00 PM")
    print("Wake-up time: 7:00 AM")

# Main home screen function

def home_screen():
    while True:
        print("\n=== Moonveil Home Screen ===")
        print("\n[Q] Settings        [E] User Info")
        print("+-----------+   +-----------+")
        print("|           |   |           |")
        print("|   [A]     |   |   [D]     |")
        print("|  Clock    |   | Sound-    |")
        print("|           |   | scapes    |")
        print("+-----------+   +-----------+")
        print("+-----------+   +-----------+")
        print("|           |   |           |")
        print("|   [Z]     |   |   [C]     |")
        print("| Schedule  |   | Reminders |")
        print("|           |   |           |")
        print("+-----------+   +-----------+")
        print("\n[X] Exit")

        choice = input("Choose an option (Q/E/A/D/Z/C/X): ").strip().upper()

        if choice == "Q":
            open_settings()
        elif choice == "E":
            show_user_info()
        elif choice == "A":
            show_clock()
        elif choice == "D":
            play_soundscapes()
        elif choice == "Z":
            view_schedule()
        elif choice == "C":
            view_reminders()
        elif choice == "X":
            print("Goodbye! 🌙")
            break
        else:
            print("Please choose a valid option.")

# Run the app
home_screen()
