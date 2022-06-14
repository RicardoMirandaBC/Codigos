from functools import partial
from tkinter import *
import pyautogui as pg
import time
import clipboard as cb
import tkinter.font as font
import os
import subprocess

def Comandos(modelo):
    try:
        os.system("taskkill /f /im winword.exe /t")
    except:
        print('nah')
    
    subprocess.Popen(['C:\\Program Files\\Microsoft Office\\root\\Office16\\winword.exe', '-new-tab'])
    
    copiar = cb.copy('Z:\Marketing\TEMPLATES\RODAPÉ E CABEÇALHO')
    
    time.sleep(2)
    
    pg.hotkey('Enter')
    time.sleep(0.30)
    
    pg.hotkey('Alt')
    time.sleep(0.30)
    
    pg.hotkey('D')
    time.sleep(0.30)
    
    pg.hotkey('M')
    time.sleep(0.30)
    
    pg.hotkey('P')
    time.sleep(0.30)
    
    pg.hotkey('Down')
    time.sleep(0.30)
    
    pg.hotkey('Tab')
    time.sleep(0.30)
    
    pg.hotkey('Enter')
    time.sleep(0.60)
    
    for i in range (3):
        pg.hotkey('Tab')
        time.sleep(0.15)
        i = i + 1
    
    pg.hotkey('Enter')
    time.sleep(0.70)
    
    pg.keyDown('Ctrl')
    pg.press('l')
    pg.keyUp('Ctrl')
    time.sleep(0.30)
    
    pg.hotkey('Ctrl','V')
    time.sleep(0.30)
    
    pg.hotkey('Enter')
    time.sleep(0.30)
    
    for i in range (4):
        pg.hotkey('Tab')
        time.sleep(0.30)
        i = i + 1
    
    pg.hotkey('Space')
    time.sleep(0.20)
    
    if (modelo == 2):
        pg.hotkey('Down')
        time.sleep(0.20)
    
    pg.hotkey('Enter')
    time.sleep(0.30)
    
    for i in range (5):
        pg.hotkey('Down')
        time.sleep(0.20)
        i = i + 1
    
    pg.hotkey('Enter')
    time.sleep(0.30)
    
    pg.hotkey('Tab')
    time.sleep(0.30)
    
    pg.hotkey('Space')
    time.sleep(0.30)
    
    pg.hotkey('Enter')
    time.sleep(0.30)
    
    pg.hotkey('Alt')
    time.sleep(0.30)
    
    pg.hotkey('T')
    time.sleep(0.30)
    
    pg.hotkey('A','C')
    time.sleep(0.30)
    
    pg.hotkey('Enter')
    time.sleep(0.30)
    
    pg.hotkey('Delete')
    time.sleep(0.30)
    
    pg.hotkey('Alt')
    time.sleep(0.30)
    
    pg.hotkey('C')
    time.sleep(0.30)
    
    pg.hotkey('S','N')
    time.sleep(0.30)
    
    pg.hotkey('E')
    time.sleep(0.30)
    
    for i in range (2):
        pg.hotkey('Tab')
        time.sleep(0.30)
        i = i + 1
    
    pg.hotkey('Enter')
    time.sleep(0.30)
    
    pg.hotkey('Alt')
    time.sleep(0.30)
    
    pg.hotkey('D')
    time.sleep(0.30)
    
    pg.hotkey('M')
    time.sleep(0.30)
    
    pg.hotkey('S')
    time.sleep(0.30)
    
    if (modelo == 1):
        copiar = cb.copy('Padrão Lobe 1')
    
    else :
        copiar = cb.copy('Padrão Lobe 2')
    
    pg.hotkey('Ctrl','V')
    time.sleep(0.30)
    
    for i in range (2):
        pg.hotkey('Tab')
        time.sleep(0.30)
        i = i + 1
    
    for i in range (3):
        pg.hotkey('Up')
        time.sleep(0.20)
        i = i + 1

    pg.hotkey('Enter')
    time.sleep(0.30)
    
    for i in range (2):
        pg.hotkey('Tab')
        time.sleep(0.30)
        i = i + 1
    
    for i in range (2):
        pg.hotkey('Up')
        time.sleep(0.20)
        i = i + 1
    
    for i in range (4):
        pg.hotkey('Enter')
        time.sleep(0.30)
        i = i + 1
    
    pg.hotkey('Alt')
    time.sleep(0.30)
    
    pg.hotkey('J','H')
    time.sleep(0.30)
    
    pg.hotkey('H')
    time.sleep(0.30)
    
    modelo = modelo + 1
    
    if (modelo > 2):
        return
    else:
        Comandos(modelo)

def Tela():
    
    Button(text='Iniciar', bg='white', fg='black', command=partial(Comandos,1)).place(x=45, y=80, width=130, height=30)

app = Tk()
var = StringVar()
app.title('')
app.geometry("210x200")
app.configure(bg='gray')

fonte = font.Font(size = 20)

Tela()

app.mainloop()