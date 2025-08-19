import streamlit as st
import pandas as pandas
import urllib.parse
import json

st.set_page_config(layout="wide")

st.title("Grafico de videos do TikTok")

# Obter dados da URL
query_params = st.query_params

if "data" in query_params:
    
    data_string = query_params.get("data")

    #decodificar a string de dados
    try:
        decoded_string = urllib.parse.unquote(data_string)
        data = json.loads(decoded_string)
        df =  pd.dataframe(data)
        df.set_index("video", inplace=True)

        st.bar_chart(df)

    except (urllib.error.URLError, json.JSONDecodeError, KeyError) as e:
        st.error(f"Erro ao processar os dados: {e}")
        st.warning("Certifique-se de que os dados estão no formato correto.")

else:
    st.warning("Nenhum dado encontrado. Por favor, forneça os dados no formato correto.")