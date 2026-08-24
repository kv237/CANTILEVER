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

# ✨ Features

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

# 🛠️ Technologies Used

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

# 📁 Project Structure

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
