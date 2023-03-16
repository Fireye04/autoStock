import pyautogui

screenWidth, screenHeight = pyautogui.size()

i = 0
while True:
    if i % 5000000 == 0:
        currentMouseX, currentMouseY = pyautogui.position()
        print(f"{currentMouseX}, {currentMouseY}")
    i+=1
