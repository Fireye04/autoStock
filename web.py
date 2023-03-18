import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pickle
import time

browser = webdriver.Firefox()


def delay(duration):
    for i in range(duration):
        print(i + 1)
        time.sleep(1)

    print("\n")


def login(email: str, password: str):
    browser.get('https://www.marketwatch.com/games/epic-gaymers-class')

    # wait for page loading
    delay(5)

    elem = browser.find_element(By.CLASS_NAME, 'close-btn')  # Find the search box
    elem.click()

    loginfo = browser.find_element(By.CLASS_NAME, "profile.logged-out")
    loginfo.click()

    loginfo = browser.find_element(By.LINK_TEXT, "Log In")
    loginfo.click()

    delay(5)

    typeBox = browser.find_element(By.ID, "username")
    typeBox.send_keys(email)

    nextButton = browser.find_element(By.CLASS_NAME, "solid-button.continue-submit.new-design")
    nextButton.click()

    delay(3)

    typeBox = browser.find_element(By.ID, "password-login-password")
    typeBox.send_keys(password)

    nextButton = browser.find_element(By.CLASS_NAME, "solid-button.new-design.basic-login-submit")
    nextButton.click()

# uncomment this to change the acting email and password
#
# info = ["email", "password"]
# with open("info.p", "wb") as data:
#     pickle.dump(info, data)


with open("info.p", "rb") as data:
    info = pickle.load(data)

login(info[0], info[1])

# screenWidth, screenHeight = pyautogui.size()
# i = 0
# while True:
#     if i % 5000000 == 0:
#         currentMouseX, currentMouseY = pyautogui.position()
#         print(f"{currentMouseX}, {currentMouseY}")
#     i+=1
