import csv
import re

import pandas as pd
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By

reference_products = []
product_description = []
product_prices = []
availabilities = []
images_sources = []

try:
    url = "https://www.tunisianet.com.tn/596-smartphone-mobile-4g-tunisie"
    driver = webdriver.Firefox(executable_path=r'/home/hosni/Downloads/geckodriver/geckodriver')
    driver.get(url)
    reference_product = driver.find_elements_by_class_name("product-reference")
    description_product = driver.find_elements_by_class_name("product-short-description")
    price_product = driver.find_elements_by_class_name("price")
    availability = driver.find_elements_by_class_name("in-stock")
    image_sources = driver.find_elements(By.TAG_NAME, "img")
    for i in image_sources:
        images_sources.append(i.get_attribute("alt"))
    for i in reference_product:
        reference_products.append(i.text)
    for j in description_product:
        product_description.append(j.text)
    for k in price_product:
        product_prices.append(k.text)
    for l in availability:
        availabilities.append(l.text)
except Exception as e:
    pass

print("Reference_Products", len(reference_products))
print("Product_Description", len(product_description))
print("Product_Price", len(product_prices))
print("Disponibility", len(availabilities))
s1 = pd.Series(reference_products, name='Reference_Product')
s2 = pd.Series(product_description, name='Product_Desciption')
s3 = pd.Series(product_prices, name="Product_Price")
s4 = pd.Series(availabilities, name="Disponibility")
df = pd.concat([s1, s2, s3, s4], axis=1)
df.to_csv("Tunisianet_Smatphone.csv")