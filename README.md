# 📊 HP Dashboard – Sprint 3 (Governança + Analytics)

Este projeto foi desenvolvido como entregável da **Sprint 3** da disciplina *Governança em IA e Business Analytics (FIAP)*.  
O objetivo é consolidar, em um único dashboard executivo, os resultados do piloto de detecção de **produtos HP falsificados em marketplaces**.  

O painel foi construído em **Streamlit** e aborda não apenas os indicadores de negócio, mas também aspectos de **governança, fairness e ética na IA**.

---

## 🗂️ Estrutura do Dashboard

### 🔍 Filtros Globais
- Período (Mês)
- Região/UF
- Linha de Produto (Cartucho / Toner)
- Canal (E-commerce / Loja / Suporte)
- Produto (Original / Falso)
- Severidade do chamado

### 📈 Página 1 – Visão Geral
- KPIs do modelo: Precisão, Recall, FPR, FNR  
- Tickets e Devoluções (Metas vs Realizado)  
- Tendência temporal (série completa ou período filtrado)

### ⚙️ Página 2 – Detecção & Operação
- Matriz de confusão (simulada)  
- Tempo médio de detecção  
- Fila de revisão humana  
- Taxa de override  

### 🛡️ Página 3 – Governança & Fairness
- Chamados e Devoluções por Região  
- **Fairness:** Taxa de Devolução (%) por Região  
- Monitoramento de deriva (simulado)  
- **Model Card** (objetivo, dados usados, limites)  
- **LGPD Mini** (base legal, minimização, retenção)

### 💰 Página 4 – Negócio & ROI
- Comparativo **Com Ação vs Sem Ação** (Chamados, Devoluções, NPS, Custos)  
- ROI e Payback estimados dinamicamente  
- Recomendação executiva **Go / No-Go**

### 🌍 Página 5 – Incidência & Evidências
- Mapa regional de ocorrências (PyDeck)  
- Botões de download: CSV dos dados filtrados + Resumo Executivo (txt)  
- Campo de **anotações e insights**

---

## 🚀 Como executar localmente

### 1. Clone o repositório
```bash
git clone https://github.com/SEU-USUARIO/hp-dashboard-sprint3.git
cd hp-dashboard-sprint3
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv .venv
.\.venv\Scriptsctivate   # Windows
source .venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o dashboard
```bash
streamlit run app.py
```

O app ficará disponível em: [http://localhost:8501](http://localhost:8501)

---

## 🌐 Deploy Online
O projeto foi publicado em **Streamlit Community Cloud**, disponível em:  
👉 [Acesse o Dashboard aqui](https://seu-link.streamlit.app)  

---

## 📌 Tecnologias utilizadas
- [Streamlit](https://streamlit.io/)  
- [Pandas](https://pandas.pydata.org/)  
- [Matplotlib](https://matplotlib.org/)  
- [Seaborn](https://seaborn.pydata.org/)  
- [PyDeck](https://deckgl.readthedocs.io/en/latest/)  

---

## ✨ Autor
Projeto desenvolvido por:

- Cristiano Washington Dias - RM555992 
- José Enrico dos Santos Tavares - RM554471 
- Lucas Hidetoshi Ichiama - RM555077 
- Marcia Ricardo Rosano - RM557464 
- Mizael Vieira Bezerra - RM555796 
- Santiago Nascimento Bernardes - RM557447 

como parte do curso de **Governança em IA e Business Analytics – FIAP**.  
