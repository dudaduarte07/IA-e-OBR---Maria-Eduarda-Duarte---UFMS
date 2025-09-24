# Código para a geração de prompts para criação de questões para a OBR

# Imports
import tkinter as tk
from tkinter import messagebox

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
    else: messagebox.showwarning("Aviso", "Nenhum prompt gerado para copiar.")

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

label_output = tk.Label(root, text="Prompt Gerado:")
label_output.pack()

text_output = tk.Text(root, height=5, width=50)
text_output.pack()

# Executa a interface
root.mainloop()
