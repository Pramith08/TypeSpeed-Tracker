
# TypeSpeed Tracker

## Overview
**TypeSpeed Tracker** is a Python script designed to measure your typing speed in words per minute (WPM) using two modes: **Live Tracking Mode** and **Random Sentences Mode**. This tool can help you improve your typing skills and monitor your progress over time.

## Features
- **Live Tracking Mode**: Measure your typing speed as you type freely. The script calculates WPM based on the characters and words typed, allowing you to see your performance in real time.
- **Random Sentences Mode**: Type a randomly selected sentence from a predefined list. The script measures your typing speed and accuracy, providing feedback on your performance.
- **Log Files**: All typing sessions are recorded in log files for later review, including details such as characters typed, words typed, WPM, and accuracy.

## Installation
To use this script, you need to have Python installed on your machine. You also need the `keyboard` library, which can be installed via pip.

```bash
pip install keyboard
```

## Usage
1. Clone or download the repository to your local machine.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script using Python:

   ```bash
   python TypeSpeed_Tracker.py
   ```

4. Choose your desired mode by entering `1` for **Live Tracking Mode** or `2` for **Random Sentences Mode**.
5. Follow the on-screen instructions to start typing.

## Logging
- Typing statistics for each session are logged in two separate files:
  - `Live_Keyboard_Log.txt`: Contains logs for the Live Tracking Mode.
  - `Random_Sentence_Keyboard_Log.txt`: Contains logs for the Random Sentences Mode.

## Author
**Pramith Kiran**  
Created on September 29, 2024
