import pyautogui as au
from time import sleep

def dislike():
  coords = au.locateCenterOnScreen('img/dark_dislike.png', confidence=0.9)
  if coords == None:
    l_coords = au.locateCenterOnScreen('img/light_dislike.png', confidence=0.9)
    if l_coords == None:
      try:
        raise ValueError('Dislike button not found')
      except:
        return "Unsuccesful"
    coords = l_coords
  au.moveTo(*coords)
  au.click()
  return "Succesfully disliked."

while True:
  print(dislike())
  sleep(0.5)