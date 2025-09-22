import streamlit as st
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Agora você pode importar módulos a partir da raiz do projeto
from src.api.google_books import buscar_livros

st.title("📘 Libris – Recomendador de Livros")
query = st.text_input("Digite um livro que você gosta:")

if query:
    resultados = buscar_livros(query)
    for item in resultados.get("items", [])[:5]:
        st.write(f"📖 {item['volumeInfo']['title']}")