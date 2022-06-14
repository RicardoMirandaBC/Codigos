import os

# gruposD = 'Grupo Fiscal C1.S1.G01;Grupo Fiscal C1.S1.G02;Grupo Contabil C1.S1.G01;Grupo Contabil C1.S1.G02;Grupo DP C1.S1.G01;Grupo DP C1.S1.G02;Grupo Societário C1.S1.G01'

raiz = "Z:\\01-Clientes\\1-PJ\\1-Gestão\\1-Lobe\\1-Ativos\\1-LR"
pastas = ['00088925000136','01570529000103','01570529000294','01570529000375','01570529000537','05263312000101','05263312000292','05263312000373','05263312000454','05263312000535','05263312000616','05263312000705','05263312000888','05263312000969','05263312001000','05263312001183','06065614000138','06065614000219','06696359000121','06696359000202','06696359000393'] 
# ['07640617000110','07640617000200','07847837000110','07847837000209','08944556000148','08944556000229','08944556000300','08944556000490','08944556000571','08944556000652','08944556000733','13535892000177','13535892000258','13535892000339','14115388000180','14115388000261','14115388000342','14144890000110','14144890000209','16699864000183','24702356000135','24702356000216','24822967000117','24822967000206','28415097000112','32996515000180','34351642000157','37530695000123','37657541000105','37871241000116','37871241000205','41299316000103','41299316000294','41299316000375','41299316000456','00126365000167','00920531000100','02907061000162','02907061000243','02907061000324','02907061000596','02907061000677','02907061000910','02907061001053','02907061001304','02907061001568','02907061001649','02907061001720','02907061001800','02907061002106','03416540000149','08593452000136','10202833000199','10353516000173','10648051000188','10856350000108','10856350000531','10960950000111','12506375000107','14115388000180','17032154000168','17658214000152','18813043000151','20238167000100','20433152000195','21866592000107','21866592000280','23245718000143','23271638000162','23271638000677','23271638000758','23271638000910','23271638001053','23271638001134','23881419000103','24822967000117','24822967000206','25452679000180','26849941000198','27310013000113','27325768000191','27718661000103','28194914000150','28194914000230','28415097000112','30205320000149','30873363000100','32429377000157','32996515000180','33772464000175','34351642000157','34890173000144','36281967000136','37530695000123','37657541000105','37871241000116','37871241000205','38006034000166','38214055000177','38284657000109','38310139000104','38613440000197','40500492000107','40667054000120','41299316000103','41299316000294','41299316000375','41299316000456','41399952000107','41675654000100','41767132000120']

for pasta in os.listdir(raiz):    
    if(os.path.isdir(raiz+'/'+pasta)):
        cnpj = pasta.split('-')[0]
        
        for pasta2 in os.listdir(raiz+'/'+pasta):
            pastaEmpresa = raiz+'/'+pasta+'/'+pasta2
            
            if(os.path.isdir(pastaEmpresa)):
                
                if ' ' in cnpj + pasta2:
                    cnpj = cnpj+pasta2.split(' ')[0]
                    cnpj = cnpj.split('-')[0]
                
                else:
                    cnpj = cnpj+pasta2.split('-')[0]
                    cnpj = cnpj.split(' ')[0]
                
                # print(cnpj)
                
                if(os.path.isdir("C:/Users/Ricardo Miranda/Documents/OneDrive/"+str(cnpj))):
                    
                    for item in os.listdir("C:/Users/Ricardo Miranda/Documents/OneDrive/"+str(cnpj)):
                        print(item)
                else:
                    
                    try:
                        #Verificar se tem tamanho de cnpj e somente digitos numericos
                        if(len(cnpj) == 14 and int(cnpj)):
                            pastaCriada = "C:/Users/Ricardo Miranda/Documents/OneDrive/"+str(cnpj)
                            # os.mkdir(pastaCriada)  
                            # if(str(cnpj) not in pastas):
                            for departamentoDiretorio in os.listdir(pastaEmpresa):
                                # pastasRequisitadas = ['CTB','FIS','CRM','DP','FIN','JUR','AUD','CTRL','Reuniões','Central','ncias','','','']
                                pastasIgnoradas = ['DOCS']
                                
                                # if list(filter(departamentoDiretorio.endswith,pastasRequisitadas)):
                                pastaDepartamento = pastaEmpresa + '/' + departamentoDiretorio 
                                # print(pastaDepartamento)
                                
                                docs = os.listdir(pastaDepartamento)
                                ignorar = False
                                
                                for index in range(0, len(docs)):
                                    for i in pastasIgnoradas:
                                        if(i in docs[index]):
                                            ignorar = True
                                    if(ignorar == False):
                                        if os.path.isdir(pastaEmpresa+'/'+departamentoDiretorio+'/'+docs[index]):
                                            
                                            os.system('xcopy "'+pastaEmpresa+'/'+departamentoDiretorio+'/'+docs[index]+'" "'+pastaCriada+'/'+departamentoDiretorio+'/'+docs[index]+'" /h /i /c /k /e /r /y')
                                        else:
                                            
                                            os.system('xcopy "'+pastaEmpresa+'/'+departamentoDiretorio+'" "'+pastaCriada+'/'+departamentoDiretorio+'"')
                                    else:
                                        print('não copia'+docs[index]+'\n')
                                    ignorar = False
                                
                        else:
                            print('não tem o tamanho de um diretorio')
                    
                    except:
                        print('não é numero')
                    
                cnpj = pasta.split('-')[0]
                
