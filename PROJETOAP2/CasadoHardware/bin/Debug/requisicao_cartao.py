from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

def organizar():
    file = open('resposta.txt', 'r')
    conteudo_file = file.read()
    file.close()

    conteudo = conteudo_file.split('-')

    var1 = ['DATA_VALIDADE.txt', 'NCARTAO.txt', 'NCODIGO.txt', 'NCONTA.txt']
    var2 = ['data_validade', 'ncartao', 'ncodigo', 'nconta']
    
    i = 0
    while(i < 4):
        var2[i] = conteudo[i]

        file = open(var1[i], 'w')
        file.write(var2[i])
        file.close()
        
        i+=1
        

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path='C:\chromedriver', chrome_options=options)
driver.get('http://192.168.1.102:5000')

#os.system('cls')

btn = driver.find_element(By.ID, '0')
btn.send_keys('C:\\Users\\arthu\\PROJETOAP2\\CasadoHardware\\bin\\Debug\\cartao.txt')

#os.system('cls')

btn = driver.find_element(By.ID, '1')
btn.click()

#os.system('cls')

print('\ndados.txt ENVIADO COM SUCESSO!\n')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print('AGUARDE...')

i = 10
while(i >= 1):
    time.sleep(1)
    i -= 1

#try:
driver.get('http://192.168.1.102:5000/static/resposta.txt')

element=driver.find_element_by_tag_name("pre")
element = str(element.text)

file = open('resposta.txt', 'w')
file.write(element)
file.close()

file = open('resposta.txt', 'r')
resp = file.read()
file.close()

if resp != 'FALSE':
    organizar()

#print('RESPOSTA ARMAZENADA COM SUCESSO')

#except:
    #print('ALGO DEU ERRADO')

driver.close()
        
        