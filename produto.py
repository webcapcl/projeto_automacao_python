import pyautogui
import time



link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 2
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')


# Paso 2: fazer login no site
pyautogui.write(link)
pyautogui.press('enter')

# Fazer uma pausa maior pro site carregar
time.sleep(2)

# Clicar no campo de login
pyautogui.click(x=517, y=448)  # Ajuste as coordenadas conforme necessário
pyautogui.write('aula@gmail.com')  # Substitua pelo seu usuário    
pyautogui.press('tab')  # Mover para o campo de senha
pyautogui.write('python123')  # Substitua pela sua senha    
pyautogui.press('tab')  # Passar para o botão
pyautogui.press('enter')  # Pressionar o botão
# Fazer uma pausa maior pro site carregar
time.sleep(5)

# Passo 4 abrir a base de dados precia fazer a instalação do pandas
# pip install pandas openpyxl

# Cmando para importar o arquivo da  base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)
# passo 5 cadastrar todos os produtos da base de dados
for linha in tabela.index:
    # todos os comando abaixo estão dentro do for 
    # pra ter funcionalidade 'identação'


# Cadastar 1 produto
# codigo
    pyautogui.click(x=631, y=320)  # Ajuste as coordenadas conforme necessário
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)  # Substitua pelo código do produto
    pyautogui.press('tab')  # Mover para o campo de marca
    
    #Marca
    marca =str(tabela.loc[linha, 'marca'])      
    pyautogui.write(marca)  # Substitua pelaLogitech   o produto
    pyautogui.press('tab')  # Mover para o campo de categoria
    # tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)  # Substitua pelo tipo do produto
    pyautogui.press('tab') 
    # categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)  # Substitua pela categoria do produto
    pyautogui.press('tab') 
    # preco
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)  # Substitua pela preço do produto
    pyautogui.press('tab') 
    # custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)  # Substitua pela custo do produto
    pyautogui.press('tab') 
    # obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)  # Substitua pela observação do produto
    pyautogui.press('tab') 

    pyautogui.press('enter')  # Pressionar o botão para cadastrar o produto
    pyautogui.scroll(4000) # Rolar a página para cima   