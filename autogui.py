import pyautogui

# for i in range(3):
# 	pyautogui.moveTo(100,100,duration=0.9)
# 	pyautogui.moveTo(200,100,duration=0.9)
# 	pyautogui.moveTo(300,100,duration=0.9)
# 	pyautogui.moveTo(400,100,duration=0.9)
# 	pyautogui.moveTo(500,100,duration=0.9)
# 	pyautogui.moveTo(600,100,duration=0.9)
# 	pyautogui.moveTo(700,100,duration=0.9)
# 	pyautogui.moveTo(800,100,duration=0.9)
# 	pyautogui.moveTo(900,100,duration=0.9)


def zero_to_infinity():
    i = 0
    while True:
        yield i
        i += 1

for x in zero_to_infinity():
	pyautogui.moveTo(100,100,duration=0.9)
	pyautogui.moveTo(200,300,duration=0.9)
	pyautogui.moveTo(300,200,duration=0.9)
	pyautogui.moveTo(400,700,duration=0.9)
	pyautogui.moveTo(500,800,duration=0.9)
	pyautogui.moveTo(600,100,duration=0.9)
	pyautogui.moveTo(700,100,duration=0.9)
	pyautogui.moveTo(800,100,duration=0.9)
	pyautogui.moveTo(900,100,duration=0.9)