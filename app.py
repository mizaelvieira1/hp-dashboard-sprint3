import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk

# -----------------------------
# Configuração inicial do app
# -----------------------------
st.set_page_config(
    page_title="Dashboard - Sprint 3",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CSS customizado estilo HP
# -----------------------------
st.markdown(
    """
    <style>
    /* Fundo geral */
    .main {
        background-color: #FFFFFF;
    }

    /* Títulos */
    h1, h2, h3, h4 {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        color: #000000;
    }

    /* Texto */
    p, div, span {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        color: #333333;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #F5F5F5;
    }

    /* Botões */
    button[kind="primary"] {
        background-color: #0096D6;
        color: white;
        border-radius: 5px;
        font-weight: bold;
    }
    button[kind="primary"]:hover {
        background-color: #007bb3;
        color: white;
    }

    /* Métricas */
    div[data-testid="stMetricValue"] {
        color: #0096D6;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Título principal
# -----------------------------
st.title("📊 Painel Executivo - Sprint 3")
st.markdown("Este painel consolida governança, analytics e impacto de negócio (HP - Produtos Falsificados).")


# -----------------------------
# Sidebar - Filtros
# -----------------------------
st.sidebar.header("🔍 Filtros")

periodo = st.sidebar.selectbox("Período", ["Jan/2025", "Fev/2025", "Mar/2025"])
regiao = st.sidebar.multiselect("Região/UF", ["Sudeste", "Norte", "Sul", "Nordeste", "Centro-Oeste"])
produto = st.sidebar.radio("Linha de Produto", ["Cartucho", "Toner"])
canal = st.sidebar.selectbox("Canal", ["E-commerce", "Loja", "Suporte"])
tipo_cartucho = st.sidebar.radio("Produto", ["Original", "Falso"])
severidade = st.sidebar.select_slider("Severidade do chamado", options=["Baixa", "Média", "Alta"])

st.sidebar.markdown("---")
st.sidebar.info("Os filtros aplicados afetam todas as páginas do dashboard.")

# -----------------------------
# Dados simulados (base única para todas as páginas)
# -----------------------------
base = []
meses = ["Jan/2025", "Fev/2025", "Mar/2025"]
regioes = ["Sudeste", "Norte", "Sul", "Nordeste", "Centro-Oeste"]
produtos = ["Cartucho", "Toner"]
canais = ["E-commerce", "Loja", "Suporte"]
tipos = ["Original", "Falso"]
severidades = ["Baixa", "Média", "Alta"]

import random
for m in meses:
    for r in regioes:
        for p in produtos:
            for c in canais:
                for t in tipos:
                    for s in severidades:
                        chamados = random.randint(20, 160)
                        devolucoes = random.randint(10, 80)
                        base.append([m, r, p, c, t, s, chamados, devolucoes])

dados_base = pd.DataFrame(base, columns=["Mês","Região","Produto","Canal","Tipo","Severidade","Chamados","Devoluções"])

# -----------------------------
# Aplica filtros globais
# -----------------------------
dados_filtrados = dados_base.copy()

if periodo:
    dados_filtrados = dados_filtrados[dados_filtrados["Mês"] == periodo]
if regiao:
    dados_filtrados = dados_filtrados[dados_filtrados["Região"].isin(regiao)]
if produto:
    dados_filtrados = dados_filtrados[dados_filtrados["Produto"] == produto]
if canal:
    dados_filtrados = dados_filtrados[dados_filtrados["Canal"] == canal]
if tipo_cartucho:
    dados_filtrados = dados_filtrados[dados_filtrados["Tipo"] == tipo_cartucho]
if severidade:
    dados_filtrados = dados_filtrados[dados_filtrados["Severidade"] == severidade]

# -----------------------------
# Estrutura de páginas (abas)
# -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Visão Geral",
    "⚙️ Detecção & Operação",
    "🛡️ Governança & Fairness",
    "💰 Negócio & ROI",
    "🌍 Incidência & Evidências"
])

# -----------------------------
# Página 1 – Visão Geral
# -----------------------------
with tab1:
    st.subheader("KPIs do Piloto")

    tickets_total = dados_filtrados["Chamados"].sum()
    devolucoes_total = dados_filtrados["Devoluções"].sum()

    # ---- KPIs do Modelo (simulados) ----
    precisao = 0.92
    recall = 0.88
    fpr = 0.07
    fnr = 0.12

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🎯 Precisão", f"{precisao*100:.1f}%")
    with col2:
        st.metric("📈 Recall", f"{recall*100:.1f}%")
    with col3:
        st.metric("⚠️ FPR", f"{fpr*100:.1f}%")
    with col4:
        st.metric("⚠️ FNR", f"{fnr*100:.1f}%")

    st.markdown("---")
    st.subheader("Metas vs Realizado")

    meta_tickets = 500
    meta_devolucoes = 100

    col5, col6 = st.columns(2)
    with col5:
        st.metric("Tickets", tickets_total, delta=f"{tickets_total-meta_tickets}")
        st.caption(f"Meta: {meta_tickets}")
    with col6:
        st.metric("Devoluções", devolucoes_total, delta=f"{devolucoes_total-meta_devolucoes}")
        st.caption(f"Meta: {meta_devolucoes}")

    st.markdown("---")
    st.subheader("Tendência temporal")

    modo_tendencia = st.radio(
        "Modo de exibição:",
        ["Série completa", "Apenas período selecionado"],
        horizontal=True
    )

    if modo_tendencia == "Série completa":
        dados_tendencia = dados_base.copy()
    else:
        dados_tendencia = dados_filtrados.copy()

    # aplica filtros adicionais
    if regiao:
        dados_tendencia = dados_tendencia[dados_tendencia["Região"].isin(regiao)]
    if produto:
        dados_tendencia = dados_tendencia[dados_tendencia["Produto"] == produto]
    if canal:
        dados_tendencia = dados_tendencia[dados_tendencia["Canal"] == canal]
    if tipo_cartucho:
        dados_tendencia = dados_tendencia[dados_tendencia["Tipo"] == tipo_cartucho]
    if severidade:
        dados_tendencia = dados_tendencia[dados_tendencia["Severidade"] == severidade]

    serie = dados_tendencia.groupby("Mês")[["Chamados","Devoluções"]].sum().reset_index()

    if not serie.empty:
        fig, ax = plt.subplots(figsize=(5,3))
        ax.plot(serie["Mês"], serie["Chamados"], marker="o", label="Chamados")
        ax.plot(serie["Mês"], serie["Devoluções"], marker="s", label="Devoluções")
        ax.set_ylabel("Volume")
        ax.set_title("Chamados e Devoluções ao longo dos meses")
        ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
        st.pyplot(fig, use_container_width=False)
    else:
        st.info("Nenhum dado disponível com os filtros aplicados.")



# -----------------------------
# Página 2 – Detecção & Operação
# -----------------------------
with tab2:
    st.subheader("Matriz de Confusão (simulada)")

    matriz = [[420, 80],
              [50, 150]]

    fig, ax = plt.subplots(figsize=(5,3))
    sns.heatmap(matriz, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Pred. Original", "Pred. Falso"],
                yticklabels=["Real Original", "Real Falso"],
                ax=ax)
    ax.set_title("Matriz de Confusão")
    st.pyplot(fig, use_container_width=False)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("⏱️ Tempo médio de detecção", "2.3s")
        st.metric("👥 Fila de revisão humana", "35 casos pendentes")
    with col2:
        st.metric("🔄 Taxa de override", "8%")
        st.metric("📦 Processados no mês", f"{tickets_total}")

# -----------------------------
# Página 3 – Governança & Fairness
# -----------------------------
with tab3:
    st.subheader("Desempenho por Região")

    desempenho = dados_filtrados.groupby("Região")[["Chamados","Devoluções"]].sum().reset_index()
    if not desempenho.empty:
        fig, ax = plt.subplots(figsize=(5,3))
        ax.bar(desempenho["Região"], desempenho["Chamados"], alpha=0.7, label="Chamados")
        ax.bar(desempenho["Região"], desempenho["Devoluções"], alpha=0.7, label="Devoluções")
        ax.set_ylabel("Volume")
        ax.set_title("Chamados e Devoluções por Região")
        ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
        st.pyplot(fig, use_container_width=False)
    else:
        st.info("Nenhum dado disponível com os filtros aplicados.")

    st.markdown("---")
    st.subheader("📊 Fairness – Diferença de Taxas por Região")

    if not desempenho.empty:
        desempenho["Taxa_devolucao_%"] = (desempenho["Devoluções"] / desempenho["Chamados"] * 100).round(1)
        st.dataframe(desempenho[["Região","Chamados","Devoluções","Taxa_devolucao_%"]], use_container_width=True)

        fig2, ax2 = plt.subplots(figsize=(5,3))
        ax2.bar(desempenho["Região"], desempenho["Taxa_devolucao_%"], color="orange", alpha=0.7)
        ax2.set_ylabel("% Devoluções / Chamados")
        ax2.set_title("Taxa de Devolução por Região (Fairness)")
        st.pyplot(fig2, use_container_width=False)

    st.markdown("---")
    st.subheader("Sinal de Deriva (simulado)")

    deriva = pd.DataFrame({
        "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
        "Precisão": [0.90, 0.89, 0.87, 0.85, 0.82, 0.80]
    })

    fig3, ax3 = plt.subplots(figsize=(5,3))
    ax3.plot(deriva["Mês"], deriva["Precisão"], marker="o", color="red")
    ax3.axhline(0.85, color="gray", linestyle="--", label="Limite aceitável")
    ax3.set_ylabel("Precisão")
    ax3.set_title("Evolução da Precisão (monitoramento de deriva)")
    ax3.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    st.pyplot(fig3, use_container_width=False)

    st.markdown("---")
    with st.expander("📄 Model Card"):
        st.markdown("""
        **Objetivo:** Detectar cartuchos falsificados no marketplace.  
        **Dados usados:** Chamados técnicos, devoluções, tempo de uso, origem da compra.  
        **Limites de uso:**  
        - Apenas para cartuchos HP.  
        - Não substitui verificação manual em casos críticos.  
        """)

    with st.expander("🛡️ LGPD Mini"):
        st.markdown("""
        - **Base legal:** Legítimo interesse na proteção da marca e consumidores.  
        - **Minimização:** Apenas dados técnicos anonimizados.  
        - **Retenção:** Dados armazenados por 12 meses e depois descartados.  
        """)


# -----------------------------
# Página 4 – Negócio & ROI
# -----------------------------
with tab4:
    st.subheader("Comparativo de Impacto (dinâmico com filtros)")

    # valores do filtro
    chamados = dados_filtrados["Chamados"].sum()
    devolucoes = dados_filtrados["Devoluções"].sum()

    # simulações dinâmicas
    nps_sem = max(-10, 60 - int(devolucoes*0.05))   # piora com mais devoluções
    nps_com = nps_sem + 20                         # melhora com ação
    custo_sem = 1000*chamados + 2000*devolucoes    # custo proporcional ao volume
    custo_com = int(custo_sem*0.5)                 # redução de 50%

    impacto = pd.DataFrame({
        "Métrica": ["Chamados", "Devoluções", "NPS", "Custo Suporte (R$)"],
        "Com Ação": [int(chamados*0.65), int(devolucoes*0.5), nps_com, custo_com],
        "Sem Ação": [chamados, devolucoes, nps_sem, custo_sem]
    })

    # tabela dinâmica
    st.dataframe(impacto, use_container_width=True)

    st.markdown("---")
    # -----------------------------
    # Gráfico 1 - Chamados, Devoluções, NPS
    # -----------------------------
    subset1 = impacto[impacto["Métrica"].isin(["Chamados","Devoluções","NPS"])]

    fig1, ax1 = plt.subplots(figsize=(5,3))
    x = range(len(subset1["Métrica"]))
    ax1.bar(x, subset1["Com Ação"], width=0.35, label="Com Ação", color="green", alpha=0.7)
    ax1.bar([i+0.35 for i in x], subset1["Sem Ação"], width=0.35, label="Sem Ação", color="red", alpha=0.7)
    ax1.set_xticks([i+0.35/2 for i in x])
    ax1.set_xticklabels(subset1["Métrica"])
    ax1.set_ylabel("Valores")
    ax1.set_title("Comparativo - Chamados, Devoluções e NPS")
    ax1.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    st.pyplot(fig1, use_container_width=False)

    st.markdown("---")
    # -----------------------------
    # Gráfico 2 - Custos
    # -----------------------------
    subset2 = impacto[impacto["Métrica"]=="Custo Suporte (R$)"]

    fig2, ax2 = plt.subplots(figsize=(5,3))
    x = range(len(subset2["Métrica"]))
    ax2.bar(x, subset2["Com Ação"], width=0.35, label="Com Ação", color="green", alpha=0.7)
    ax2.bar([i+0.35 for i in x], subset2["Sem Ação"], width=0.35, label="Sem Ação", color="red", alpha=0.7)
    ax2.set_xticks([i+0.35/2 for i in x])
    ax2.set_xticklabels(subset2["Métrica"])
    ax2.set_ylabel("R$")
    ax2.set_title("Comparativo - Custo de Suporte")
    ax2.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    st.pyplot(fig2, use_container_width=False)

    st.markdown("---")
    # ROI e Payback calculados dinamicamente
    roi = round(((custo_sem - custo_com) / custo_com) * 100, 1) if custo_com > 0 else 0
    payback = "8 meses" if roi > 0 else "N/A"

    col1, col2 = st.columns(2)
    with col1:
        st.metric("ROI estimado", f"{roi}%")
    with col2:
        st.metric("Payback", payback)

    st.markdown("---")
    st.success("Recomendação: **Go 🚀** - O modelo apresenta impacto positivo significativo.")

# -----------------------------
# Página 5 – Incidência & Evidências
# -----------------------------
with tab5:
    st.subheader("🗺️ Mapa de Incidência Regional")

    mapa_data = dados_filtrados.groupby("Região")[["Chamados"]].sum().reset_index()
    mapa_data["lat"] = mapa_data["Região"].map({
        "Sudeste": -23.55, "Norte": -3.12, "Sul": -30.0,
        "Nordeste": -8.05, "Centro-Oeste": -15.6
    })
    mapa_data["lon"] = mapa_data["Região"].map({
        "Sudeste": -46.63, "Norte": -50.0, "Sul": -51.2,
        "Nordeste": -34.9, "Centro-Oeste": -47.9
    })

    # 🚨 remove linhas sem coordenadas
    mapa_data = mapa_data.dropna(subset=["lat","lon"])

    if not mapa_data.empty:
        import pydeck as pdk

        camada = pdk.Layer(
            "ScatterplotLayer",
            data=mapa_data,
            get_position='[lon, lat]',
            get_radius=80000 ,   # escala dos pontos
            get_fill_color='[255, 0, 0, 180]',  # vermelho forte
            get_line_color='[0, 0, 0]',         # borda preta
            line_width_min_pixels=2,
            pickable=True
        )

        view = pdk.ViewState(latitude=-15, longitude=-55, zoom=3)

        tooltip = {
            "html": "<b>Região:</b> {Região}<br/>"
                    "<b>Chamados:</b> {Chamados}",
            "style": {"backgroundColor": "white", "color": "black"}
        }

        st.pydeck_chart(pdk.Deck(
            layers=[camada],
            initial_view_state=view,
            map_style="light",   # fundo claro
            tooltip=tooltip
        ))
    else:
        st.info("Nenhum dado para plotar no mapa com os filtros aplicados.")

    st.markdown("---")
    st.subheader("⬇️ Downloads e Evidências")

    csv = dados_filtrados.to_csv(index=False).encode('utf-8-sig')
    st.download_button("Baixar CSV - Dados Filtrados", csv, "dados_filtrados.csv", "text/csv")

    resumo = f"""
    Resumo Executivo - Sprint 3

    O modelo de detecção de cartuchos falsificados mostrou impacto positivo:
    - Chamados totais (filtro): {dados_filtrados['Chamados'].sum()}
    - Devoluções totais (filtro): {dados_filtrados['Devoluções'].sum()}
    - ROI estimado em 100% e Payback em 8 meses.

    Recomendação Executiva: GO 🚀
    """
    st.download_button("Baixar Resumo Executivo (txt)", resumo, "resumo_executivo.txt")

    st.markdown("---")
    st.subheader("📝 Anotações e Insights")
    insight = st.text_area("Digite aqui seus insights...", "")
    if st.button("Salvar Insight"):
        st.success("Insight registrado: " + insight)

