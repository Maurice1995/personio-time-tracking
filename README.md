# Personio Time Automation Scripts

This repository contains two Python scripts designed to automate time entry in the Personio HR management system. These scripts use GUI automation to input randomized work times within specified parameters, making the time tracking process more efficient and less monotonous.

## Scripts

1. `time_correction_randomized.py`
2. `time_automation.py`

Both scripts perform similar functions with slight variations in their implementation.

## Features

- Generates random work start and end times within specified ranges
- Ensures total work time is between 7 hours 42 minutes and 8 hours 30 minutes
- Rounds all times to the nearest 5-minute interval
- Automates data entry into the Personio web interface
- Supports entering data for multiple days in a single run

## Requirements

- Python 3.x
- PyAutoGUI library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/personio-time-automation.git
   ```

2. Install the required Python library:
   ```
   pip install pyautogui
   ```

## Usage

1. Open your Personio attendance page in your web browser.
2. Run either of the scripts:
   ```
   python time_correction_randomized.py
   ```
   or
   ```
   python time_automation.py
   ```
3. When prompted, enter the number of days you want to process.
4. Ensure your cursor is in the correct starting position and that the Personio window is one Alt+Tab away from your current window.
5. The script will switch to the Personio window and begin entering data.

## Customization

You can modify the following parameters in the scripts to suit your needs:

- Work start time range (default: 09:00 - 09:55)
- Minimum work duration (default: 8 hours 12 minutes (including 30 minutes break))
- Maximum work duration (default: 9 hours (including 30 minutes break))
- Break start and end times (default: 12:00 - 12:30)

## Caution

These scripts use GUI automation, which means they simulate keyboard and mouse inputs. Ensure that you:

1. Have permission to use such automation tools with your Personio account.
2. Do not interact with your computer while the script is running to avoid interfering with the automation.
3. Are aware of your company's policies regarding time tracking and automation tools.

## Disclaimer

These scripts are provided "as is" without warranty of any kind. Use them at your own risk. The authors are not responsible for any consequences resulting from the use of these scripts.

## License

MIT License

Copyright (c) [2024] 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.