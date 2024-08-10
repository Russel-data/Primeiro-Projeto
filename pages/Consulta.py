import streamlit as st
import pandas as pd

dados = pd.read_csv("clientes.csv")

st.set_page_config(
    page_title="Consulta cadastro",
    page_icon="🔍"
)


st.title("Clientes cadastrados")
st.divider()

localizar = st.text_input("Digite o nome", key="localizar")

# Botões de pesquisa e exclusão
col1, col2 = st.columns(2)
btn_pesquisar = col1.button("Pesquisar", key="Pesquisa")
btn_excluir = col2.button("Excluir", key="Excluir")

# Executa a pesquisa quando o botão "Pesquisar" é clicado
if btn_pesquisar:
    # Filtra os dados com base no nome digitado
    dados_filtrados = dados[dados['nome'].str.contains(localizar, case=False, na=False)]
    
    # Verifica se encontrou algum cliente
    if not dados_filtrados.empty:
        st.dataframe(dados_filtrados)
        st.success("Cliente encontrado", icon="✅")
    else:
        st.error("Cliente não encontrado", icon="❌")

# Executa a exclusão quando o botão "Excluir" é clicado
if btn_excluir:
    # Filtra os dados com base no nome digitado
    dados_filtrados = dados[dados['nome'].str.contains(localizar, case=False, na=False)]
    
    # Verifica se encontrou algum cliente para excluir
    if not dados_filtrados.empty:
        # Exclui o cliente dos dados
        dados = dados[~dados['nome'].str.contains(localizar, case=False, na=False)]
        
        # Salva os dados atualizados de volta ao arquivo CSV
        dados.to_csv("clientes.csv", index=False)
        
        st.success("Cliente excluído com sucesso", icon="✅")
    else:
        st.error("Cliente não encontrado para exclusão", icon="❌")

# Exibe os dados atualizados
st.dataframe(dados)
