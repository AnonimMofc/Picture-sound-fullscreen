#                                           +++++  Для прекращения нужно нажать ЛЮБУЮ кнопку на клавиатуре 
#                                           +++++  To stop you must press ANY button on keyboard

import cv2
from playsound import playsound
import pyautogui
import threading

def play_sound():
    playsound('negrimolosi.mp3') # Название звуквой дорожки + формат(smth.mp3/smth.wav)   |||  Name of sound + format(smth.mp3/smth.wav)

img = cv2.imread('badbad.mp3') # Название картинки + формат(smth.jpg и т.д.)   ||| Name of pic + format(smth.jpg etc.)

screen_width, screen_height = pyautogui.size()
resized_img = cv2.resize(img, (screen_width, screen_height), interpolation=cv2.INTER_AREA)

cv2.namedWindow('wompwomp', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('wompwomp', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

threading.Thread(target=play_sound, daemon=True).start()

cv2.imshow('wompwomp', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
