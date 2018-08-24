import os
import PySimpleGUI as sg 
import time 

#cmd: rundll32.exe user32.dll, LockWorkStation

starter = 0 
max_time = 25 

os.system("rundll32.exe user32.dll, LockWorkStation")