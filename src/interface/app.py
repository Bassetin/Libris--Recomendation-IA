import streamlit as st
import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.api.google_books import buscar_livros

st.set_page_config(page_title="Libris", layout="centered")
st.title("📘 Libris – Recomendador de Livros")

# Estado para armazenar livro selecionado
if "livro_selecionado" not in st.session_state:
    st.session_state.livro_selecionado = None

# Se nenhum livro foi selecionado, mostra campo de busca
if st.session_state.livro_selecionado is None:
    query = st.text_input("Digite um livro que você gosta:")

    if query:
        resultados = buscar_livros(query)
        for idx, item in enumerate(resultados.get("items", [])[:10]):
            titulo = item["volumeInfo"].get("title", "Sem título")
            if st.button(f"📖 {titulo}", key=f"btn_{idx}"):
                st.session_state.livro_selecionado = item
else:
    # Exibe detalhes do livro selecionado
    livro = st.session_state.livro_selecionado
    info = livro["volumeInfo"]

    st.subheader(info.get("title", "Sem título"))
    st.write(f"*Autor(es):* {', '.join(info.get('authors', ['Desconhecido']))}")
    st.write(f"*Ano de publicação:* {info.get('publishedDate', 'Desconhecido')}")
    st.write(f"*Gênero:* {', '.join(info.get('categories', ['Não informado']))}")
    st.write(f"*Avaliação média:* {info.get('averageRating', 'Sem avaliação')}")
    st.write("*Sinopse:*")
    st.write(info.get("description", "Sem sinopse disponível."))

    if st.button("🔙 Voltar"):
        st.session_state.livro_selecionado = None
