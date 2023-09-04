import pywhatkit
import time
import pyautogui
import keyboard as k
import pandas as pd
df=pd.read_csv("phone_no.csv")
for i in range(0,20):
    sample=df["phone_no"][i]
    phone="+91"+str(sample)
    message =""
    pywhatkit.sendwhatmsg_instantly(phone, message)
    pyautogui.click(1050, 950)
    time.sleep(5)
    k.press_and_release('enter')
    time.sleep(2)
    k.press_and_release('cmd+w')
    print("MESSAGE SENT TO: ",phone)