from playwright.sync_api import sync_playwright
import time
import clipboard
import pyperclip
import pyautogui as pg
import sqlite3
import random

con = sqlite3.connect('C:\\Users\\Lucas_Feitosa\\Desktop\\python\\BOT\\Banco_IP.db')
cursor = con.cursor()


while True:
    with sync_playwright() as p:
        nav = p.chromium.launch(headless=False)
        context = nav.new_context()
        context.set_default_timeout(600000)
        pag = nav.new_page()
        
        try:    
                # pag.goto('https://meuip.com.br/tools-geo.php', timeout=600000)
    
    
                # time.sleep(3)  # Aguarde alguns segundos para a página renderizar
    
                # xpath_expression = 'xpath=//*[@id="content"]/div[1]/div[3]/div/div/div/div[2]'  
                # element = pag.query_selector(xpath_expression)
                # print(element)
    
                # if element:
        
                #     texto_elemento = element.inner_text()

        
                #     texto_esperado = 'São Paulo'

                    # if texto_esperado in texto_elemento:
                        try:
                       
                            pag.goto('https://www.google.com.br/?hl=pt-BR', timeout=600000)
                        except:
                            pag.goto('http://192.168.1.1/index.html#login')
                            pag.fill('xpath=//*[@id="txtPwd"]', '4dUA222a')
                            pag.click('xpath=//*[@id="btnLogin"]')
                            time.sleep(10)
                            pag.click('xpath=//*[@id="container"]/div[3]/a[5]/div/img')
                            pag.click('xpath=//*[@id="frmLan"]/div/ul/li[6]/a')
                            pag.click('xpath=//*[@id="frmRestoreReset"]/div/div[1]/div/input[1]')
                            pag.click('xpath=//*[@id="yesbtn"]')
                            time.sleep(70)



                        pag.fill('//*[@id="APjFqb"]', '4devs')
                        pag.keyboard.press('Enter')
                        time.sleep(1)
                        pag.click('//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
                        
                        pag.click('xpath=//*[@id="top-nav"]/li[23]/a')
                        pag.click('xpath=//*[@id="app-wrapper"]/div[2]/div[2]/div[1]/div[1]/div[2]/label')
                        pag.click('xpath=//*[@id="idade"]')
                        #pag.keyboard.press('ArrowDown')
                        pag.keyboard.press('ArrowDown')
                        pag.keyboard.press('Enter')
                        pag.click('xpath=//*[@id="cep_estado"]')
                        pag.keyboard.press('s')
                        pag.keyboard.press('ArrowDown')
                        pag.keyboard.press('ArrowDown')
                        pag.keyboard.press('Enter')
                        pag.click('xpath=//*[@id="cep_cidade"]')
                        time.sleep(6)
                        pag.keyboard.press('s')
                        vezes = 77
                        for _ in range(vezes):
                            pag.keyboard.press('ArrowDown')
                        pag.keyboard.press('Enter')
                        pag.click('xpath=//*[@id="app-wrapper"]/div[2]/div[2]/div[4]/div[1]/div[3]/label')
                        pag.click('xpath=//*[@id="bt_gerar_pessoa"]')
                        pag.wait_for_selector('//*[@id="nome"]/span[1]')
                        nome_element = pag.locator('xpath=//*[@id="nome"]/span[1]')
                        nome = nome_element.text_content()
                        email_element = pag.locator('xpath=//*[@id="email"]/span[1]')
                        email = email_element.text_content()
                        celular_element = pag.locator('xpath=//*[@id="celular"]/span[1]')
                        celular = celular_element.text_content()
                        cpf_element = pag.locator('//*[@id="cpf"]/span[1]')
                        cpf = cpf_element.text_content()
                        nascimento_element = pag.locator('//*[@id="data_nasc"]/span[1]')
                        nascimento = nascimento_element.text_content()
                        cep_element = pag.locator('xpath=//*[@id="cep"]/span[1]')
                        cep = cep_element.text_content()
                        numero_element = pag.locator('xpath=//*[@id="numero"]/span[1]')
                        numero = numero_element.text_content()                       
                        pag.goto('https://leadsolution.g2afse.com/click?pid=73&offer_id=258', timeout=600000)                       
                        time.sleep(1)
                        
                        try:
                            pag.locator('xpath=//*[@id="btn-cookie"]')
                            pag.keyboard.press('F5')
                            # pag.wait_for_selector('xpath=//*[@id="header"]/div/button', timeout=40000)
                            # pag.click('xpath=//*[@id="header"]/div/button')
                            #pag.click('//*[@id="btn-cookie"]')
                            pag.click('xpath=//*[@id="header"]/div/button')
                            #time.sleep(1000000)

                            # vezes_tab = 10
                            # for _ in range(vezes_tab):
                            #     pag.keyboard.press('Tab')
                            # pag.keyboard.press('Enter')
                            
                            time.sleep(15)
                            vezes_tab_nome = 53
                            for _ in range(vezes_tab_nome):
                                pag.keyboard.press('Tab')
                            pyperclip.copy(nome)
                            pag.keyboard.press('Control+v')
                            


                            pag.keyboard.press('Tab')
                            
                            pag.keyboard.press('Tab')
                            
                            pyperclip.copy(email)
                            pag.keyboard.press('Control+v')
                            time.sleep(2)
                            pag.keyboard.press('Tab')
                            pyperclip.copy(celular)
                            pag.keyboard.press('Control+v')
                            pag.keyboard.press('Tab')
                            pyperclip.copy(cpf)
                            pag.keyboard.press('Control+v')
                            pag.keyboard.press('Tab')
                            pyperclip.copy(nascimento)
                            pag.keyboard.press('Control+v')
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Space')
                            time.sleep(4)
                            pag.keyboard.press('Tab')
                            
                            time.sleep(1)
                            pag.keyboard.press('Tab')
                            time.sleep(1)
                            pag.keyboard.press('Enter')
                            time.sleep(13)
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            cursos = [
                                "Direito", "Ciências Econômicas", "Engenharia Civil", "Psicologia", "Educação Física",
                                "Administração"

                            ]
                            cursos_aleatorio = random.choice(cursos)

                            
                            
                            pyperclip.copy(cursos_aleatorio)
                            print(cursos_aleatorio)
                            pag.keyboard.press('Control+v')
                            pag.keyboard.press('ArrowDown')
                            pag.keyboard.press('Enter')
                            time.sleep(4)
                            
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            unidade = 'São Paulo'
                            pyperclip.copy(unidade)
                            pag.keyboard.press('Control+v')
                            pag.keyboard.press('ArrowDown')
                            pag.keyboard.press('Enter')
                            time.sleep(7)
                            pag.keyboard.press('Tab')
                            time.sleep(2)
                            pag.keyboard.press('Tab')
                            time.sleep(2)
                            pag.keyboard.press('Enter')
                            time.sleep(20)
                            pag.keyboard.press('M')
                            time.sleep(7)
                            pag.keyboard.press('Enter')
                            pag.keyboard.press('Tab')
                            time.sleep(1)
                            pag.keyboard.press('Tab')
                            time.sleep(1)
                            pag.keyboard.press('Tab')
                            
                            time.sleep(1)
                            pag.keyboard.press('Tab')
                            time.sleep(1)
                            pag.keyboard.press('Enter')
                            time.sleep(7)
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            time.sleep(2)
                            pyperclip.copy(cep)
                            pag.keyboard.press('Control+v')
                            
                            pag.keyboard.press('Tab')
                            time.sleep(4)
                            pag.keyboard.press('Tab')
                            pyperclip.copy(numero)
                            time.sleep(2)
                            pag.keyboard.press('Control+v')
                            
                            pag.keyboard.press('Tab')
                        
                            pag.keyboard.press('Tab')
                            
                            pag.keyboard.press('Tab')
                            
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            
                            pag.keyboard.press('Enter')
                            time.sleep(4)
                            
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            pyperclip.copy(unidade)
                            pag.keyboard.press('Control+v')
                            pag.keyboard.press('ArrowDown')
                            pag.keyboard.press('Enter')
                            time.sleep(2)
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            pyperclip.copy(unidade)
                            pag.keyboard.press('Control+v')
                            pag.keyboard.press('ArrowDown')
                            pag.keyboard.press('ArrowDown')
                            pag.keyboard.press('Enter')
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            escola = [
                                'RUI BLOEM', 'FERNAO DIAS PAES', "SAO PEDRO COLEGIO", "ALBERT SABIN COLEGIO", "BARAO DE RAMALHO",
                                "MARAJOARA COLEGIO", "TERRAMAR COLEGIO", "MORUMBI SUL COLEGIO", "COLEGIO SANTA MARTA",

                            ]
                            escolas_aleatorio = random.choice(escola)

                            
                            pyperclip.copy(escolas_aleatorio)
                            
                            pag.keyboard.press('Control+v')
                            pag.keyboard.press('ArrowDown')
                            pag.keyboard.press('Enter')
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            termino = '2022'
                            pyperclip.copy(termino)
                            pag.keyboard.press('Control+v')
                            pag.keyboard.press('ArrowDown')
                            time.sleep(2)
                            pag.keyboard.press('Tab')
                            time.sleep(2)
                            pag.keyboard.press('Tab')
                            time.sleep(2)
                            pag.keyboard.press('Tab')
                            time.sleep(2)
                            pag.keyboard.press('Tab')
                            time.sleep(2)
                            pag.keyboard.press('Enter')
                            time.sleep(6)
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Enter')
                            time.sleep(10)
                            pag.click('xpath=//*[@id="btn-cookie"]')
                            pg.click(x=1146, y=364)
                            time.sleep(10)
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Enter')
                            time.sleep(15)
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Tab')
                            pag.keyboard.press('Enter')
                            time.sleep(5)
                            
                            pag.goto('http://www.meuip.com')
                            ipcopy_element = pag.locator('xpath=/html/body/div/div[1]/div/table/tbody/tr/td[1]/h1/font')
                            ipcopy = ipcopy_element.text_content()

                            cursor.execute(f"INSERT INTO ip VALUES ('{ipcopy}')")
                            
                            con.commit()

                            pag.goto('http://192.168.1.1/index.html#login')
                            pag.fill('xpath=//*[@id="txtPwd"]', '4dUA222a')
                            pag.click('xpath=//*[@id="btnLogin"]')
                            time.sleep(10)
                            pag.click('xpath=//*[@id="container"]/div[3]/a[5]/div/img')
                            pag.click('xpath=//*[@id="frmLan"]/div/ul/li[6]/a')
                            pag.click('xpath=//*[@id="frmRestoreReset"]/div/div[1]/div/input[1]')
                            pag.click('xpath=//*[@id="yesbtn"]')
                            time.sleep(70)




                        except:
                            pag.goto('http://192.168.1.1/index.html#login')
                        pag.fill('xpath=//*[@id="txtPwd"]', '4dUA222a')
                        pag.click('xpath=//*[@id="btnLogin"]')
                        time.sleep(10)
                        pag.click('xpath=//*[@id="container"]/div[3]/a[5]/div/img')
                        pag.click('xpath=//*[@id="frmLan"]/div/ul/li[6]/a')
                        pag.click('xpath=//*[@id="frmRestoreReset"]/div/div[1]/div/input[1]')
                        pag.click('xpath=//*[@id="yesbtn"]')
                        time.sleep(70)
                       
                       
                        
                
        except:
                print('ocorreu um erro!')
                nav.close()




                
        finally:
                nav.close()    
        
    #print(nome, email, celular, cpf, nascimento)