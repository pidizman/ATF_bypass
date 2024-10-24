#TODO: generate .exe via python3 -m PyInstaller main.py --onefile

import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

options = Options()
options.add_experimental_option("detach", True)

def type_text(driver, elements):
    text = ""
    for element in elements:
        text += element.text + ""

    for char in text:
        delay = random.uniform(0.0, 0.8)
        keyboard.write(char)
        time.sleep(delay)

        if driver.find_element(By.ID, "correction").text.startswith("Rychlost"):
            return True

    return False

def repeat_until_success(driver):
    while True:
        elements = driver.find_elements(By.CLASS_NAME, "textLine")
        elements.insert(0, driver.find_element(By.ID, "original"))

        if type_text(driver, elements):
            return True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.maximize_window()
    driver.get("https://www.atfonline.cz/index.php?cat=edu")
    print("Select the text you want to type and press enter")
    input()
    print("You have 5 seconds to switch to the browser")
    time.sleep(5)

    repeat_until_success(driver)

finally:
    print("done")
