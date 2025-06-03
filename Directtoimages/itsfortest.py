import cv2
from playsound import playsound
import pyautogui
import threading

def play_sound():
    playsound('')

img = cv2.imread('')

screen_width, screen_height = pyautogui.size()
resized_img = cv2.resize(img, (screen_width, screen_height), interpolation=cv2.INTER_AREA)

cv2.namedWindow('wompwomp', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('wompwomp', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

threading.Thread(target=play_sound, daemon=True).start()

cv2.imshow('wompwomp', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
