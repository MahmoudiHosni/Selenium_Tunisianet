import csv
import re

import pandas as pd
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By

reference_products = []
descriptions = []
prices = []
stocks = []
offres = []
marques = []
images = []

try:
    url = "https://www.tunisianet.com.tn/301-pc-portable-tunisie"
    driver = webdriver.Firefox(executable_path=r'/home/hosni/Downloads/geckodriver/geckodriver')
    driver.get(url)
    driver.fullscreen_window()
    reference_product = driver.find_elements(By.XPATH, "//article/div/h2/a")
    desc = driver.find_elements(By.XPATH, "//div/div/a/p")
    price = driver.find_elements(By.CLASS_NAME, "price")
    stock = driver.find_elements(By.XPATH, "//article/div/div/div/span")
    offre = driver.find_elements(By.XPATH, "//article/div/div/a/p/span/strong")
    marque = driver.find_elements(By.XPATH, "//article/div/div/div/a/img")
    image = driver.find_elements(By.XPATH, "//article/div/a/img")
    for i in image:
        images.append(i.get_attribute("data-full-size-image-url"))
    for i in marque:
        marques.append(i.get_attribute("alt"))
    for i in offre:
        offres.append(i.text)
    for i in stock:
        stocks.append(i.text)
    for i in price:
        prices.append(i.text)
    for i in reference_product:
        reference_products.append(i.text)
    for i in desc:
        descriptions.append(i.text)

except Exception as e:
    pass

print("Reference_Products", len(reference_products))
print("Description", len(descriptions))
print("Prices", len(prices))
print("Availability", len(stocks))
print("Marque", len(marques))
print("Offre", len(offres))
print("Image_Url", len(images))

s1 = pd.Series(reference_products, name='Reference_Product')
s2 = pd.Series(descriptions, name='Description')
s3 = pd.Series(prices, name='Price')
s31 = pd.Series(stocks, name='Availability')
s4 = pd.Series(marques, name='Marque')
s5 = pd.Series(offres, name='Offre')
s6 = pd.Series(images, name='Image_URL')
df = pd.concat([s1, s2, s3, s31, s4, s5, s6], axis=1)
df.to_csv("Tunisianet_Smatphone.csv")