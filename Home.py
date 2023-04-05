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
        element = WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, 'li#property-font-family.property.opened'))
    except:
        print('brak elementu')
    else:
        print('otwarto')
        wyniki.append('otwiera sie okno listy')
    time.sleep(5)

    wysz = JeszczeWyszukiwanie(driver, wyniki)
    wysz.znajdz()

    driver.close()
    print(tabulate({'\nWyniki bardzo malego testu': wyniki}, headers="keys"))

class JeszczeWyszukiwanie:
    """wyszukiwanie """

    def __init__(self, driver, wyniki):
        self.driver = driver
        self.wyniki = wyniki
        self.driver.maximize_window()

    def znajdz(self):
        self.driver.find_element(By.ID, 'search').send_keys('Arrow Functions')
        time.sleep(5)

        element = self.driver.find_element(By.ID, 'menu-item-8550')
        element.click()
        self.wyniki.append('wynik z klasy wyszukiwanie brak wyników')
        time.sleep(5)


if __name__ == "__main__":
    main()
