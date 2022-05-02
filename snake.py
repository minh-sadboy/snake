import time

import cv2
import mss
import numpy
import pyautogui
from datetime import datetime 
from random import randrange
import threading

def white(monitor):
    img= numpy.array(sct.grab(monitor))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lwr = numpy.array([80, 0, 0])
    upr = numpy.array([179, 255, 146])
    msk = cv2.inRange(hsv, lwr, upr)
    krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
    dlt = cv2.dilate(msk, krn, iterations=5)
    res = 255 - cv2.bitwise_and(dlt, msk)
    cv2.imshow("res", res)

    height, width = msk.shape[:2] 
    num_pixels = height * width 
    count_white = cv2.countNonZero(msk) 
    percent_white = (count_white/num_pixels) * 100 
    percent_white = round(percent_white,2) 
    return percent_white






with mss.mss() as sct:

    # Part of the screen to capture
    monitortop = {"top": 510, "left": 900, "width": 100, "height": 50}
    monitorbottom = {"top": 720, "left": 900, "width": 100, "height": 50}
    monitorleft = {"top": 610, "left": 860, "width": 50, "height": 100}
    monitorright = {"top": 610, "left": 1000, "width": 50, "height": 100}
   

    global direction
    direction = "left"
    while "Screen capturing":
       
        if direction == "top":
            pyautogui.moveTo(950, 330)
            result = white(monitortop)
            if result < 70:
                direction = "left"
                pyautogui.moveTo(330, 655)
                time.sleep(0.3)
                                  


        if direction == "bottom":
            pyautogui.moveTo(950, 970)
            result = white(monitorbottom)
            if result < 70:
               
                direction = "right"
                pyautogui.moveTo(1520, 655)
                time.sleep(0.3)
                        

      
        if direction == "left":
            monitorleft = {"top": 560, "left": 690, "width": 200, "height": 150}    
            pyautogui.moveTo(330, 655)
            result = white(monitorleft)
            if result < 70:               
                direction = "bottom"
                pyautogui.moveTo(950, 970)
                time.sleep(0.3)    
                        
            

        if direction == "right":
            monitorbottom = {"top": 650, "left": 865, "width": 150, "height": 200}    
            pyautogui.moveTo(1520, 655)
            result = white(monitorright)
            if result < 70:
                direction = "top"
                pyautogui.moveTo(950, 330)
                time.sleep(0.3)


        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


