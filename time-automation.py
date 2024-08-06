import pyautogui
import time

def enter_time(time_str):
    pyautogui.write(time_str)
    time.sleep(0.1)
    pyautogui.press('tab')
    time.sleep(0.1)

def enter_time_entry():
    # Increased pause time for better reliability
    pause_time = 0.1    

    # Click into the "From" field for work hours
    time.sleep(pause_time)

    # Clear the field and enter work start time
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    enter_time("09:00")
    
    #pyautogui.press('tab')

    # Clear the field and enter work end time
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    enter_time("17:30")

    # Tab to break fields (2 times)
    for _ in range(1):
        pyautogui.press('tab')
        time.sleep(pause_time)
  

    # Clear the field and enter break start time
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    enter_time("12:00")

    # Clear the field and enter break end time
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    enter_time("12:30")

    # Tab to "Save & add next day" button (5 times)
    for _ in range(4):
        pyautogui.press('tab')
        time.sleep(pause_time)

    # Press Enter to save and move to next day
    pyautogui.press('enter')
    time.sleep(3)  # Increased wait time for page to update

def main():
    print("Please switch to the Personio attendance page.")
    print("The script will start in 5 seconds...")
    time.sleep(2)

    num_days = 5

    for day in range(num_days):
        enter_time_entry()
        print(f"Entered time for day {day + 1}")
        time.sleep(2)  # Wait between days

    print("Time entry complete!")

if __name__ == "__main__":
    main()
