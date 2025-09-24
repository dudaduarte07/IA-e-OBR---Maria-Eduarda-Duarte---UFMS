# IA-e-OBR---Maria-Eduarda-Duarte---UFMS
Projeto de extensão realizado como parte da graduação de Engenharia de Computação
Aluna: Maria Eduarda de Paula Duarte


# 1) Visão geral

Este repositório concentra o pipeline de criação, validação e exportação de questões para a OBR (Olimpíada Brasileira de Robótica), a partir de prompts estruturados. Ele cobre:

- Modelagem de templates de prompt (persona, estilo OBR, critérios de qualidade).

- Geração em lote (JSONL/CSV) de questões balanceadas por nível, tema e habilidade.

- Validação automática (lint semântico/estrutural, deduplicação, verificação de alternativa única correta).

- Pós-processamento (balanceamento, normalização de enunciado, formatação).

- Exportação para formatos comuns (CSV, JSONL).

# 2) Objetivos didáticos (OBR)

- Níveis: N1–N5 (ajustável).

- Áreas: lógica, algoritmos, programação, sensores, atuadores, eletrônica básica, planejamento, mecânica, ética/segurança.

- Habilidades: interpretação, decomposição de problemas, simulação mental, cálculo aproximado, análise de algoritmos, depuração.

Os prompts e validadores seguem rubricas de clareza, unicidade da resposta, contexto robótico realista, não ambiguidade e nível cognitivo (lembrar → aplicar → analisar).



# 3) Estrutura do projeto
IA E OBR/
├─ criar_questao/

│  ├─ prompt+questao.py

│  ├─ prompt.py

│  └─ selecao_questoes.py

├─ plataforma/

│  ├─ banco_questoes.html

│  ├─ comunidade.html

│  ├─ index.html

├  ├─ script.js

│  ├─ style.css

├  ├─ tarefas.html

│  └─ criar_questao.html

└─ README.md
