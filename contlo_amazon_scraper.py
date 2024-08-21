from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    browser.get("https://www.amazon.in/")

    searchInput = browser.find_element(By.ID, "twotabsearchtextbox")
    searchInput.send_keys("lg soundbar")
    searchInput.submit()


    time.sleep(3)


    productList = []
    searchResult = browser.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")

    for result in searchResult:
        try:
            productTitleArray = result.find_element(By.CSS_SELECTOR, "h2 a span").text
            
            

            productPrice = result.find_element(By.CSS_SELECTOR, ".a-price-whole").text
            
            cleanPrice = productPrice.replace(",", "")
            price = int(cleanPrice)
            
            productList.append(((productTitleArray.split(","))[0], price))
        except Exception:
            continue

    productList.sort(key=lambda x: x[1])

    for title, price in productList:
        print(f"{title} - Rs.{price}\n")
    
finally:
    browser.quit()
