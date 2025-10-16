# =============================================
# 📘 LIBRIS — Sistema de Login + Recomendação
# =============================================

# ==== Importações básicas ====
import streamlit as st
import sys
import os

# ==== Configuração inicial da página ====
st.set_page_config(page_title="📘 Libris", layout="centered")

# ==== Ajuste de caminho (para importar o módulo buscar_livros) ====
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.api.google_books import buscar_livros


# =============================================
# 🔧 Inicialização de variáveis no session_state
# =============================================

if "logado" not in st.session_state:
    st.session_state.logado = False
if "pagina" not in st.session_state:
    st.session_state.pagina = "login"
if "usuario" not in st.session_state:
    st.session_state.usuario = ""
if "livro_selecionado" not in st.session_state:
    st.session_state.livro_selecionado = None


# =============================================
# 🔐 TELA DE LOGIN
# =============================================
def tela_login():
    """Mostra a tela de login do sistema."""

    st.title("🔐 Área de Login")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha:", type="password")

    if st.button("Entrar"):
        if usuario == "admin" and senha == "123":
            st.session_state.logado = True
            st.session_state.usuario = usuario
            st.session_state.pagina = "recomendador"
            st.success("✅ Login feito com sucesso!")
            st.rerun()
        else:
            st.error("❌ Usuário ou senha incorretos.")


# =============================================
# 📚 TELA DE RECOMENDAÇÃO DE LIVROS
# =============================================
def tela_recomendador():
    """Mostra a tela principal do recomendador de livros."""

    # === Barra lateral (informações e logout) ===
    st.sidebar.title(f"👋 Olá, {st.session_state.usuario}")
    if st.sidebar.button("Sair"):
        st.session_state.logado = False
        st.session_state.pagina = "login"
        st.session_state.livro_selecionado = None
        st.rerun()

    # === Título da página ===
    st.title("📘 Libris – Recomendador de Livros")

    # === Campo de busca ===
    if st.session_state.livro_selecionado is None:
        query = st.text_input("Digite um livro que você gosta:")

        if query:
            resultados = buscar_livros(query)

            for idx, item in enumerate(resultados.get("items", [])[:10]):
                info = item.get("volumeInfo", {})
                titulo = info.get("title", "Sem título")
                autores = ", ".join(info.get("authors", ["Desconhecido"]))
                imagem = info.get("imageLinks", {}).get("thumbnail", None)
                descricao = info.get("description", "Sem descrição disponível.")[:150] + "..."

                with st.container():
                    cols = st.columns([1, 4])

                    with cols[0]:
                        if imagem and imagem.startswith("http"):
                            st.image(imagem, width=100)
                        else:
                            st.image("https://via.placeholder.com/120x180?text=Sem+Capa", width=100)

                    with cols[1]:
                        st.markdown(f"### {titulo}")
                        st.markdown(f"**Autor(es):** {autores}")
                        st.markdown(f"_{descricao}_")

                        if st.button(f"📖 Ver mais sobre '{titulo}'", key=f"btn_{idx}"):
                            st.session_state.livro_selecionado = item
                            st.rerun()

    # === Exibição dos detalhes do livro selecionado ===
    else:
        livro = st.session_state.livro_selecionado
        info = livro["volumeInfo"]

        titulo = info.get("title", "Sem título")
        autores = ", ".join(info.get("authors", ["Desconhecido"]))
        imagem = info.get("imageLinks", {}).get("thumbnail", None)

        # Exibe capa e título
        st.markdown(f"## {titulo}")
        if imagem and imagem.startswith("http"):
            st.image(imagem, width=150)
        else:
            st.image("https://via.placeholder.com/150x220?text=Sem+Capa", width=150)

        # Informações do livro
        st.write(f"**Autor(es):** {autores}")
        st.write(f"**Ano de publicação:** {info.get('publishedDate', 'Desconhecido')}")
        st.write(f"**Gênero:** {', '.join(info.get('categories', ['Não informado']))}")
        st.write(f"**Avaliação média:** {info.get('averageRating', 'Sem avaliação')}")
        st.markdown("### 📖 Sinopse:")
        st.write(info.get("description", "Sem sinopse disponível."))

        if st.button("🔙 Voltar"):
            st.session_state.livro_selecionado = None
            st.rerun()


# =============================================
# 🧭 CONTROLE DE NAVEGAÇÃO ENTRE AS TELAS
# =============================================
if st.session_state.pagina == "login":
    tela_login()

elif st.session_state.pagina == "recomendador" and st.session_state.logado:
    tela_recomendador()

else:
    st.session_state.pagina = "login"
    st.rerun()
