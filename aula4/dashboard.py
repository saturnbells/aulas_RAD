# -*- coding: utf-8 -*-
"""dashboard de funcionários"""

import streamlit as st
import pandas as pd
import numpy as np

# -------------------------------------------------------------------
# 1. configuração da página
# -------------------------------------------------------------------

st.set_page_config(page_title="dashboard de funcionários", layout="wide")
st.title("📊 dashboard de análise de Ffncionários")

# -------------------------------------------------------------------
# 2. carregar e tratar os dados (com cache)
# -------------------------------------------------------------------

@st.cache_data
def carregar_dados():
    # dados brutos
    dados = {
        "nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"],
        "idade": [23, 35, 29, np.nan, 40],
        "cidade": ["SP", "RJ", "SP", "MG", "RJ"],
        "salario": [3000, 5000, 4000, 3500, np.nan],
        "data_contratacao": pd.to_datetime([
            "2020-01-10", "2019-03-15", "2021-07-22", "2018-11-30", "2022-05-10"
        ])
    }
    df = pd.DataFrame(dados)

    # tratar valores nulos
    df["idade"] = df["idade"].fillna(df["idade"].mean())
    df["salario"] = df["salario"].fillna(df["salario"].median())

    # feature engineering
    df["salario_anual"] = df["salario"] * 12
    df["ano_contratacao"] = df["data_contratacao"].dt.year

    def classificar_salario(x):
        if x > 4500:
            return "Alto"
        elif x > 3000:
            return "Médio"
        else:
            return "Baixo"

    df["categoria_salario"] = df["salario"].apply(classificar_salario)

    return df

df = carregar_dados()

# -------------------------------------------------------------------
# 3. filtros na barra lateral
# -------------------------------------------------------------------
st.sidebar.header("🔎 Filtros")

cidades = st.sidebar.multiselect(
    "selecione a cidade",
    options=df["cidade"].unique(),
    default=df["cidade"].unique()
)

faixa_salario = st.sidebar.slider(
    "faixa salarial",
    float(df["salario"].min()),
    float(df["salario"].max()),
    (float(df["salario"].min()), float(df["salario"].max()))
)

df_filtrado = df[
    (df["cidade"].isin(cidades)) &
    (df["salario"] >= faixa_salario[0]) &
    (df["salario"] <= faixa_salario[1])
]

# -------------------------------------------------------------------
# 4. KPIs (indicadores principais)
# -------------------------------------------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("💰 salário médio", f"R$ {df_filtrado['salario'].mean():.2f}")
col2.metric("👥 total funcionários", df_filtrado.shape[0])
col3.metric("📈 salário máximo", f"R$ {df_filtrado['salario'].max():.2f}")

# -------------------------------------------------------------------
# 5. tabela de dados
# -------------------------------------------------------------------
st.subheader("📋 dados")
st.dataframe(df_filtrado, use_container_width=True)

# -------------------------------------------------------------------
# 6. gráficos de análise
# -------------------------------------------------------------------
st.subheader("📊 análises")
col1, col2 = st.columns(2)

# média salarial por cidade
col1.bar_chart(df_filtrado.groupby("cidade")["salario"].mean())

# distribuição por categoria de salário
col2.bar_chart(df_filtrado["categoria_salario"].value_counts())

# -------------------------------------------------------------------
# 7. tabela dinâmica (pivot)
# -------------------------------------------------------------------
st.subheader("📌 tabela dinâmica")
pivot = pd.pivot_table(
    df_filtrado,
    values="salario",
    index="cidade",
    columns="categoria_salario",
    aggfunc="mean"
)
st.dataframe(pivot)

# -------------------------------------------------------------------
# 8. download dos dados filtrados
# -------------------------------------------------------------------
st.subheader("⬇️ download dos dados")
csv = df_filtrado.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Baixar CSV",
    data=csv,
    file_name="dados_filtrados.csv",
    mime="text/csv"
)

# -------------------------------------------------------------------
# 9. upload de arquivo próprio (CSV)
# -------------------------------------------------------------------
st.sidebar.subheader("📂 upload de csv")
uploaded_file = st.sidebar.file_uploader("envie um csv", type=["csv"])

if uploaded_file:
    df_upload = pd.read_csv(uploaded_file)
    st.write("📄 Dados carregados:")
    st.dataframe(df_upload)
