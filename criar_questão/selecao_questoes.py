import tkinter as tk
from tkinter import messagebox
import os

def buscar_questoes(materia, nivel):
    questoes_pasta = 'C:/Users/maria/EXTENSÃO-OBR/CodigosExtensao/QUESTÕES'
    gabaritos_pasta = 'C:/Users/maria/EXTENSÃO-OBR/CodigosExtensao/GABARITOS'

    questoes_disponiveis = []
    for arquivo in os.listdir(questoes_pasta):
        if arquivo.startswith(f'{materia}-{nivel}-') and not arquivo.endswith('GABARITO'):
            questoes_disponiveis.append(arquivo)
    
    return questoes_disponiveis

def exibir_questao(questao):
    questoes_pasta = 'C:/Users/maria/EXTENSÃO-OBR/CodigosExtensao/QUESTÕES'
    with open(os.path.join(questoes_pasta, questao), 'r') as f:
        return f.read()

def adicionar_prova(questao):
    questoes_pasta = 'C:/Users/maria/EXTENSÃO-OBR/CodigosExtensao/QUESTÕES'
    gabaritos_pasta = 'C:/Users/maria/EXTENSÃO-OBR/CodigosExtensao/GABARITOS'
    
    # Adiciona a questão ao arquivo prova.txt
    with open('prova.txt', 'a') as f:
        f.write(exibir_questao(questao))
        f.write('\n---\n')
    
    # Adiciona o gabarito ao arquivo provaGABARITO.txt
    gabarito = questao.replace('.txt', 'GABARITO.txt')
    with open(os.path.join(gabaritos_pasta, gabarito), 'r') as f:
        gabarito_conteudo = f.read()
    
    with open('provaGABARITO.txt', 'a') as f:
        f.write(gabarito_conteudo)
        f.write('\n---\n')

def buscar_questao():
    materia = entry_materia.get()
    nivel = entry_nivel.get()
    questoes_disponiveis = buscar_questoes(materia, nivel)
    
    if not questoes_disponiveis:
        messagebox.showinfo("Resultado", "Nenhuma questão encontrada.")
        return
    
    lista_questoes.delete(0, tk.END)
    for questao in questoes_disponiveis:
        lista_questoes.insert(tk.END, questao)

def visualizar_questao():
    selecionada = lista_questoes.curselection()
    if not selecionada:
        messagebox.showwarning("Seleção", "Selecione uma questão da lista.")
        return
    
    questao = lista_questoes.get(selecionada[0])
    conteudo = exibir_questao(questao)
    
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, conteudo)

def adicionar_questao():
    selecionada = lista_questoes.curselection()
    if not selecionada:
        messagebox.showwarning("Seleção", "Selecione uma questão da lista.")
        return
    
    questao = lista_questoes.get(selecionada[0])
    adicionar_prova(questao)
    messagebox.showinfo("Sucesso", "Questão e gabarito adicionados com sucesso.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerenciador de Questões")

# Entrada de matéria e nível
tk.Label(root, text="Matéria:").pack()
entry_materia = tk.Entry(root)
entry_materia.pack()

tk.Label(root, text="Nível:").pack()
entry_nivel = tk.Entry(root)
entry_nivel.pack()

# Botão de busca
btn_buscar = tk.Button(root, text="Buscar Questões", command=buscar_questao)
btn_buscar.pack()

# Lista de questões
lista_questoes = tk.Listbox(root, height=20, width=30)
lista_questoes.pack()

# Área de visualização da questão
text_area = tk.Text(root, height=10, width=50)
text_area.pack()

# Botões de visualizar e adicionar
btn_visualizar = tk.Button(root, text="Visualizar Questão", command=visualizar_questao)
btn_visualizar.pack()

btn_adicionar = tk.Button(root, text="Adicionar Questão", command=adicionar_questao)
btn_adicionar.pack()

root.mainloop()
