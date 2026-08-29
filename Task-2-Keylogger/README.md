# 🔑 Cantilever Cybersecurity Internship — Task 2

## Keylogger Security Demonstration

A Python-based **Keylogger Security Demonstration** developed as part of the **Cantilever Cybersecurity Internship**.

This project demonstrates the fundamental concepts of keyboard event monitoring, event processing, timestamp recording, special-key identification, event counting, and local report generation in a controlled and transparent testing environment.

> ⚠️ **Security Notice**
>
> This project is strictly intended for **educational and authorized cybersecurity testing purposes**. The implementation is designed as a visible demonstration and does not provide covert surveillance, system-wide credential collection, persistence, or network-based data transmission.

---

# 🎯 Objective

The primary objective of this task is to understand the basic working principles of keyboard event monitoring and demonstrate how keyboard events can be detected and processed using Python.

The application provides a controlled testing environment in which the user can:

- Start keyboard event logging.
- Enter test keyboard input.
- Detect keyboard events.
- Identify normal keyboard keys.
- Identify special keyboard keys.
- Record timestamps for each event.
- Count keyboard events during a session.
- Stop event logging.
- Generate a local text-based activity report.

The project focuses on understanding the **security implications of keylogging technology** while maintaining an ethical and controlled implementation.

---

# ✨ Features

## ⌨️ Keyboard Event Detection

The application detects keyboard events generated during the controlled demonstration session.

Example:

```text
[2026-08-29 12:05:02] c
[2026-08-29 12:05:03] a
[2026-08-29 12:05:03] n
[2026-08-29 12:05:03] t
```

---

## 🕒 Timestamp Recording

Each detected keyboard event is recorded together with the date and time at which the event occurred.

Example:

```text
[2026-08-29 12:05:08] c
[2026-08-29 12:05:08] y
[2026-08-29 12:05:08] b
```

This makes it possible to determine when individual keyboard events occurred during a demonstration session.

---

## 🔑 Special Key Detection

Special keyboard keys are converted into readable names.

Examples include:

```text
[SPACE]
[ENTER]
[BACKSPACE]
[TAB]
[CTRL]
[SHIFT]
[ESC]
```

This makes the generated report easier to understand and analyze.

---

## 📊 Event Counter

The application maintains a count of keyboard events recorded during the current demonstration session.

The final report contains the total number of recorded events.

Example:

```text
Session Stopped: 2026-08-29 12:05:16
Total Events: 24
```

---

## ▶️ Start and Stop Controls

The application provides controls for starting and stopping the keyboard event demonstration.

This allows the user to explicitly control when event recording begins and ends.

---

## 📄 Local Report Generation

Recorded keyboard events are stored locally in:

```text
results/key_events.txt
```

The report contains:

- Session start time
- Keyboard events
- Event timestamps
- Special-key names
- Session stop time
- Total event count

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3** | Application development |
| **Tkinter** | Graphical user interface |
| **pynput** | Keyboard event handling |
| **datetime** | Timestamp generation |
| **File Handling** | Local report generation |
| **Git** | Version control |
| **GitHub** | Source-code hosting |

---

# 📁 Project Structure

```text
Task-2-Keylogger/
│
├── keylogger.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── results/
    └── key_events.txt
```

### File Description

| File / Directory | Description |
|---|---|
| `keylogger.py` | Main Python application |
| `README.md` | Project documentation |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Prevents unnecessary/local files from being committed |
| `results/` | Stores demonstration output |
| `key_events.txt` | Sample keyboard-event report |

> `venv/` is intentionally excluded from GitHub through `.gitignore` because virtual environments are local development environments.

---

# 🔄 Application Workflow

The application follows the workflow below:

