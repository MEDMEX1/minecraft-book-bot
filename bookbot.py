import pyperclip
import time
from keyboard import is_pressed
from threading import Thread
import os
import ctypes
import win32api
import win32api as winAPI
import win32con
import keyboard
import pyautogui
import sys

ctypes.windll.kernel32.SetConsoleTitleW("Bl4ckBoy is King")

class App:
    def __init__(self):
        Thread(target = self.main).start()
        Thread(target = self.menu).start()
        Thread(target = self.kill).start()
    
    def kill(self):
        while True:
            time.sleep(0.1)
            if is_pressed("end"):
                os._exit(0)

    def main(self):
        while True:
            time.sleep(0.1)
            if is_pressed("insert"):
                ctypes.windll.user32.mouse_event(0x0008, 0, 0)
                ctypes.windll.user32.mouse_event(0x00010, 0, 0)
                with open("text.txt", 'r+') as f:
                    for i in range(50):
                        pyperclip.copy(f.read(200))
                        time.sleep(0.5)
                        ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)
                        ctypes.windll.user32.keybd_event(0x56, 0, 0, 0)
                        ctypes.windll.user32.keybd_event(0x11, 0, 0x0002, 0)
                        ctypes.windll.user32.keybd_event(0x56, 0, 0x0002, 0)
                        time.sleep(0.1)
                        pyautogui.click(1067, 500)

    def menu(self):
        print("press insert to start")
        print("press end to stop")

App()
