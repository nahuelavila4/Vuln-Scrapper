# Vulnerability Scraper

This project is a Python-based web scraper for gathering security vulnerability data from the National Vulnerability Database (NVD) and storing it in an SQLite database.

## Features

- Scrapes vulnerability information, including:
  - Vulnerability ID (CVE)
  - Description
  - Publication date
- Filters out duplicate entries on re-run
- Stores data in an SQLite database for easy querying and access

## Prerequisites

- Python 3.x
- Required packages: `requests`, `beautifulsoup4`, `sqlite3`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Data Usage Disclaimer

This project scrapes data from the [National Vulnerability Database (NVD)](https://nvd.nist.gov/), maintained by the National Institute of Standards and Technology (NIST). The data is publicly accessible, but users should comply with NIST’s [data usage policies](https://www.nist.gov/open/license). This project does not claim ownership of the data and is intended for educational and research purposes only.
