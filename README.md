# Zillow Data Extractor

This script extracts rental listings (address, price, and property link) from a Zillow webpage and adds an entry to a Google Sheet by submitting each entry into a Google Form.

### What the Script Does

* Sends a request to a Zillow webpage

* Scrapes:

  * Listing URLs
  * Property addresses
  * Rental prices

* Opens Google Form using Selenium

* Automatically fills and submits form data for each scraped listing

* Repeats until all rows are submitted

### Requirements
Python 3.9+ recommended

Install dependencies: `pip install -r requirements.txt`

### Running the Script
`python main.py`


### Notes
* Form fields are: Address, Price Per Month, Link
* This script submits actual Google Forms — avoid testing on real/final forms unless intended
* Add time.sleep() delays if your internet is slow as Selenium may lag
* Use custom headers to avoid some anti-scraping filters
_This script might not work if Zillow changes website structure!_
