import os
import requests
from urllib.parse import urlparse

input_value = (input("Please enter a website address or a path to a .txt file: "))

if input_value.lower().endswith(".txt"):
    with open(input_value, "r") as file:
        websites = [line.strip() for line in file if line.strip()]
else:
    websites = [input_value]

def download_favicon(website):
    parsed_url = urlparse(website)
    host = parsed_url.netloc
    favicon_url = f"https://www.google.com/s2/favicons?domain={host}"
    response = requests.get(favicon_url)
    favicon_data = response.content
    filename = host.replace("www.", "").replace("/", "") + ".ico"
    favicon_path = os.path.join(favicon_folder, filename)
    with open(favicon_path, "wb") as file:
        file.write(favicon_data)
    print(f"Favicon downloaded and saved as {filename} for {host}")

favicon_folder = os.path.join(os.path.dirname(__file__), "favicon")
if not os.path.exists(favicon_folder):
    os.mkdir(favicon_folder)

for website in websites:
    download_favicon(website)