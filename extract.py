import requests
import xml.etree.ElementTree as ET
import pandas as pd

def get_sitemap_urls(sitemap_index_url):
    response = requests.get(sitemap_index_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the sitemap index. Status code: {response.status_code}")

    sitemap_urls = []
    root = ET.fromstring(response.content)
    for sitemap in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap"):
        sitemap_loc = sitemap.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
        sitemap_urls.append(sitemap_loc)

    return sitemap_urls

def process_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    if response.status_code != 200:
        print(f"Error processing sitemap: {sitemap_url} - Status code: {response.status_code}")
        return []

    urls = []
    root = ET.fromstring(response.content)
    for url_elem in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
        url_loc = url_elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
        urls.append(url_loc)

    return urls

sitemap_index_url = "https://example.com/sitemap_index.xml"  # Replace with the URL of your sitemap index
sitemap_urls = get_sitemap_urls(sitemap_index_url)

# Create a list to store URLs from individual sitemaps
all_urls = []

for sitemap_url in sitemap_urls:
    urls = process_sitemap(sitemap_url)
    all_urls.extend(urls)

# Check if there are URLs to create DataFrame
if all_urls:
    df_all = pd.DataFrame({"url": all_urls})
    # Save the extracted URLs to a CSV file
    df_all.to_csv('sitemap_urls.csv', index=False)
else:
    print("No valid sitemap URLs were processed.")
