import pyautogui
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.marketwatch.com/games/epic-gaymers-class')


elem = browser.find_element(By.NAME, 'p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

screenWidth, screenHeight = pyautogui.size()

# i = 0
# while True:
#     if i % 5000000 == 0:
#         currentMouseX, currentMouseY = pyautogui.position()
#         print(f"{currentMouseX}, {currentMouseY}")
#     i+=1
