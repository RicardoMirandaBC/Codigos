import os
from tkinter import *
import tkinter.font as font

#Declaração de variaveis globais
auxiliar = 0
aux = 0

def Procurar_parametro(file,diretorio,parametros):
    
    parametros = parametros.replace(' ','')
    
    if parametros.endswith(';'):
        parametros = parametros.rstrip(parametros[-1])
        print (parametros)
    
    parametros = parametros.split(';')
    
    arquivo = diretorio+os.sep+file
    
    global auxiliar
    array = ['']
    
    for parametro in parametros:
        
        if(parametro in file):
            array.append(arquivo)
            auxiliar = 1
    Imprimir_array(array)
    
    array.clear()
    
    return

#Checa se o arquivo é uma pasta e a concatena
def Procurar_pasta(parametro,diretorio,file):
    caminho = diretorio + os.sep + file
    if os.path.isdir(caminho):
        Procurar_arquivo(caminho)
    elif file.endswith('.XML') or file.endswith('.xml'):
        Procurar_parametro(file,diretorio,parametro)

#Procura os arquivos por arquivos XML
def Procurar_arquivo(caminho = ''):
    global auxiliar
    global aux
    parametro = caixa_parametro.get()
    
    if(caminho == ''):
        diretorio = caixa_diretorio.get()
    
    else:
        diretorio = caminho
    
    #Checa se pelo menos um dos arquivos possuem o parametro
    if(aux == 0):
        for file in os.listdir(diretorio):  
            Procurar_pasta(parametro,diretorio,file)
        
        if(auxiliar == 0):
            str(aux)
            aux = 1
            Procurar_arquivo()
        
        auxiliar = 0
        aux = 0
        return
        
    else:
        os.system('explorer "Z:\\05-App\\Relatorios\\XMLs"')
        auxiliar = 0
        aux = 0



#Imprimi o Array de arquivos
def Imprimir_array(array):
    
    if(auxiliar == 1):
        for i in array:
            if(i != ''):
                os.system('copy "'+str(i)+'" "Z:\\05-App\\Relatorios\\XMLs"')
    return

#Constroi a tela
def Tela():
    
    texto_diretorio = Text(app)
    texto_diretorio.place(x = 10, y = 10, width=90, height=20)
    texto_diretorio.configure(state='normal')
    texto_diretorio.insert('end','    Diretorio:')
    texto_diretorio['font'] = myFont
    texto_diretorio.configure(state='disabled')
    texto_diretorio = Text(app, state='disabled', width=44, height=5)

    texto_parametro = Text(app)
    texto_parametro.place(x = 10, y = 40, width=90, height=20)
    texto_parametro.configure(state='normal')
    texto_parametro.insert('end','  Parametros:')
    texto_parametro['font'] = myFont
    texto_parametro.configure(state='disabled')
    
    Button(text='Procurar', bg='white', fg='black', command=Procurar_arquivo).place(x=165, y=80, width=120, height=40)
    
    return

#Inicia o codigo
app = Tk()
var = StringVar()
app.title('Pesquisa XML')
app.geometry("430x150")
app.configure(bg='gray')

myFont = font.Font(size=10)

caixa_diretorio = Entry(app)
caixa_diretorio['font'] = myFont
caixa_diretorio.place(x = 110,y = 10,width=310, height=20)

caixa_parametro = Entry(app)
caixa_parametro['font'] = myFont
caixa_parametro.place(x = 110,y = 40,width=310, height=20)

Tela()

app.mainloop()