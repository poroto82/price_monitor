# Walmart Price Scraper

![Scrapy](https://img.shields.io/badge/Scrapy-2.5.1-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.8-blue.svg)

## Description

This project is a Walmart and Amazon product price scraper using the Scrapy library in Python. The scraper is configured to extract product information, including title, price, and product link. Additionally, it uses proxies and User-Agent rotation to avoid IP blocks and restrictions.

## Features

- **Product data extraction from Walmart**: Title, price, and link.
- **Product data extraction from Amazon**: Title, price, and link.
- **Proxy support**: Uses a list of proxies to make requests.
- **User-Agent rotation**: Changes the User-Agent on each request to avoid being blocked.

## Requirements

- Python 3.8 or higher
- Scrapy 2.5.1

## Installation

1. Clone the repository:

2. Create a virtual environment and install the dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Add your proxies to the list in `settings.py`:

    ```python
    # settings.py
    PROXY_LIST = [
        'http://your_proxy_1:port',
        'http://your_proxy_2:port',
        'http://your_proxy_3:port',
    ]
    ```

## Usage

To run the spider and save the data to a JSON file, use the following command:

```bash
scrapy crawl walmart -o products.json
```
