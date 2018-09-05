import PySimpleGUI as sg
import time
import subprocess
import textwrap

starter = 0
mins = 00
max_time = 25
form = sg.FlexForm('Mindsaver')

form_rows = [[sg.Text(textwrap.fill('Tiempo transcurrido desde el inicio del programa (la computadora se bloqueara cuando llegue a {} minutos)'.format(max_time), 40), size=(30,3))],
             [sg.Text('', size=(8, 2), font=('Helvetica', 20), key='output')],
             [sg.SimpleButton('Cerrar')]]

form.LayoutAndRead(form_rows, non_blocking=True)

while mins <= max_time:
    form.FindElement('output').Update('{:02d}:{:02d}'.format(mins, starter))
    button, values = form.ReadNonBlocking()
    starter += 1
    if values is None or button == 'Cerrar':
        break
    time.sleep(1)
    if starter % 60 == 0:
        starter = 0 
        mins += 1 
    if mins == max_time:
        form.FindElement('output').Update("H3LL0 FR13ND")
        for i in range(0,15):
            subprocess.call("rundll32.exe user32.dll, LockWorkStation", shell = False)
            time.sleep(1)
        mins = 0
else:
    form.CloseNonBlockingForm()
