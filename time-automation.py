import pyautogui
import time
import random
from datetime import datetime, timedelta

def round_to_nearest_5_minutes(dt):
    """Round a datetime object to the nearest 5 minutes"""
    minutes = (dt.minute // 5) * 5
    return dt.replace(minute=minutes, second=0, microsecond=0)

def random_time(start, end):
    """Generate a random time between start and end, rounded to 5-minute intervals"""
    start_dt = datetime.strptime(start, "%H:%M")
    end_dt = datetime.strptime(end, "%H:%M")
    delta = int((end_dt - start_dt).total_seconds())
    if delta <= 0:
        return end  # If start is equal to or later than end, return end time
    random_seconds = random.randint(0, delta)
    random_time = start_dt + timedelta(seconds=random_seconds)
    rounded_time = round_to_nearest_5_minutes(random_time)
    return rounded_time.strftime("%H:%M")

def generate_work_times():
    work_start_time = random_time("09:00", "09:55")

    # Calculate the earliest and latest possible end times
    start_dt = datetime.strptime(work_start_time, "%H:%M")
    earliest_end = max((start_dt + timedelta(hours=8, minutes=12)).time(), datetime.strptime("17:00", "%H:%M").time())
    latest_end = min((start_dt + timedelta(hours=9)).time(), datetime.strptime("17:55", "%H:%M").time())
    
    # Ensure earliest_end is not later than latest_end
    if earliest_end > latest_end:
        earliest_end = latest_end

    work_stop_time = random_time(earliest_end.strftime("%H:%M"), latest_end.strftime("%H:%M"))
    
    return work_start_time, work_stop_time

def enter_time(time_str):
    pyautogui.write(time_str)
    time.sleep(0.1)
    pyautogui.press('tab')
    time.sleep(0.1)

def enter_time_entry(work_start_time, work_stop_time, break_start_time, break_end_time):
    pause_time = 0.1    

    time.sleep(pause_time)

    # Enter work start time
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    enter_time(work_start_time)

    # Enter work end time
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    enter_time(work_stop_time)

    # Tab to break fields (1 time)
    pyautogui.press('tab')
    time.sleep(pause_time)

    # Enter break start time
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    enter_time(break_start_time)

    # Enter break end time
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    enter_time(break_end_time)

    # Tab to "Save & add next day" button (5 times)
    for _ in range(4):
        pyautogui.press('tab')
        time.sleep(pause_time)

    # Press Enter to save and move to next day
    pyautogui.press('enter')
    time.sleep(3)  # Increased wait time for page to update

def main():
    print("Script is starting, make sure you have your curser in the right spot and that Personio is one Alt+Tab away.")

    num_days = int(input("Enter the number of days to process: "))

    time.sleep(1)

    # Perform the initial alt+tab to switch to the browser window
    pyautogui.hotkey('alt', 'tab')

    time.sleep(1)  # Wait a bit longer after switching windows

    
    break_start_time = "12:00"
    break_end_time = "12:30"

    for day in range(num_days):
        work_start_time, work_stop_time = generate_work_times()
        enter_time_entry(work_start_time, work_stop_time, break_start_time, break_end_time)
        print(f"Day {day + 1}: Work {work_start_time} - {work_stop_time}, Break {break_start_time} - {break_end_time}")
        time.sleep(2)

    print("Time entry complete!")

if __name__ == "__main__":
    main()
