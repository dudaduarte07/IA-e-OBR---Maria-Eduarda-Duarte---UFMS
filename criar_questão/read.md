# 📝 Montador e Gerenciador de Questões – OBR

Este projeto foi desenvolvido para auxiliar na **criação de prompts para geração de questões via ChatGPT** e também no **gerenciamento de questões e gabaritos** já salvos em arquivos.  

O sistema possui duas partes principais:  
1. **Montador de Prompts** → Cria prompts personalizados e já abre o ChatGPT para gerar questões automaticamente.  
2. **Gerenciador de Questões** → Busca, exibe e organiza questões e gabaritos em arquivos de prova.  

---

## 🚀 Funcionalidades

### Montador de Prompts
- Inserir **Matéria**, **Conteúdo Específico** e **Regras** para gerar um prompt estruturado.  
- Copiar o prompt para a área de transferência.  
- Abrir automaticamente o **ChatGPT** no navegador e colar o prompt para gerar uma questão.  
- Fechar o navegador pelo próprio sistema.  

### Gerenciador de Questões
- Buscar questões salvas localmente por **matéria** e **nível**.  
- Visualizar o conteúdo de cada questão em tempo real.  
- Adicionar questões e seus gabaritos em arquivos de prova (`prova.txt` e `provaGABARITO.txt`).  

---

## 🛠️ Tecnologias utilizadas
- [Python 3](https://www.python.org/)  
- [Tkinter](https://docs.python.org/3/library/tkinter.html) → Interface gráfica  
- [Selenium](https://www.selenium.dev/) + [Undetected ChromeDriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) → Automação do navegador  
- [webdriver-manager](https://pypi.org/project/webdriver-manager/) → Gerenciar drivers do Chrome  
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/) → Manipulação de imagens  
- [Pyperclip](https://pypi.org/project/pyperclip/) → Copiar textos para a área de transferência  

---

## ⚙️ Instalação e Configuração

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/dudaduarte07/IA-e-OBR---Maria-Eduarda-Duarte---UFMS/tree/main
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado)**:
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Linux/Mac
```

3. **Instale as dependências**:
```bash
pip install -r requirements.txt
```


---

##  ▶️ Como Usar

1. Montador de Prompts

Execute o script:
```bash
python prompt+questao.py
```


  - Preencha Matéria, Conteúdo e Regras.

  - Clique em Gerar Prompt.

  - Se desejar, clique em Criar Questão → o navegador abrirá o ChatGPT, colará o prompt e gerará a questão.

2. Gerenciador de Questões

Execute:
```bash
python selecao_questoes.py
```


  - Digite a Matéria e o Nível.

  - Clique em Buscar Questões.

  - Selecione uma questão da lista e visualize.

  - Clique em Adicionar Questão para exportar para prova.txt e provaGABARITO.txt.

---

## 📌 Observações Importantes

As pastas QUESTÕES e GABARITOS devem existir e conter os arquivos no formato:

  - Matéria-Nivel-ID.txt (questão)

  - Matéria-Nivel-IDGABARITO.txt (gabarito correspondente)

Para usar o ChatGPT integrado, é necessário ter Google Chrome instalado.

---

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou enviar PRs com melhorias.


























