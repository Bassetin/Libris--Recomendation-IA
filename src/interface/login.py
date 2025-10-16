import streamlit as st

def mostrar_tela_login():
    st.title("🔐 Área de Login")

    usuario = st.text_input("Usuario")
    senha = st.text_input("Senha:", type="password")

    if st.button("Entrar"):
        if usuario == "admin" and senha == "123":
            st.session_state.logado = True
            st.session_state.usuario = usuario
            st.session_state.opcao = "Recomendar livros"
            st.success("Login feito com sucesso!")
            st.rerun()
        else:
            st.error("Usuario ou senha incorretos.")
    else:
        st.success("✅ Você já está logado.")
        if st.button("Sair"):
            st.session_state.logado = False
            st.info("Você saiu da conta.")