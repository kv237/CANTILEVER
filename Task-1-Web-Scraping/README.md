# 📚 Cantilever Cybersecurity Internship — Task 1

## E-Commerce Web Scraping and Product Search

A Python-based web scraping and product search application that collects product information from an e-commerce website, stores the data in CSV format, provides command-line search functionality, and offers a Flask-based web interface.

This project was developed as part of the **Cantilever Cybersecurity Internship**.

---

## 🎯 Objective

The objective of this task is to develop a web scraping application that collects publicly available product information from an e-commerce website and provides users with an easy way to search and view the collected products.

The application extracts:

- Product title
- Product price
- Product rating
- Product description
- Product URL

The collected information is stored in a structured CSV file and can be searched through both the command line and a Flask web interface.

---

# ✨ Features

### 🌐 Web Scraping

The scraper retrieves product information from the **Books to Scrape** website.

It extracts:

- Product title
- Product price
- Product rating
- Product description
- Product URL

---

### 💾 CSV Data Storage

The scraped product information is stored in:

```text
data/products.csv
```

The CSV file provides structured storage for the collected product information.

---

### 🔎 Product Search

The project provides a command-line product search utility.

Users can search for products by entering a product name or keyword.

Example:

```text
Enter product name to search: Sapiens
```

The application displays matching products including:

- Title
- Price
- Rating
- Description

---

### 🖥️ Flask Web Interface

The project also includes a Flask-based web interface.

Users can open the application in a browser and search for products through a graphical interface.

The interface displays:

- Product title
- Price
- Rating
- Description
- Original product page

---

### 🔗 Original Product Links

Each product contains its original product page URL, allowing users to access the source page directly.

---

# 🌐 Website Used

The project uses **Books to Scrape**, a demo website specifically designed for practicing web scraping.

**Website:**

https://books.toscrape.com/

The website provides publicly accessible sample book data for educational web scraping purposes.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Application development |
| Requests | Sending HTTP requests |
| BeautifulSoup4 | HTML parsing and web scraping |
| Pandas | Data processing and CSV generation |
| Flask | Web application |
| HTML | Web interface |
| CSS | Interface styling |
| Git | Version control |
| GitHub | Source code hosting |

---

# 📁 Project Structure

```text
Task-1-Web-Scraping/
│
├── scraper.py
├── search.py
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── products.csv
│
└── templates/
    └── index.html
```

---

# 🔄 Application Workflow

The project follows the workflow below:

```text
                    Books to Scrape
                          │
                          ▼
                  Send HTTP Request
                          │
                          ▼
                    Parse HTML
                          │
                          ▼
                Extract Product Data
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
           Title        Price        Rating
             │
             ▼
       Product Description
             │
             ▼
        Product URL
             │
             ▼
       Store Product Data
             │
             ▼
       data/products.csv
             │
             ▼
       Product Search
             │
        ┌────┴─────┐
        ▼          ▼
   CLI Search   Flask Web App
        │          │
        └────┬─────┘
             ▼
       Display Results
```

---

## Workflow Description

1. **Connect to the website**  
   The scraper sends an HTTP request to Books to Scrape.

2. **Parse the webpage**  
   BeautifulSoup parses the returned HTML content.

3. **Extract product information**  
   Product title, price, rating, description, and URL are extracted.

4. **Process the data**  
   The collected information is organized into structured records.

5. **Generate CSV data**  
   Pandas is used to create and save the product dataset.

6. **Store the data**  
   The final dataset is saved to:

   ```text
   data/products.csv
   ```

7. **Search products**  
   Users can search the collected products using the command-line search utility.

8. **Web interface**  
   The Flask application provides a browser-based interface for searching and viewing products.

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

Clone the main Cantilever repository:

```bash
git clone https://github.com/kv237/CANTILEVER.git
```

---

## 2. Navigate to Task 1

```bash
cd CANTILEVER/Task-1-Web-Scraping
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

at the beginning of the terminal prompt.

### Git Bash

```bash
source venv/Scripts/activate
```

---

## 5. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

The project uses libraries including:

```text
requests
beautifulsoup4
pandas
flask
```

---

# ▶️ Running the Web Scraper

Run:

```bash
python scraper.py
```

The application connects to the website and begins collecting product information.

Example output:

```text
======================================================================
Website connected successfully!
Products found: 20
======================================================================

Scraped: A Light in the Attic
Scraped: Tipping the Velvet
Scraped: Soumission
Scraped: Sharp Objects
Scraped: Sapiens: A Brief History of Humankind
...
Scraped: It's Only the Himalayas

======================================================================
Scraping completed successfully!
Total products: 20
Data saved to: data/products.csv
```

---

# 📊 Generated Dataset

After running the scraper, verify that the CSV file has been created:

```text
data/products.csv
```

The file contains:

```text
Title
Price
Rating
Description
URL
```

---

# 🔍 Running Product Search

Run:

```bash
python search.py
```

The application displays:

```text
============================================================
        PRODUCT SEARCH
