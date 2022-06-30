import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW
from functools import partial
from tkinter import *
from tkinter.ttk import *

#Variaveis globais
usuario = 'admin@lobebr.onmicrosoft.com'
senha = '@Lo#28160710#Be@'
departamentos = ['01-CTB', '02-FIS', '03-DP', '05-JUR', '06-AUD']
permissoes = '13'
login = TRUE
painel = TRUE

#Recebe, separa e organiza os cnpj's
def organizar_cnpjs(caixa_cnpj):
    lista_cnpjs = caixa_cnpj.get()
    lista_cnpjs = lista_cnpjs.replace(' ','')
    
    if lista_cnpjs.endswith(';'):
        lista_cnpjs = lista_cnpjs.rstrip(lista_cnpjs[-1])
    
    cnpjs = lista_cnpjs.split(';')
    
    iniciar_driver(cnpjs)

#Procura pelo elemento antes de continuar
def esperar_elemento(driver, elemento, tempo):
    time.sleep(0.15)
    WDW(driver, tempo).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))

#Iniciar driver do chrome
def iniciar_driver(cnpjs):
    global login
    global painel
    login = TRUE
    painel = TRUE
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    for cnpj in cnpjs:
        iniciar_sharepoint(cnpj, driver)

#Iniciar e logar no chrome
def iniciar_sharepoint(cnpj, driver):
    global login
    driver.get('https://lobebr.sharepoint.com/sites/lobe/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2Flobe%2FShared%20Documents%2FGestao3%2F'+cnpj+'&viewid=1ea88aaa-0d0a-40c4-ab25-7c033e7f7d58')
    
    #Checa se o usuário já está logado
    if login:
        esperar_elemento(driver, '[id="i0116"]', 10)
        
        driver.find_element(By.ID, "i0116").send_keys(usuario)
        driver.find_element(By.ID, "idSIButton9").click()
        
        esperar_elemento(driver, '[name="passwd"]', 10)
        
        driver.find_element(By.ID, "i0118").send_keys(senha)
        driver.find_element(By.ID, "idSIButton9").click()
        driver.find_element(By.ID, "idBtn_Back").click()
        
        login = FALSE
    
    listar_itens(driver)

#Transforma as pastas em um elemento de array
def listar_itens(driver):
    
    esperar_elemento(driver, '[class = "ms-List-cell"]', 10)
    itens = driver.find_elements(By.CLASS_NAME, 'ms-List-cell')
    
    for item in itens:
        filtrar_pastas(driver, item)

#Separa as pastas que precisam ser alteradas o acesso
def filtrar_pastas(driver, item):
    global departamentos
    
    try:
        item.find_element(By.CLASS_NAME, 'ms-DetailsRow-cell').click()
    except:
        return
    
    esperar_elemento(driver, '[title*="-"]', 10)
    dep = driver.find_element(By.CLASS_NAME, 'is-selected').find_element(By.CSS_SELECTOR, '[title*="-"]').text
    
    if dep in departamentos:
        local_dep = departamentos.index(dep)
        acessar_avancado(driver, local_dep, item)
    else:
        item.find_element(By.CLASS_NAME, 'ms-DetailsRow-cell').click()

#Entra na aba de gerenciamento avançado
def acessar_avancado(driver, local_dep, item):
    global painel
    global permissoes
    
    if painel:
        driver.find_element(By.CSS_SELECTOR, '[title="Abrir o painel de detalhes"]').click()
        painel = FALSE
    
    esperar_elemento(driver, '[class = "od-SharingSection-manageAccess"]', 10)
    numero_permissoes = driver.find_element(By.CSS_SELECTOR, '[aria-label*="Grupos que"]').text
    
    if permissoes in numero_permissoes:
        driver.find_element(By.CSS_SELECTOR, '[class="od-SharingSection-manageAccess"]').click()
        
        esperar_elemento(driver, '[id="shareFrame"]', 10)
        driver.switch_to.frame('shareFrame')
        
        #Da o Scroll para acesso a opcao "Avançado"
        driver.execute_script("document.querySelector('.od-PermissionsList').scrollTo({top:document.querySelector('.od-PermissionsList-advancedUrl').offsetTop});")
        driver.find_element(By.CSS_SELECTOR, '.od-PermissionsList-advancedUrl')
        driver.find_element(By.TAG_NAME, 'a').click()
        
        trocar_aba(driver, local_dep, item)
    else:
        item.find_element(By.CLASS_NAME, 'ms-DetailsRow-cell').click()

#Altera as abas 
def trocar_aba(driver, local_dep, item):
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    WDW(driver, 10).until(EC.visibility_of_element_located((By.ID, "ctl00_PlaceHolderLeftNavBar_QuickLaunchNavigationManager")))
    
    liberar_edicao(driver)
    marcar_caixas(driver, local_dep, tabs, item)

#Seleciona a opção para liberar os checkbox
def liberar_edicao(driver):
    
    try:
        esperar_elemento(driver, '[title="Permissões"]', 10)
    except:
        time.sleep(3)
    
    driver.find_element(By.ID, "Ribbon.Permission.Manage.StopInherit-Large").click()
    try:
        WDW(driver, 3).until(EC.alert_is_present())
        Alert(driver).accept()
    except:
        WDW(driver, 3).until(EC.alert_is_present())
        Alert(driver).accept()

#Separa as caixas a serem selecionadas por deportamento
def marcar_caixas(driver, local_dep, tabs, item):
    try:
        esperar_elemento(driver, '[id="idSelectAll"]', 3)
    except:
        esperar_elemento(driver, '[id="idSelectAll"]', 3)
    
    driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[0].click()")
    driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[2].click()")
    driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[3].click()")
    driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[9].click()")
    driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[11].click()")
    driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[12].click()")
    
    match local_dep:
        case 1:
            driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[6].click()")
            driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[7].click()")
            driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[8].click()")
        case 2:
            driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[4].click()")
            driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[5].click()")
        case 3:
            driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[10].click()")
        case 4:
            driver.execute_script("document.querySelectorAll('input[type=\"checkbox\"]')[1].click()")
    
    esperar_elemento(driver, '[id="Ribbon.Permission.Modify.RemovePerms-Large"]', 10)
    driver.find_element(By.ID, "Ribbon.Permission.Modify.RemovePerms-Large").click()
    
    WDW(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    esperar_elemento(driver, '[id="Ribbon.Permission.Modify.RemovePerms-Large"]', 15)
    
    finalizar_aba(driver, tabs, item)

#Finaliza a aba avançada e volta para a principal
def finalizar_aba(driver, tabs, item):
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.switch_to.default_content()
    try:
        driver.find_element(By.ID, "shareFrame").send_keys(Keys.ESCAPE)
        item.find_element(By.CLASS_NAME, 'ms-DetailsRow-cell').click()
    except:
        item.find_element(By.CLASS_NAME, 'ms-DetailsRow-cell').click()

#Construção da interface
def tela(app):
    app.title('Gerenciar acessos')
    app.geometry("430x90")
    app.configure(bg='light blue')

    caixa_cnpj = Entry(app)
    caixa_cnpj.place(x = 110, y = 10, width=310, height=20)
    texto_cnpj = Label(app)
    texto_cnpj.place(x = 10, y = 10, width=90, height=20)
    texto_cnpj.configure(text='         CNPJ',state='readonly',justify='center')
    texto_cnpj = Text(app, width=44, height=5)
    
    Button(text='PROCURAR', command=partial(organizar_cnpjs,caixa_cnpj)).place(x=155, y=40, width=120, height=40)

#Main
def main ():
    app = Tk()
    tela(app)
    app.mainloop()

main()