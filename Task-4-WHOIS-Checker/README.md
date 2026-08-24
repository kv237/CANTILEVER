# 🔎 Cantilever Cybersecurity Internship — Task 4

## WHOIS Domain Information Checker

A Python-based cybersecurity utility that retrieves publicly available **WHOIS domain registration information** and generates structured reports in **CSV and TXT formats**.

This project was developed as part of the **Cantilever Cybersecurity Internship**.

---

## 🎯 Objective

The objective of this task is to develop a command-line WHOIS information checker that allows users to enter a domain name and retrieve publicly available registration information.

The application retrieves:

- Domain name
- Registrar
- Creation date
- Expiration date
- Name servers
- Domain status

The retrieved information is displayed in the terminal and saved as reports.

---

## ✨ Features

- Domain name input through the command line
- Domain format validation
- WHOIS information lookup
- Registrar information
- Domain creation date
- Domain expiration date
- Name server information
- Domain status
- Error handling
- CSV report generation
- Individual TXT report generation

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Application development |
| python-whois | WHOIS information retrieval |
| CSV | Structured result storage |
| Regular Expressions | Domain validation |
| File Handling | Report generation |
| datetime | Date formatting |
| Git | Version control |
| GitHub | Source code hosting |

---

## 📁 Project Structure

```text
Task-4-WHOIS-Checker/
│
├── whois_checker.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── results/
    ├── whois_results.csv
    ├── google_com.txt
    └── github_com.txt
```

---

# 🔄 Application Workflow

The WHOIS Domain Information Checker follows the workflow below:

```text
              User
                │
                ▼
        Enter Domain Name
                │
                ▼
        Validate Domain
                │
        ┌───────┴───────┐
        │               │
      Valid           Invalid
        │               │
        ▼               ▼
   WHOIS Lookup      Show Error
        │
        ▼
 Retrieve Information
        │
        ├── Domain
        ├── Registrar
        ├── Creation Date
        ├── Expiration Date
        ├── Name Servers
        └── Status
                │
                ▼
         Display Results
                │
        ┌───────┴───────┐
        ▼               ▼
   CSV Report       TXT Report
```

### Workflow Description

1. **User enters a domain name**  
   The application accepts a domain name through the command line.

2. **Domain validation**  
   The application checks whether the entered domain follows the expected format.

3. **WHOIS lookup**  
   If the domain is valid, the application performs a WHOIS lookup.

4. **Retrieve information**  
   The application retrieves available information including:
   - Domain
   - Registrar
   - Creation Date
   - Expiration Date
   - Name Servers
   - Status

5. **Display results**  
   The retrieved WHOIS information is displayed in the terminal.

6. **Generate reports**  
   The information is saved in two formats:
   - CSV report for structured data
   - TXT report for human-readable information

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

Clone the main Cantilever repository:

```bash
git clone https://github.com/kv237/CANTILEVER.git
```

---

## 2. Navigate to Task 4

```bash
cd CANTILEVER/Task-4-WHOIS-Checker
```

---

## 3. Create a Virtual Environment

Windows:

```bash
py -m venv venv
```

---

## 4. Activate the Virtual Environment

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

After activation, you should see:

```text
(venv)
```

at the beginning of your terminal prompt.

### Git Bash

```bash
source venv/Scripts/activate
```

---

## 5. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The main dependency used by this project is:

```text
python-whois
```

---

# ▶️ Running the Application

Run the WHOIS checker using:

```bash
python whois_checker.py
```

The application will display:

```text
============================================================
          WHOIS DOMAIN INFO CHECKER
============================================================
Enter domain name:
```

Enter a valid domain name.

For example:

```text
google.com
```

---

# 🧪 Testing the Application

The application can be tested using publicly available domains.

## Test 1 — Google

Run:

```bash
python whois_checker.py
```

Enter:

```text
google.com
```

Expected output will contain information similar to:

```text
============================================================
             WHOIS DOMAIN INFORMATION
============================================================

Domain: GOOGLE.COM
Registrar: MarkMonitor, Inc.
Creation Date: 1997-09-15 04:00:00
Expiration Date: 2028-09-14 04:00:00
Name Servers: NS1.GOOGLE.COM, NS2.GOOGLE.COM,
              NS3.GOOGLE.COM, NS4.GOOGLE.COM
Status: clientDeleteProhibited

============================================================
```

> **Note:** WHOIS information can change over time. The exact dates, status values, and other information returned may be different when the application is executed.

---

## Test 2 — GitHub

Run:

```bash
python whois_checker.py
```

Enter:

