#Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Fazer login
#Importar a base de dados
#Cadastrar 1 produto
#Repetir o processo 

import pyautogui
import time
#delay pra cada comando do pyautogui
pyautogui.PAUSE = 0.5

#abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#escrever o link e entrar nele
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#delay um pouco maioremail@gmail.com
time.sleep(3)
#fazer login
pyautogui.click(x=547, y=384) #clickar pra escrever email
pyautogui.write ("email@gmail.com") #escreve email
pyautogui.press("tab") #tabeia o fomulario, manda pra baixo
pyautogui.write ("senha123")#escreve senha
pyautogui.click(x=676, y=534)
time.sleep(3) 

import pandas

tabela = pandas.read_csv("produtos.csv")

#Cadastrar 1 produto

for linha in tabela.index:

    pyautogui.click (x=557, y=261) #clicka no campo 1
    codigo = tabela.loc[linha, "codigo"]

    pyautogui.write(codigo) #codigo do produto
    pyautogui.press ("tab") #tabeia para o proximo

    pyautogui.write(tabela.loc[linha,"marca"]) #marca
    pyautogui.press ("tab") #tabeia para o proximo

    pyautogui.write(tabela.loc[linha,"tipo"]) #tipo
    pyautogui.press("tab") #tabeia para o proximo

    pyautogui.write(str(tabela.loc[linha,"categoria"])) #categoria
    pyautogui.press("tab") #tabeia para o proximo

    pyautogui.write(str(tabela.loc[linha,"preco_unitario"])) #preço
    pyautogui.press("tab") #tabeia para o proximo

    pyautogui.write(str(tabela.loc[linha,"custo"])) #custo
    pyautogui.press("tab") #tabeia para o proximo
    
    #caso a OBS esteja vazia, ele vai apenas passar pro proximo, caso contrario, ele escreve a obs.
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs): #verifica se está vazio o campo (NaN)
        pyautogui.write(obs) #obs
    pyautogui.press("tab") #tabeia para o proximo

    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)