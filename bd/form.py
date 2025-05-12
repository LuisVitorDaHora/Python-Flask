import streamlit as st
import dados

st.title("Jogos")

nome = st.text_input("Nome do jogo")
ano = st.number_input("Ano de lançamento", min_value=1900, max_value=2025)
nota = st.slider("Nota", min_value=0.0, max_value=10.0)
genero = st.selectbox("Gênero", ["Ação", "Aventura", "RPG", "Estratégia", "Outros"])

if st.button("Adicionar Jogo"):
    dados.insere_dados(nome, ano, nota, genero)
    st.success("Jogo adicionado com sucesso!")

games = dados.obter_dados()
st.header("Lista de Jogos")
st.table(games)