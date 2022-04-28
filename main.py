# -*- coding: utf-8 -*-
import win32gui
import win32api
import time

def main():
    hwndMain = win32gui.FindWindow(None, "No Man's Sky")
    while True:
        time.sleep(1)
        if hwndMain:
            if hwndMain != win32gui.GetForegroundWindow():
                win32api.PostMessage(hwndMain, 0x06, 1, 0)
        else:
            quit()

if __name__ == '__main__':
    main()
