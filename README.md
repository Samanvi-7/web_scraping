## Web Scraping Application
This Python application uses Selenium to scrape product details from a website. It retrieves product names, original prices, discounted prices, and discounts where available.

## Requirements

- Python3
- Selenium 4
- Chrome WebDriver

## Installation

1. **Clone the repository:**

   ```bash
   git clone <https://github.com/Samanvi-7/web_scraping.git>
   cd <web_scraping>
    ```
2. **Install Dependencies:**

- Creating virtual environment
    ```
    pip install selenium
    ```

## Chrome WebDriver

To run this application, you need to download and configure Chrome WebDriver, which allows Selenium to interface with the Chrome browser. Follow these steps to set it up:

1. **Check your Chrome browser version:**
   - Open Chrome and go to `chrome://settings/help`.
   - Note down your Chrome version number.

2. **Download Chrome WebDriver:**
   - Visit the [Chrome WebDriver download page](https://developer.chrome.com/docs/chromedriver/downloads).
   - Download the WebDriver version that matches your Chrome browser version.

3. **Setup WebDriver:**
   - Extract the downloaded WebDriver executable (`chromedriver`) to a directory.
   - Add the directory containing `chromedriver` to your system's PATH environment variable. This step allows you to run `chromedriver` from any location in your terminal or command prompt.

4. **Verify installation:**
   - Open a terminal or command prompt.
   - Type `chromedriver --version` and press Enter. You should see the WebDriver version printed, confirming it's correctly set up.

5. **Configure in your code:**
   - In your Python script (`main.py`), specify the path to `chromedriver` where you initialize the WebDriver:
     ```python
     path = "/path/to/chromedriver"  # Update with your actual path
     service = Service(executable_path=path)
     driver = webdriver.Chrome(service=service)
     ```

6. **Run your application:**
   - Execute your Python script (`main.py`) to start scraping product details from the specified website using Chrome WebDriver.



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License 

Distributed under the MIT License. See [MIT](https://choosealicense.com/licenses/mit/) for more information.
    

