# Imports
import tkinter as tk
from tkinter import messagebox
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from PIL import Image
import undetected_chromedriver as uc
import time

#           Código para gerar a prompt e já criar a questão através do ChatGPT

# Funções
def gerarPrompt():
    template = "Elabore uma questão de {materia} que envolva {conteudoEspecifico} e que de alguma forma envolva robôs. Siga as seguintes regras:\n{regras}"
    materia = entry_materia.get()
    conteudoEspecifico = entry_conteudo.get()
    regras = entry_regras.get("1.0", tk.END).strip()

    # Verificando entrada
    if not materia or not conteudoEspecifico or not regras:
        messagebox.showwarning("Preencha todos os campos por favor")
        return
    
    promptFinal = template.format(materia=materia, conteudoEspecifico=conteudoEspecifico, regras=regras)
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, promptFinal)

def limparCampos():
    entry_materia.delete(0, tk.END)
    entry_conteudo.delete(0, tk.END)
    entry_regras.delete("1.0", tk.END)
    text_output.delete(1.0, tk.END)

def copiarPrompt():
    prompt_final = text_output.get(1.0, tk.END).strip()
    if prompt_final:
        root.clipboard_clear()
        root.clipboard_append(prompt_final)
        messagebox.showinfo("Copiado", "Prompt copiado para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Nenhum prompt gerado para copiar.")

def criarQuestao():
    global driver
    prompt_final = text_output.get(1.0, tk.END).strip()
    if not prompt_final:
        messagebox.showwarning("Aviso", "Nenhum prompt gerado para criar a questão.")
        return
    
    # Copia o prompt para a área de transferência
    pyperclip.copy(prompt_final)
    
    # Inicializa o navegador com Selenium

    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    service = Service(ChromeDriverManager().install())
    driver = uc.Chrome(service=service, options=chrome_options)
    driver.get("https://chatgpt.com/")

    # Espera o navegador carregar
    time.sleep(5)  # Ajuste o tempo conforme necessário

    # Localiza o campo de entrada e cola o prompt copiado
    campo_entrada = driver.find_element(By.XPATH, '//*[@id="prompt-textarea"]')
    campo_entrada.send_keys(Keys.CONTROL, 'v')
    campo_entrada.send_keys(Keys.ENTER)
    time.sleep(5)

    messagebox.showinfo("Info", "Questão criada com sucesso no site!")

def fecharNavegador():
    global driver
    if driver:
        driver.quit()
        messagebox.showinfo("Fechado", "Navegador fechado com sucesso.")
        driver = None
    else:
        messagebox.showwarning("Aviso", "Nenhum navegador aberto para fechar.")


# Configuração da janela principal

root = tk.Tk()
root.title("Montador de Prompts")
root.geometry("400x400")

# Widgets da Interface Gráfica
label_materia = tk.Label(root, text="Materia:")
label_materia.pack()

entry_materia= tk.Entry(root, width=50)
entry_materia.pack()

label_conteudo = tk.Label(root, text="Conteúdo:")
label_conteudo.pack()

entry_conteudo = tk.Entry(root, width=50)
entry_conteudo.pack()

label_regras = tk.Label(root, text="Regras:")
label_regras.pack()

entry_regras = tk.Text(root, width=50, height=5)
entry_regras.pack()

button_gerar = tk.Button(root, text="Gerar Prompt", command=gerarPrompt)
button_gerar.pack()

button_limpar = tk.Button(root, text="Limpar", command=limparCampos)
button_limpar.pack()

button_copiar = tk.Button(root, text="Copiar Prompt", command=copiarPrompt)
button_copiar.pack()

button_criar_questao = tk.Button(root, text="Criar Questão", command=criarQuestao)
button_criar_questao.pack()

button_fechar_navegador = tk.Button(root, text="Fechar Navegador", command=fecharNavegador)
button_fechar_navegador.pack()

label_output = tk.Label(root, text="Prompt Gerado:")
label_output.pack()

text_output = tk.Text(root, height=5, width=50)
text_output.pack()

# Executa a interface
root.mainloop()