============================================================

Enter product name to search:
```

Enter a product name or keyword.

### Example

```text
Enter product name to search: Sapiens
```

Expected output:

```text
Search Results
============================================================
Found 1 product(s):

Title: Sapiens: A Brief History of Humankind
Price: £54.23
Rating: Five
Description: From a renowned historian comes a groundbreaking...
------------------------------------------------------------
```

---

# 🧪 Testing Product Search

## Test 1 — Search for Sapiens

Run:

```bash
python search.py
```

Enter:

```text
Sapiens
```

The application should return:

```text
Sapiens: A Brief History of Humankind
```

---

## Test 2 — Search for "The"

Run:

```bash
python search.py
```

Enter:

```text
The
```

The application should return products whose titles contain the search keyword.

Example results include:

```text
The Requiem Red
The Dirty Little Secrets of Getting Your Dream Job
The Coming Woman
The Boys in the Boat
The Black Maria
```

---

## Test 3 — Search for a Non-Existing Product

Run:

```bash
python search.py
```

Enter a keyword that does not exist in the dataset.

Example:

```text
xyz123
```

The application should display:

```text
No products found.
```

---

# 🌐 Running the Flask Web Application

Start the Flask application:

```bash
python app.py
```

The application should display something similar to:

```text
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
```

---

## 🌍 Open the Web Application

Open a web browser and visit:

```text
http://127.0.0.1:5000
```

The product search interface should appear.

Users can enter a product name and search the collected dataset.

---

# 🖥️ Web Application Features

The Flask interface provides:

- Product search
- Product title
- Product price
- Product rating
- Product description
- Original product page link

For example, searching for:

```text
Sapiens
```

displays:

```text
Sapiens: A Brief History of Humankind

£54.23

⭐ Rating: Five

Product description...

View Product
```

The **View Product** link opens the original product page on Books to Scrape.

---

# 🔍 How to Verify the Results

After running the scraper, verify the generated files.

### Windows Command Prompt

```cmd
dir data
```

Expected:

```text
products.csv
```

### Git Bash

```bash
ls data
```

Expected:

```text
products.csv
```

---

## View the CSV File

### Windows Command Prompt

```cmd
type data\products.csv
```

### Git Bash

```bash
cat data/products.csv
```

The CSV should contain product records with:

```text
Title
Price
Rating
Description
URL
```

---

# 🔄 Complete Testing Process

An evaluator can test the complete project using the following sequence:

### Step 1 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2 — Run the scraper

```bash
python scraper.py
```

### Step 3 — Verify CSV

```bash
dir data
```

or:

```bash
ls data
```

### Step 4 — Test command-line search

```bash
python search.py
```

Search for:

```text
Sapiens
```

### Step 5 — Start Flask

```bash
python app.py
```

### Step 6 — Open browser

Visit:

```text
http://127.0.0.1:5000
```

### Step 7 — Test web search

Search for:

```text
Sapiens
```

The product information and original product link should be displayed.

---

# ❌ Error Handling

The application handles common situations such as:

### Website Connection Failure

If the website cannot be accessed, the scraper reports the HTTP request failure.

### No Search Results

If a product does not exist in the collected dataset:

```text
No products found.
```

### Empty Search

The search application handles empty or invalid search input according to the implemented search logic.

---

# 🔐 Ethical and Security Considerations

This project was developed for educational purposes using **Books to Scrape**, a demo website intended for practicing web scraping.

The application:

- Uses normal HTTP requests.
- Uses a User-Agent header.
- Uses request timeouts.
- Does not attempt to bypass authentication.
- Does not access private information.
- Does not bypass security controls.
- Uses publicly accessible educational data.

---

# 🚀 Future Improvements

Possible future enhancements include:

- Scraping multiple pages automatically
- Category-based filtering
- Price-range filtering
- Rating-based filtering
- Pagination
- Advanced search
- Product sorting
- Database storage
- Improved Flask UI
- Automated testing
- API development
- Docker support
- Deployment to a cloud platform

---

# 📌 Internship Information

**Organization:** Cantilever

**Program:** Cybersecurity Internship

**Task:** Task 1 — E-Commerce Web Scraping and Product Search

**Category:** Web Scraping / Data Processing / Web Application

---

# 👨‍💻 Author

**Krishna Vamshi**

GitHub:

https://github.com/kv237

---

# 📜 Disclaimer

This project is intended for **educational and authorized purposes only**.

The scraper uses the Books to Scrape demonstration website, which is specifically intended for web scraping practice.

Users should always respect the terms of service, robots.txt policies, rate limits, and applicable laws when scraping websites.

---

## 📄 License

This project was developed for educational and internship purposes.
