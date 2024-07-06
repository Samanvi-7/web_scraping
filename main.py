from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd 
import os

web='https://www.kindlife.in/on-the-body/skincare-en-3/eye-care-en/'

path="/Users/samanvithota/Desktop/web_scraping/chromedriver"
service=Service(executable_path=path)

driver=webdriver.Chrome(service=service)
driver.get(web)


wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="page_content_"]')))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)  # Give time for content to load

products = driver.find_elements(By.CLASS_NAME, "bk-product-list")
print(f"Found {len(products)} products")

product_data = [ ]

for product in products:
    try:
        title = product.find_element(By.CLASS_NAME, "product-title").text
        price = product.find_element(By.CLASS_NAME, "bk-product-list__price").text
    
        # Split the price text
        price_details = price.split("\n")
        if len(price_details) == 3:
            discounted_price = price_details[0]
            original_price = price_details[1]
            discount = price_details[2]
        elif len(price_details) == 2:
            discounted_price = price_details[0]
            original_price = price_details[1]
            discount = "N/A"
        else:
            discounted_price = price_details[0]
            original_price = "N/A"
            discount = "N/A"
        
        print(f"Product name: {title}\n Original Price: {original_price}\n Discounted Price: {discounted_price}\n Discount: {discount}\n ")

        product_data.append({
            'Title': title,
            'Original_price': original_price,
            'Discounted_price': discounted_price,
            'Discount': discount
        })

    except Exception as e:
        print(f"Error extracting product details: {e}")


driver.quit()

df=pd.DataFrame(product_data)
csv_path='/Users/samanvithota/Desktop/web_scraping/product_data.csv'
os.makedirs(os.path.dirname(csv_path),exist_ok=True)
df.to_csv(csv_path,index=False)

