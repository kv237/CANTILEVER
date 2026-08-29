import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os


# ============================================================
# Configuration
# ============================================================

RESULTS_DIR = "results"
LOG_FILE = os.path.join(RESULTS_DIR, "key_events.txt")


# ============================================================
# Key Logger Application
# ============================================================

class KeyLoggerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger Security Demonstration")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.logging_active = False
        self.event_count = 0

        os.makedirs(RESULTS_DIR, exist_ok=True)

        self.create_interface()

    # --------------------------------------------------------
    # Create GUI
    # --------------------------------------------------------

    def create_interface(self):

        title = tk.Label(
            self.root,
            text="KEYLOGGER SECURITY DEMONSTRATION",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=20)

        description = tk.Label(
            self.root,
            text=(
                "Educational demonstration: keyboard events are "
                "recorded only inside this application."
            ),
            font=("Arial", 10)
        )
        description.pack(pady=5)

        self.status_label = tk.Label(
            self.root,
            text="Status: Logging Stopped",
            font=("Arial", 11, "bold")
        )
        self.status_label.pack(pady=10)

        # Text input area
        self.text_area = tk.Text(
            self.root,
            height=10,
            width=70,
            font=("Consolas", 12)
        )
        self.text_area.pack(pady=10)

        self.text_area.insert(
            "1.0",
            "Click 'Start Logging' and type here..."
        )

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.start_button = tk.Button(
            button_frame,
            text="Start Logging",
            width=15,
            command=self.start_logging
        )
        self.start_button.grid(
            row=0,
            column=0,
            padx=5
        )

        self.stop_button = tk.Button(
            button_frame,
            text="Stop Logging",
            width=15,
            command=self.stop_logging
        )
        self.stop_button.grid(
            row=0,
            column=1,
            padx=5
        )

        self.clear_button = tk.Button(
            button_frame,
            text="Clear Text",
            width=15,
            command=self.clear_text
        )
        self.clear_button.grid(
            row=0,
            column=2,
            padx=5
        )

        self.exit_button = tk.Button(
            button_frame,
            text="Exit",
            width=15,
            command=self.exit_application
        )
        self.exit_button.grid(
            row=0,
            column=3,
            padx=5
        )

        # Event counter
        self.counter_label = tk.Label(
            self.root,
            text="Key Events Recorded: 0",
            font=("Arial", 11)
        )
        self.counter_label.pack(pady=10)

        # Bind keyboard events only to this text area
        self.text_area.bind(
            "<KeyPress>",
            self.handle_keypress
        )

        # Initial focus
        self.text_area.focus_set()

    # --------------------------------------------------------
    # Start Logging
    # --------------------------------------------------------

    def start_logging(self):

        self.logging_active = True

        self.status_label.config(
            text="Status: Logging Active"
        )

        self.text_area.focus_set()

        self.write_session_header()

    # --------------------------------------------------------
    # Stop Logging
    # --------------------------------------------------------

    def stop_logging(self):

        self.logging_active = False

        self.status_label.config(
            text="Status: Logging Stopped"
        )

        self.write_session_footer()

    # --------------------------------------------------------
    # Handle Keyboard Event
    # --------------------------------------------------------

    def handle_keypress(self, event):

        if not self.logging_active:
            return

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        key_name = self.get_key_name(event)

        self.event_count += 1

        self.counter_label.config(
            text=f"Key Events Recorded: {self.event_count}"
        )

        self.save_event(
            timestamp,
            key_name
        )

    # --------------------------------------------------------
    # Convert Key Event to Readable Name
    # --------------------------------------------------------

    def get_key_name(self, event):

        special_keys = {
            "space": "[SPACE]",
            "Return": "[ENTER]",
            "BackSpace": "[BACKSPACE]",
            "Tab": "[TAB]",
            "Escape": "[ESC]",
            "Shift_L": "[SHIFT]",
            "Shift_R": "[SHIFT]",
            "Control_L": "[CTRL]",
            "Control_R": "[CTRL]",
            "Alt_L": "[ALT]",
            "Alt_R": "[ALT]",
            "Caps_Lock": "[CAPS LOCK]",
            "Delete": "[DELETE]",
            "Insert": "[INSERT]",
            "Home": "[HOME]",
            "End": "[END]",
            "Left": "[LEFT]",
            "Right": "[RIGHT]",
            "Up": "[UP]",
            "Down": "[DOWN]"
        }

        if event.keysym in special_keys:
            return special_keys[event.keysym]

        if event.char:
            return event.char

        return f"[{event.keysym}]"

    # --------------------------------------------------------
    # Save Key Event
    # --------------------------------------------------------

    def save_event(self, timestamp, key_name):

        try:

            with open(
                LOG_FILE,
                "a",
                encoding="utf-8"
            ) as file:

                file.write(
                    f"[{timestamp}] {key_name}\n"
                )

        except OSError as error:

            messagebox.showerror(
                "File Error",
                f"Could not save key event:\n{error}"
            )

    # --------------------------------------------------------
    # Write Session Header
    # --------------------------------------------------------

    def write_session_header(self):

        try:

            with open(
                LOG_FILE,
                "a",
                encoding="utf-8"
            ) as file:

                file.write("\n")
                file.write("=" * 60)
                file.write("\n")
                file.write("KEYLOGGER SECURITY DEMONSTRATION")
                file.write("\n")
                file.write(
                    "Session Started: "
                    + datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                )
                file.write("\n")
                file.write("=" * 60)
                file.write("\n")

        except OSError as error:

            messagebox.showerror(
                "File Error",
                f"Could not create log file:\n{error}"
            )

    # --------------------------------------------------------
    # Write Session Footer
    # --------------------------------------------------------

    def write_session_footer(self):

        try:

            with open(
                LOG_FILE,
                "a",
                encoding="utf-8"
            ) as file:

                file.write("\n")
                file.write(
                    "Session Stopped: "
                    + datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                )
                file.write("\n")
                file.write(
                    f"Total Events: {self.event_count}"
                )
                file.write("\n")
                file.write("=" * 60)
                file.write("\n")

        except OSError as error:

            messagebox.showerror(
                "File Error",
                f"Could not save session information:\n{error}"
            )

    # --------------------------------------------------------
    # Clear Text
    # --------------------------------------------------------

    def clear_text(self):

        self.text_area.delete(
            "1.0",
            tk.END
        )

        self.text_area.focus_set()

    # --------------------------------------------------------
    # Exit
    # --------------------------------------------------------

    def exit_application(self):

        if self.logging_active:

            self.stop_logging()

        self.root.destroy()


# ============================================================
# Main
# ============================================================

def main():

    root = tk.Tk()

    application = KeyLoggerApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
