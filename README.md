# 🎲 Guess-the-Number (Tkinter Game)

A simple desktop game with a GUI built using Python and `tkinter`, where you try to guess the number randomly selected by the computer.

---

## 🖥️ Description

**Guess the Number** is a game where the player tries to guess a randomly selected number in as few attempts as possible. The number range is chosen by the player at the beginning of the game using radio buttons:

- 🟢 **Easy**: 0–50  
- 🟡 **Medium**: 0–100  
- 🔴 **Hard**: 0–200

With each attempt, an icon is displayed to show whether the guessed number is too low, too high, or correct.

---

## 📦 Requirements

- Python 3.x
- Image files:
  - `uparrow.png`
  - `downarrow.png`
  - `correct.png`
  - `dice.png`
- Built-in libraries:
  - `tkinter`
  - `random`
  - `os`, `sys`

---

## ▶️ How to Run

1. Make sure the following image files are in the **same folder** as the script:
    - `uparrow.png`
    - `downarrow.png`
    - `correct.png`
    - `dice.png`

2. Run the program:

```bash
python guess_the_number.py
Instructions:

Select a difficulty level and click Randomize to start the game.

Enter a number and press Enter.

See whether your guess is correct or if you need to try again!

📸 Screenshots
Include screenshots of the UI here to show what the game looks like.

markdown
Αντιγραφή
Επεξεργασία
![Screenshot](screenshot1.png)
![Screenshot](screenshot2.png)
💡 Notes
The app can be bundled as a standalone .exe using PyInstaller.

The resource_path() function supports using image files even in a compiled executable version.

📜 License
This project is free to use, modify, and distribute.
Enjoy the game and good luck guessing! 🎉