```text
github.com
```

The application should retrieve and display information including:

- Domain
- Registrar
- Creation date
- Expiration date
- Name servers
- Status

---

## Test 3 — Invalid Domain

Run:

```bash
python whois_checker.py
```

Enter:

```text
cantilever
```

The application should reject the input and display a message similar to:

```text
Invalid domain name: cantilever

Please enter a valid domain such as:
google.com
example.org
github.com
```

---

# 📊 Generated Results

After a successful lookup, the application saves the information in two formats.

## CSV Report

The combined results are stored in:

```text
results/whois_results.csv
```

The CSV contains fields such as:

```text
Domain
Registrar
Creation Date
Expiration Date
Name Servers
Status
```

Multiple domain lookups can be stored in the same CSV file.

---

## TXT Report

An individual human-readable TXT report is generated for each domain.

Examples:

```text
results/google_com.txt
results/github_com.txt
```

Each TXT report contains the WHOIS information retrieved for that domain.

---

# 🔍 How to Verify the Results

After running the program, check the `results` directory.

### Windows Command Prompt

```cmd
dir results
```

### Git Bash

```bash
ls results
```

You should see files similar to:

```text
google_com.txt
github_com.txt
whois_results.csv
```

---

## View the CSV Report

### Windows Command Prompt

```cmd
type results\whois_results.csv
```

### Git Bash

```bash
cat results/whois_results.csv
```

---

## View a TXT Report

### Windows Command Prompt

```cmd
type results\google_com.txt
```

### Git Bash

```bash
cat results/google_com.txt
```

This allows an evaluator to verify that the application successfully generated the requested reports.

---

# 📋 Example Output

For a successful lookup such as `google.com`, the terminal displays:

```text
============================================================
             WHOIS DOMAIN INFORMATION
============================================================
Domain: GOOGLE.COM
Registrar: MarkMonitor, Inc.
Creation Date: 1997-09-15 04:00:00
Expiration Date: 2028-09-14 04:00:00
Name Servers: NS1.GOOGLE.COM, NS2.GOOGLE.COM,
              NS3.GOOGLE.COM, NS4.GOOGLE.COM
Status: clientDeleteProhibited
============================================================
```

The application then saves:

```text
WHOIS information saved to:
results\whois_results.csv

TXT report saved to:
results\google_com.txt
```

---

# ❌ Error Handling

## Empty Input

If the user does not enter a domain:

```text
Error: Domain name cannot be empty.
```

---

## Invalid Domain

If an invalid domain is entered:

```text
Invalid domain name: cantilever

Please enter a valid domain such as:
google.com
example.org
github.com
```

---

## WHOIS Lookup Failure

If the WHOIS lookup cannot be completed, the application reports the failure instead of terminating unexpectedly.

Example:

```text
WHOIS lookup failed
```

WHOIS availability can vary depending on the domain extension, registry, registrar, privacy settings, WHOIS server availability, and network connectivity.

---

# 🔐 Cybersecurity Relevance

WHOIS information can be useful during legitimate cybersecurity reconnaissance and domain investigation.

It can provide publicly available information that may help security professionals understand:

- Domain registration details
- Registrar relationships
- Domain lifecycle
- Name server infrastructure
- Domain status

This information can support legitimate:

- Threat intelligence
- Domain investigation
- Security assessments
- Reconnaissance activities

---

# ⚠️ Data Availability

WHOIS information is not guaranteed to be available for every domain.

Returned information can vary depending on:

- Domain extension
- Registry policies
- Registrar configuration
- Privacy protection
- WHOIS server availability
- Registry restrictions

Some information may therefore be missing, redacted, or unavailable.

---

# 🚀 Future Improvements

Possible future enhancements include:

- Batch WHOIS lookup
- JSON report generation
- DNS record lookup
- IP address resolution
- Reverse DNS lookup
- Domain expiration alerts
- Domain availability checking
- Interactive web interface
- Automated reporting
- Logging system
- Unit testing
- Docker support

---

# 📌 Internship Information

**Organization:** Cantilever

**Program:** Cybersecurity Internship

**Task:** Task 4 — WHOIS Domain Information Checker

**Category:** Cybersecurity / Reconnaissance Utility

---

# 👨‍💻 Author

**Krishna Vamshi**

GitHub:

https://github.com/kv237

---

# 📜 Disclaimer

This project is intended for **educational and authorized cybersecurity purposes only**.

WHOIS information should be used responsibly and in accordance with applicable laws, policies, and terms of service.

---

## 📄 License

This project was developed for educational and internship purposes.
