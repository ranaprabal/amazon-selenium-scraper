# Amazon Selenium Scraper

This repository contains a Python script that uses Selenium to scrape product information from Amazon India. The script searches for "LG Soundbar" and retrieves the product names and prices, then sorts the results by price.

## Requirements

- Python 3.x
- Selenium
- Google Chrome
- ChromeDriver

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ranaprabal/amazon-selenium-scraper.git
   cd amazon-selenium-scraper
   ```

2. **Install dependencies:**

   Use `pip` to install the required Python packages:

   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver:**

   - Ensure you have Google Chrome installed.
   - Download from google official website

4. **Run the script:**

   ```bash
   python contlo_amazon_scraper.py
   ```

   The script will open a Chrome browser, navigate to Amazon India, perform a search for "LG Soundbar", and print a list of products with their prices.

## Usage

This script is a simple example of using Selenium for web scraping and automation. You can modify the search query and the elements being scraped to adapt it for other products or websites.
