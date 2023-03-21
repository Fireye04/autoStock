from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# haha poopy haha so funny amogus im so funny hahahhaahhaahha
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


def login(website='https://www.marketwatch.com/games/epic-gaymers-class') -> bool:
    try:
        browser.get(website)

        # wait for page loading
        delay(5)
        elem = browser.find_element(By.CLASS_NAME, 'close-btn')  # Find the search box
        # elem.send_keys(Keys.RETURN)
        elem.click()

        loginfo = browser.find_element(By.CLASS_NAME, "profile.logged-out")
        loginfo.click()

        loginfo = browser.find_element(By.LINK_TEXT, "Log In")
        loginfo.click()

        delay(1)

        typeBox = browser.find_element(By.ID, "username")
        typeBox.send_keys(email)

        nextButton = browser.find_element(By.CLASS_NAME, "solid-button.continue-submit.new-design")
        nextButton.click()

        delay(1)

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


def updateStats(site='https://www.marketwatch.com/games/epic-gaymers-class'):
    if not login(site):
        return

    delay(3)

    browser.get(site + "/portfolio")

    delay(3)

    lisst = browser.find_element(By.CLASS_NAME, "table.table--secondary.holdings")
    body = lisst.find_element_by_tag_name("tbody")
    holdings = body.find_elements_by_tag_name("tr")

    stonks = []
    for hold in holdings:
        stonks.append(hold.text)

    stats = []

    for stonk in stonks:
        s = stonk.split("\n")
        stats.append(s)

    # Ticker, Shares owned, Type (buy/short), current share price, $change, %change, $ value, total value $change/%change
    print(stats)

    inp = input("Quit? ")
    if inp == "y":
        browser.quit()


updateStats("https://www.marketwatch.com/games/tgseblock")
