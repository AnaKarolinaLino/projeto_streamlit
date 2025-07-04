import streamlit as st

st.set_page_config(page_title="Projeto Streamlit", layout="wide")
st.markdown("# Testando o Streamlit")

def main():
  abas = st.tabs([
    "Clientes",
    "Cadastrar Cliente",
    "Editar",
    "Deletar"
  ])

  with abas[0]:
    st.title("Clientes")
  
  with abas[1]:
    st.title("Cadastar Clientes")

    with st.form(key='add_cliente', clear_on_submit=True):
      nome = st.text_input("Nome", placeholder="Nome")
      email = st.text_input("Email", placeholder="Email")
      idade = st.number_input("Idade", placeholder="Idade", format="%d", step=1)
      telefone = st.number_input("Telefone", placeholder="Telefone", format="%d", step=1)
      profissao = st.selectbox("Selecione a Profissão", options=[
        "Desenveldor Web", "Analista de Infraestrutura",
        "DBA Senior", "Tecnico de Informatica"
      ])
      btn_cadastrar = st.form_submit_button("Cadastrar Cliente")

      if btn_cadastrar:
        if not nome or not email or idade == 0:
            st.error("Todos os campos precisam ser preenchidos")
        else:
            data_cliente = {
        "nome": nome,
        "email": email,
        "idade": idade,
        "telefone": telefone,
        "profissao": profissao
      }

            st.write(data_cliente)
  


# if btn_cadastrar:
    #   if not nome or not email or idade == 0:
    #     st.error("Preencha todos campos para Realizar o Cadastro")
    #   else:






  with abas[2]:
    st.title("Editar")
  
  with abas[3]:
    st.title("Deletar")

main()

