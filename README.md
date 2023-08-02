# Python Sitemap Extractor

This Python script is designed to extract URLs from a sitemap index file and individual sitemap files. It utilizes the `requests` library to fetch the sitemap files and `xml.etree.ElementTree` for parsing the XML content. The extracted URLs are then saved to a CSV file using `pandas`.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `requests` library (You can install it using `pip install requests`)
- `pandas` library (You can install it using `pip install pandas`)

## Usage

1. Replace the `sitemap_index_url` variable with the URL of your sitemap index. The sitemap index should contain references to individual sitemap files.
   ```python
   sitemap_index_url = "https://example.com/sitemap_index.xml"  # Replace with the URL of your sitemap index
Run the script using Python:
Copy code
python extract.py
How it works
The script performs the following steps:

Fetch the sitemap index using get_sitemap_urls function:

The function sends an HTTP request to the specified sitemap index URL.
It checks the HTTP response status code to ensure a successful fetch (status code 200).
If successful, it parses the XML content of the sitemap index using xml.etree.ElementTree.
The function then extracts the URLs of individual sitemap files and returns them as a list.
Process each individual sitemap using process_sitemap function:

For each sitemap URL obtained from the sitemap index, the function sends an HTTP request.
It checks the HTTP response status code to ensure a successful fetch (status code 200).
If successful, it parses the XML content of the sitemap using xml.etree.ElementTree.
The function extracts the URLs of individual webpages from the sitemap and returns them as a list.
Concatenate all URLs from individual sitemaps:

The script initializes an empty list called all_urls.
It iterates through the list of sitemap URLs obtained from the sitemap index.
For each sitemap URL, it calls process_sitemap to extract the URLs of webpages.
The extracted URLs are added to the all_urls list.
Create a DataFrame and save URLs to a CSV file:

If there are URLs extracted from the sitemaps (i.e., the all_urls list is not empty), the script creates a pandas DataFrame.
The DataFrame is created with a single column "url," containing all the extracted URLs.
Finally, the DataFrame is saved to a CSV file named "sitemap_urls.csv" in the script's working directory.
If no valid sitemap URLs are processed or there are no URLs in the sitemaps, the script displays a message indicating so.

Please make sure that you have the necessary permissions to fetch and process the sitemap files from the provided URL.
