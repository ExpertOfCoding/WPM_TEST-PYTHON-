# DBK WPM Typing Test

## Overview
The DBK WPM Typing Test is a Python-based application designed to measure typing speed (Words Per Minute, WPM) and accuracy. It uses the `tkinter` library to provide a graphical interface where users can type sentences and receive real-time feedback on their performance.

---

## Features
- **Random Sentence Selection:** Sentences are loaded from an external text file (`sentences.txt`) and displayed randomly for each session.
- **Real-Time Feedback:** The application tracks correct and incorrect key presses, displaying the results immediately.
- **WPM Calculation:** The typing speed is calculated in real-time, using the standard formula for WPM.
- **Session Results Logging:** Performance metrics, including WPM, correct key presses, typos, and session duration, are logged in a results file (`sonuc.txt`).

---

## How It Works

### Main Components

1. **Graphical User Interface (GUI):** Built using `tkinter`, it includes labels, entry fields, and buttons to interact with the user.
2. **Random Sentence Loading:** Sentences are loaded from a text file and selected randomly for each session.
3. **Real-Time Typing Feedback:** Tracks the user’s progress, providing updates on accuracy and speed.
4. **Performance Logging:** Saves results to an external file for future reference.

---

## File Structure

### 1. **main.py**
The main Python script that runs the typing test.

### 2. **sentences.txt**
A text file containing sentences for the typing test. Each line in this file represents a potential sentence for the test.

### 3. **sonuc.txt**
A log file where the results of each typing session are stored, including WPM, accuracy, and duration.

---

## Code Walkthrough

### 1. **Imports and Window Setup**
```python
import time
import tkinter as tk
import random

window = tk.Tk()
window.title("DBK Testi")
window.config(background="black", pady=100)
window.minsize(300, 400)
```
- `time`: Used for measuring session duration.
- `tkinter`: Provides the graphical interface.
- `random`: Selects random sentences from the text file.
- The `tk.Tk` object initializes the main application window.

### 2. **Global Variables and Sentence Loading**
```python
sv = tk.StringVar()
CORRECT = 0
FALSE = 0
with open("sentences.txt", "r", encoding="UTF-8") as file:
    readedlines = file.readlines()
    randomsayi = random.randint(0, len(readedlines) - 1)
    text = readedlines[randomsayi].strip()
```
- `sv`: Tracks user input.
- `CORRECT` and `FALSE`: Track the number of correct and incorrect key presses.
- Sentences are loaded from `sentences.txt` and one is selected randomly.

### 3. **Callback and Real-Time Typing Feedback**
```python
def callback(a, b, c):
    global CORRECT, FALSE, text
    if sv.get() == text[:len(sv.get())]:
        CORRECT += 1
    else:
        FALSE += 1
    if sv.get() == text:
        sv.set("")  # Reset input
```
- The `callback` function is triggered on every user input, checking for correctness and updating metrics.

### 4. **Performance Calculation**
```python
def goon():
    WPM = ((CORRECT / 5) / (time.time() - time_t)) * 60
    Label2.config(text=f"WPM: {WPM:0.1f}")
    if not OKAY:
        with open("sonuc.txt", "a", encoding="UTF-8") as file:
            file.write(f"WPM: {WPM:0.1f}, Correct: {CORRECT}, Typos: {FALSE}\n")
```
- Calculates WPM in real-time and updates the display.
- Results are saved to `sonuc.txt` at the end of the session.

### 5. **GUI Components**
```python
Label = tk.Label(text=text, pady=20, bg="black", fg="white")
Entry = tk.Entry(width=50, textvariable=sv)
Label1 = tk.Label(frame, text=f"Correct: {CORRECT}", bg="black", fg="green")
Label3 = tk.Label(frame, text=f"Typos: {FALSE}", bg="black", fg="red")
Label2 = tk.Label(text=f"WPM: {WPM}", bg="black", fg="white")
```
- Labels and entry fields display the current text, performance metrics, and user input.

---

## Usage

1. **Run the Application:**
   ```bash
   python main.py
   ```

2. **Typing Test:**
   - Type the displayed text into the entry field.
   - The application will provide real-time feedback on your performance.

3. **View Results:**
   - Open `sonuc.txt` to view the logged results of each session.

---

## Customization

1. **Adding New Sentences:**
   - Add new lines to `sentences.txt` to include more sentences in the typing test.

2. **Changing Design:**
   - Modify `tk.Label` and `tk.Entry` properties in `main.py` to adjust colors, sizes, and styles.

---

## Example Results
```plaintext
WPM: 79.7, Correct: 73, Typos: 7, Total: 80
WPM: 88.3, Correct: 63, Typos: 3, Total: 66
WPM: 120.8, Correct: 58, Typos: 3, Total: 61
```
- Results include WPM, correct and incorrect key presses, total key presses, and session duration.

---

## Future Improvements
- Add a leaderboard to display top performances.
- Include a countdown timer for fixed-duration tests.
- Support multi-language sentences for typing practice.
- Enhance UI for better user experience.

---

## Dependencies
- Python 3.x
- `tkinter` (comes pre-installed with Python)

---

## License
This project is open-source and available under the MIT License.

