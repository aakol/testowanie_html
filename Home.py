from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as Stan_elementu
from selenium import webdriver
import time
import os
from tabulate import tabulate
def main():
    wyniki = []
    os.environ['PATH'] += '/usr/bin/safaridriver'
    driver = webdriver.Safari()
    driver.get("https://webkit.org/status/")

    time.sleep(3)
    WebDriverWait
    element = driver.find_element(By.ID, 'menu-item-8550')
    print(element.text)
    element.click()

    time.sleep(3)
    element = driver.find_element(By.CLASS_NAME, 'primary')

    if element.is_displayed():
        print('znaleziono')
        wyniki.append('dziala link menu _____')
    try:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.CLASS_NAME, "primary"))
    except:
        print('brak elementu')
    else:
        print('znaleziono Huraaaa')

    element = driver.find_element(By.ID, 'property-font-family')

    element.click()
    try:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, 'li#property-font-family.property.opened'))
    except:
        print('brak elementu')
    else:
        print('otwarto')
        wyniki.append('otwiera sie okno listy')
    time.sleep(5)
    print(tabulate({'\nWyniki bardzo malego testu': wyniki}, headers="keys"))

if __name__ == "__main__":
    main()