```text
                         USER
                           │
                           ▼
                  Launch Application
                           │
                           ▼
                 Visible Test Interface
                           │
                           ▼
                    Start Logging
                           │
                           ▼
                  Enter Test Input
                           │
                           ▼
                  Detect Key Event
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
             Normal Key          Special Key
                 │                   │
                 ▼                   ▼
            Record Key          Convert to Name
                 │                   │
                 └─────────┬─────────┘
                           │
                           ▼
                    Add Timestamp
                           │
                           ▼
                   Update Counter
                           │
                           ▼
                   Save Local Event
                           │
                           ▼
                     Stop Logging
                           │
                           ▼
                  Generate Report
                           │
                           ▼
              results/key_events.txt
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

Clone the main Cantilever repository:

```bash
git clone https://github.com/kv237/CANTILEVER.git
```

Navigate to the Task 2 directory:

```bash
cd CANTILEVER/Task-2-Keylogger
```

---

## 2. Create a Virtual Environment

Creating a virtual environment keeps project dependencies isolated from the system Python installation.

### Windows Command Prompt

Create the environment:

```cmd
py -m venv venv
```

Activate it:

```cmd
venv\Scripts\activate
```

After successful activation, the terminal should display:

```text
(venv)
```

---

## 3. Git Bash Setup

If Git Bash is being used, activate the virtual environment with:

```bash
py -m venv venv
source venv/Scripts/activate
```

A successful activation should display:

```text
(venv)
```

---

## 4. Install Dependencies

Install the project dependencies:

```bash
pip install -r requirements.txt
```

The primary package used by this project is:

```text
pynput
```

---

# ▶️ How to Run

Make sure the virtual environment is activated.

Run:

```bash
python keylogger.py
```

The application will launch the controlled demonstration interface.

Use the interface to start and stop event recording.

---

# 🧪 Testing Procedure

The application can be tested using harmless demonstration text.

## Step 1 — Launch the Application

Run:

```bash
python keylogger.py
```

---

## Step 2 — Start the Demonstration

Use the application's **Start Logging** control.

---

## Step 3 — Enter Test Input

Enter harmless test text.

For example:

```text
Cantilever Cybersecurity
```

---

## Step 4 — Test Special Keys

Test selected keyboard keys such as:

```text
Space
Enter
Backspace
Tab
```

The application should represent supported special keys using readable labels.

Example:

```text
[SPACE]
[ENTER]
[BACKSPACE]
[TAB]
```

---

## Step 5 — Stop the Demonstration

Use the application's **Stop Logging** control.

---

## Step 6 — Verify the Report

The recorded results are stored in:

```text
results/key_events.txt
```

To display the report in Windows Command Prompt:

```cmd
type results\key_events.txt
```

---

# 📊 Sample Output / Results

A successful demonstration session produced the following output:

```text
============================================================
KEYLOGGER SECURITY DEMONSTRATION
Session Started: 2026-08-29 12:05:00
============================================================
[2026-08-29 12:05:02] c
[2026-08-29 12:05:03] a
[2026-08-29 12:05:03] n
[2026-08-29 12:05:03] t
[2026-08-29 12:05:04] i
[2026-08-29 12:05:05] l
[2026-08-29 12:05:05] e
[2026-08-29 12:05:06] v
[2026-08-29 12:05:06] e
[2026-08-29 12:05:06] r
[2026-08-29 12:05:07] [SPACE]
[2026-08-29 12:05:08] c
[2026-08-29 12:05:08] y
[2026-08-29 12:05:08] b
[2026-08-29 12:05:09] e
[2026-08-29 12:05:09] r
[2026-08-29 12:05:09] s
[2026-08-29 12:05:10] e
[2026-08-29 12:05:10] c
[2026-08-29 12:05:10] u
[2026-08-29 12:05:11] r
[2026-08-29 12:05:11] i
[2026-08-29 12:05:11] t
[2026-08-29 12:05:11] y

Session Stopped: 2026-08-29 12:05:16
Total Events: 24
============================================================
```

### Result Summary

| Test Item | Result |
|---|---|
| Application launched | ✅ Successful |
| Keyboard events detected | ✅ Successful |
| Normal keys recorded | ✅ Successful |
| Space key detected | ✅ Successful |
| Timestamps generated | ✅ Successful |
| Event counter updated | ✅ Successful |
| Session stopped correctly | ✅ Successful |
| Text report generated | ✅ Successful |

The demonstration successfully recorded **24 keyboard events** during the sample session.

---

# 🔍 Verification

The generated report can be verified directly from the project directory.

Run:

```cmd
type results\key_events.txt
```

The report should contain the session header, recorded events, timestamps, session termination information, and total event count.

A successful report follows this general structure:

```text
============================================================
KEYLOGGER SECURITY DEMONSTRATION
Session Started: YYYY-MM-DD HH:MM:SS
============================================================

