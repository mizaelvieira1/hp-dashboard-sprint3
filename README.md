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
