
# **Python Keylogger**

A simple Python-based keylogger that records keystrokes and saves them to a file for analysis or debugging purposes.

## **Features**
- Records all keystrokes, including special keys like Enter, Space, Backspace, etc.
- Logs are saved to a file (`keylog.txt`) in plain text.
- Lightweight and easy to set up.

## **Prerequisites**
- Python 3.6 or later.
- `pynput` library for capturing keyboard input.

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/as4dmin/python-keylogger.git
   cd python-keylogger
   ```

2. Install the required library:
   ```bash
   pip install pynput
   ```

3. Run the keylogger:
   ```bash
   python keylogger.py
   ```

## **Usage**
- Once started, the keylogger will record all keystrokes.
- Logs are saved in the `keylog.txt` file in the project directory.
- To stop the keylogger, terminate the script (e.g., Ctrl+C in the terminal).

## **Customization**
- You can change the output log file by modifying the `LOG_FILE` variable in `keylogger.py`.

## **Disclaimer**
This program is intended for ethical and educational purposes only. Ensure you have the necessary permissions before using this software on any system. Unauthorized use of this program may violate privacy laws and result in legal consequences.

---

## **Example Log Output**
```
hello[Space]world[Enter]
[Shift]Python[Backspace]y[Enter]
```

## **Contributing**
Contributions are welcome! Feel free to submit issues and pull requests.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
