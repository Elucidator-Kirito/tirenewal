import time

def start_pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Remaining time: {seconds // 60} minutes {seconds % 60} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Take a short break.")

def main():
    print("Welcome to the Focus Timer!")
    while True:
        try:
            minutes = int(input("Enter the number of minutes for your pomodoro session: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    start_pomodoro_timer(minutes)

if __name__ == "__main__":
    main()

