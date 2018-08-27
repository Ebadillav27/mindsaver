import PySimpleGUI as sg
import time
import os

starter = 0
mins = 00
max_time = 25
form = sg.FlexForm('Mindsaver', auto_size_text=True)
output_element = sg.Text('', size=(8, 2), font=('Helvetica', 20))

form_rows = [[sg.Text('Tiempo transcurrido desde el inicio del programa (la computadora se bloqueara cuando llegue a {} minutos'.format(max_time))],
             [output_element],
             [sg.SimpleButton('Cerrar')]]

form.LayoutAndRead(form_rows, non_blocking=True)



while mins <= max_time:
    output_element.Update('{:02d}:{:02d}'.format(mins, starter))
    button, values = form.ReadNonBlocking()
    starter += 1
    if values is None or button == 'Cerrar':
        break
    time.sleep(1)
    if starter % 60 == 0:
        starter = 0 
        mins += 1 
    if mins == max_time:
        output_element.Update("H3LL0 FR13ND")
        for i in range(0,15):
            os.system("rundll32.exe user32.dll, LockWorkStation")
            time.sleep(1)
        mins = 0



else:
    form.CloseNonBlockingForm()
