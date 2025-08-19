import streamlit as st
import pandas as pandas
import urllib.parse

st.set_page_config(layout="wide")

st.title("Grafico de videos do TikTok")

# Obter dados da URL
query_params = st.query_params()
data_string  = query_params.get("data", [""])[0]

if data_string:
    # Decodificar a string de dados
    data - eval(decoded_string)
    df = pd.Dataframe(data)
    df.set_index("video", implace=True)

    st.bar_chart(df)

else:
    st.warning("nenhum dado encontrado. Por favor, forneça os dados no formato correto.")