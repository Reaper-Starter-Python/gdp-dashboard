import streamlit as st

# Configuração visual da página do site
st.set_page_config(page_title="Validação de Acesso", page_icon="🔒", layout="centered")

st.title("🛡️ Sistema de Verificação de Entrada")
st.markdown('=' * 45)

# 1. Campo para o usuário digitar a idade (Substitui o input numérico)
idade = st.number_input("👉 Qual a data do nosso aniversário de namoro? ", min_value=0, max_value=120, value=0, step=1)
st.markdown('=' * 45)

# Verificação de segurança da idade
if idade == '30/11/2023':
    # Se for maior de idade, o acesso é liberado e mostra o resto do formulário
    st.success("Acesso Liberado 🔓")
    st.markdown('=' * 45)

    # Campo de texto na web para a pergunta do Lucas
    lu = st.text_input("❓Você me ama❓ ").lower().strip()

    s = 'Sempre soube disso. TE AMO'
    n = 'Oxi existe essa opção😒'

    # Só exibe o resultado se o usuário já tiver digitado alguma coisa
    if lu != "":
        if lu == 'sim' or lu == 's':
            st.warning(f"O Lucas {s}")
        elif lu == 'não' or lu == 'nao' or lu == 'n':
            st.info(f"{n}")
        else:
            st.error("A resposta é simples, sim ou não.")