[YYYY-MM-DD HH:MM:SS] key
[YYYY-MM-DD HH:MM:SS] key
[YYYY-MM-DD HH:MM:SS] [SPECIAL_KEY]

Session Stopped: YYYY-MM-DD HH:MM:SS
Total Events: N
============================================================
```

---

# 🔐 Cybersecurity Relevance

Keylogging is an important cybersecurity topic because malicious keylogging techniques can potentially be used to monitor user input and obtain sensitive information.

Potential targets can include:

- Usernames
- Passwords
- Messages
- Financial information
- Other sensitive keyboard input

Studying the concept helps cybersecurity professionals understand:

- How keyboard events can be detected.
- How malicious keyloggers may operate.
- Why endpoint security is important.
- How suspicious activity can be identified.
- Why secure authentication mechanisms are necessary.

This project focuses on the **educational understanding of the underlying concept** rather than covert deployment.

---

# 🛡️ Security Considerations

Organizations and users can reduce the risk associated with malicious keylogging through appropriate security controls.

Recommended practices include:

- Keep operating systems and applications updated.
- Use reputable endpoint security software.
- Monitor suspicious processes and applications.
- Review unexpected startup programs.
- Avoid installing software from untrusted sources.
- Apply least-privilege principles.
- Use multi-factor authentication.
- Monitor unusual system behavior.
- Restrict unauthorized software execution.
- Maintain appropriate endpoint monitoring and logging.

---

# ⚠️ Ethical Considerations

Keylogging technology can be misused when deployed without authorization.

This project is therefore intended only for:

- Educational purposes.
- Authorized security testing.
- Systems owned by the tester.
- Controlled laboratory environments.
- Demonstrations performed with appropriate consent.

**Never use keylogging software to secretly monitor another person's activity or capture credentials without authorization.**

---

# 📌 Limitations

This implementation is intentionally designed as a controlled educational demonstration.

It does **not** provide:

- Covert background operation.
- System-wide surveillance.
- Credential harvesting from external applications.
- Network transmission of captured information.
- Remote command-and-control functionality.
- Persistence mechanisms.
- Stealth or evasion techniques.

The implementation is therefore intended to demonstrate the basic concept while avoiding features associated with covert surveillance or credential theft.

---

# 📚 Learning Outcomes

Through this project, the following concepts were demonstrated:

- Python application development.
- Keyboard event handling.
- Event-driven programming.
- Special-key identification.
- Timestamp generation.
- Session-based event tracking.
- Local file handling.
- Report generation.
- Basic cybersecurity threat concepts.
- Security and ethical considerations.
- Git and GitHub project organization.

The project also provides practical exposure to the difference between **security research/demonstration** and potentially malicious keylogging behavior.

---

# 👨‍💻 Internship Information

**Organization:** Cantilever

**Program:** Cybersecurity Internship

**Task:** Task 2 — Keylogger Security Demonstration

**Category:** Cybersecurity / Python

**Implementation:** Controlled Educational Demonstration

**Repository:** CANTILEVER

---

# 👤 Author

**Krishna Vamshi**

Cybersecurity Internship Candidate

GitHub:

https://github.com/kv237

---

# 📜 Disclaimer

This project is provided strictly for **educational, research, and authorized cybersecurity testing purposes**.

The author does not support or encourage unauthorized monitoring, credential theft, privacy violations, or deployment of keylogging software against systems or users without permission.

Users are responsible for ensuring that their use of this project complies with applicable laws, organizational policies, and ethical security-testing practices.

---

## ⭐ Project Summary

This project demonstrates the fundamental principles of keyboard event monitoring through a controlled Python application.

It combines:

```text
Python
   │
   ├── Keyboard Event Detection
   ├── Special-Key Handling
   ├── Timestamp Recording
   ├── Event Counting
   └── Local Report Generation
```

The implementation emphasizes **transparency, controlled testing, cybersecurity awareness, and ethical use**.
