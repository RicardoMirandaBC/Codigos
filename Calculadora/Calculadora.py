import os
import sys
from cgitb import text
from functools import partial
from glob import glob
from tkinter import *

# declaracao de variaveis globais
numeros = [0,0,0,0,0,0,0,0,0,0]
operacoes = ['','','','','','','','','','']
situacao = 0

#Criação da tela
def Tela():
    
    #Botoes numerais
    i = 1
    espaco_y = 0
    espaco_x = 0
    
    while i < 11:
        
        j = i
        
        if(j == 10):
            j = 0
            espaco_x = 100
        
        Button(text=j, bg='white', fg='black', command=partial(Distinguir,j)).place(x=10+espaco_x, y=130+espaco_y, width=100, height=100)
        
        espaco_x = espaco_x + 100

        if (j % 3 == 0):
            espaco_y = espaco_y + 110
            espaco_x = espaco_x - espaco_x
        i = i + 1
    
    #Botoes operacionais
    operacoes = ['+', '-', '*', '/', '=']
    i = 0
    espaco_y = 0
    espaco_x = 0
    for op in operacoes:
        
        if(op == '='):
            espaco_x = 110
            espaco_y = 110
        
        Button(text=op, bg='white', fg='black', command=partial(Distinguir,op)).place(x=320 - espaco_x, y=130+(i*110) - espaco_y, width=100, height=100)
        
        i = i + 1
        
    #Botao Clear
    Button(text='Clear', bg='white', fg='black', command=partial(Restart)).place(x=10, y=460, width=100, height=100)
    
    return

#Restaura o programa
def Restart():
        
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
#Separa numeros de operacoes
def Distinguir(var):

    if(numeros[0] == 0):
        caixa.delete(0,'end')
    caixa.insert('end',var)
    if(str(var) == '='):
        Calcular()			
    if(str(var).isnumeric()):
        Mesclar_valor(var)
    else:
        Mesclar_operacao(var)
    return

#Guarda os numeros em um array
def Mesclar_valor(var):
    global situacao
    contador = 0
    if(numeros[0] == 0):
        numeros[contador] = var
        situacao = 1
        return
        
    while(contador < 10):
        
        if(numeros[contador] == 0):
            if (situacao == 1):
                
                numeros[contador-1] = int(str(numeros[contador-1])+str(var))
                print(numeros[contador-1])
                return
            numeros[contador] = var
            situacao = 1
            return
        contador = contador + 1

             
#Guarda as operacoes em um array
def Mesclar_operacao(var):
    global situacao
    contador = 0
    
    if(operacoes[0] == ""):
        operacoes[0] = var
        situacao = 0
        return
        
    while(contador < 10):
        if(operacoes[contador] == ""):
            operacoes[contador] = var
            situacao = 0
            return
        contador = contador + 1
        

#Recebe os vetores e realiza a conta        
def Calcular():
    global numeros
    global operacoes
    global situacao
    contador = 0
    resultado = 0
    
    while(operacoes[contador] != ""):
        if(operacoes[contador] == '+'):
            resultado = numeros[contador] + numeros[contador+1]
            
        if(operacoes[contador] == '-'):
            resultado = numeros[contador] - numeros[contador+1]
		
        if(operacoes[contador] == '*'):
            resultado = numeros[contador] * numeros[contador+1]
        
        if(operacoes[contador] == '/'):
            resultado = numeros[contador] / numeros[contador+1]
        
        contador = contador + 1   
                
    print(resultado)
    caixa.delete(0,'end')
    caixa.insert(1,resultado)
    numeros = [0,0,0,0,0,0,0,0,0,0]
    operacoes = ['','','','','','','','','','']
    situacao = 0
    return

app = Tk()
var = StringVar()
app.title('Calculadora')
app.geometry("430x570")
app.configure(bg='gray')
caixa = Entry(app)
caixa.place(x = 10,y = 10,width=410, height=100)

Tela()

app.mainloop()