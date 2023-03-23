from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle
import time
import atexit

from tradeType import TradeType


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


def login(browser, email, password,
          website='https://www.marketwatch.com/games/epic-gaymers-class') -> bool:
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
        print(f"LOGIN FAILURE: {e}")
        browser.quit()
        return False


def trade(browser, ticker: str, shares: int, tType: TradeType, email, password,
          site='https://www.marketwatch.com/games/epic-gaymers-class'):
    if not login(browser, email, password, site):
        return False

    try:
        delay(5)

        tickerinp = browser.find_element(By.CLASS_NAME, "input--text.is-search.j-miniTrade")
        tickerinp.send_keys(ticker)

        delay(5)

        stockRet = browser.find_element(By.CLASS_NAME, "table.table--secondary")
        bodu = stockRet.find_element_by_tag_name("tbody")
        ret = bodu.find_element(By.CLASS_NAME, "table__row")
        button = ret.find_element(By.CLASS_NAME, "btn.btn--secondary.j-trade.t-trade")
        browser.execute_script("window.scrollTo(0, 500)")
        delay(1)
        button.click()

        buttonL = browser.find_element(By.CLASS_NAME, "radio__group.full-span")
        buttons = buttonL.find_elements_by_tag_name("li")

        elem = None

        for but in buttons:
            inp = but.find_element_by_tag_name("input")
            dis = inp.get_attribute("disabled")

            if dis and tType.value == but.text:
                raise Exception("Selected trade option is disabled")
            elif not dis and tType.value == but.text:
                elem = but

        if elem is None:
            raise Exception("Trade option not found")

        elem.click()
        delay(1)

        slider = browser.find_element(By.CLASS_NAME, "input--range.j-range-shares")
        maxx = int(slider.get_attribute("max"))

        if shares > maxx:
            shares = maxx
        elif shares < 1:
            shares = 1

        shInput = browser.find_element(By.CLASS_NAME, "input--text.j-number-shares")
        shInput.send_keys(Keys.ARROW_RIGHT + Keys.BACKSPACE + str(shares))

        cont = browser.find_element(By.CLASS_NAME, "btn.btn--primary.j-submit")
        cont.click()

    except Exception as e:
        print(f"TRADE FAILURE: {e}")
        browser.quit()
        return False


def updateStats(browser, email, password, site='https://www.marketwatch.com/games/epic-gaymers-class'):
    if not login(browser, email, password, site):
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

    # Ticker, Shares owned, Type (buy/short), current share price, $change, %change, $ value,
    # total value $change/%change
    print(stats)

    # TODO: Update info.p and user.py to reflect new stats


def getStockPrice(browser, ticker: str, email, password,
                  site='https://www.marketwatch.com/games/epic-gaymers-class'):
    if not login(browser, email, password, site):
        return

    delay(3)

    tickerinp = browser.find_element(By.CLASS_NAME, "input--text.is-search.j-miniTrade")
    tickerinp.send_keys(ticker)

    delay(5)

    stockRet = browser.find_element(By.CLASS_NAME, "table.table--secondary")
    bodu = stockRet.find_element_by_tag_name("tbody")
    ret = bodu.find_element(By.CLASS_NAME, "table__row")
    button = ret.find_element(By.CLASS_NAME, "primary.t-link")
    browser.execute_script("window.scrollTo(0, 500)")
    delay(1)
    button.click()

    el = browser.find_element(By.CLASS_NAME, "value")

    return el.text


def main():
    browser = webdriver.Firefox()

    with open("info.p", "rb") as data:
        info = pickle.load(data)

    userEmail = info[0]
    userPassword = info[1]

    # trade(browser, "INTC", 999, TradeType.SHORT, userEmail, userPassword,
    # "https://www.marketwatch.com/games/bot-testing")

    # updateStats(browser, userEmail, userPassword, "https://www.marketwatch.com/games/tgseblock")

    print(getStockPrice(browser, "INTC", userEmail, userPassword))

    atexit.register(exit_handler)


if __name__ == "__main__":
    main()


def exit_handler(browser):
    browser.quit()
