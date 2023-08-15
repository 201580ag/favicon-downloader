# favicon-downloader
This repository is a simple tool for downloading a website's favicon using Python. When the user enters the website address or .txt file path, the Web sites' Fabicon is downloaded and saved through the Google Fabicon service.

# Favicon Downloader

Favicon Downloader is a simple tool that allows you to download favicons from websites using Python. It can process individual website addresses or a list of addresses from a .txt file.

## Usage

### Prerequisites

Before using Favicon Downloader, make sure you have Python installed on your system.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/201580ag/favicon-downloader.git
   ```

2. Navigate to the repository's directory:

   ```bash
   cd favicon-downloader
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install requests
   ```

### How to Use

1. Run the script by executing the following command:

   ```bash
   python favicon_downloader.py
   ```

2. You will be prompted to enter a website address or the path to a .txt file containing a list of website addresses.

   - If you provide a website address, the script will download the favicon for that website.
   - If you provide a .txt file, the script will read each line (website address) and download the corresponding favicons.

3. The downloaded favicon icons will be saved in the 'favicon' folder within the repository.
