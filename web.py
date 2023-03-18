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

    print(" ")

# uncomment this to change the acting email and password
#
# info = ["email", "password"]
# with open("info.p", "wb") as data:
#     pickle.dump(info, data)


with open("info.p", "rb") as data:
    info = pickle.load(data)

email = info[0]
password = info[1]


def login() -> bool:
    try:
        browser.get('https://www.marketwatch.com/games/epic-gaymers-class')

        # wait for page loading
        delay(5)

        elem = browser.find_element(By.CLASS_NAME, 'close-btn')  # Find the search box
        # elem.send_keys(Keys.RETURN)
        elem.click()

        loginfo = browser.find_element(By.CLASS_NAME, "profile.logged-out")
        loginfo.click()

        loginfo = browser.find_element(By.LINK_TEXT, "Log In")
        loginfo.click()

        delay(3)

        typeBox = browser.find_element(By.ID, "username")
        typeBox.send_keys(email)

        nextButton = browser.find_element(By.CLASS_NAME, "solid-button.continue-submit.new-design")
        nextButton.click()

        delay(3)

        typeBox = browser.find_element(By.ID, "password-login-password")
        typeBox.send_keys(password)

        nextButton = browser.find_element(By.CLASS_NAME, "solid-button.new-design.basic-login-submit")
        nextButton.click()

        return True
    except Exception as e:
        print(f"FAILURE: {e}")
        browser.quit()
        return False



def trade():
    if not login():
        return



    inp = input("Quit? ")
    if inp == "y":
        browser.quit()


trade()
