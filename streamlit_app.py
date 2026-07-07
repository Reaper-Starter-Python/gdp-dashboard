import streamlit as st

# Configuração visual da página do site
st.set_page_config(page_title="Validação de Acesso", page_icon="🔒", layout="centered")

st.title("🛡️ Sistema de Verificação de Entrada")
st.markdown('=' * 45)

# 1. Campo para o usuário digitar a idade (Substitui o input numérico)
idade = st.number_input("👉 Qual sua idade?", min_value=0, max_value=120, value=0, step=1)
st.markdown('=' * 45)

# Verificação de segurança da idade
if idade >= 18:
    # Se for maior de idade, o acesso é liberado e mostra o resto do formulário
    st.success("Acesso Liberado 🔓")
    st.markdown('=' * 45)
    
    # Campo de texto na web para a pergunta do Lucas
    lu = st.text_input("❓ O Lucas dá o cu 👉👌?").lower().strip()
    
    s = 'queima muito🔥'
    n = 'A gente está falando do mesmo 🏳️‍🌈Lucas🏳️‍🌈?'
    
    # Só exibe o resultado se o usuário já tiver digitado alguma coisa
    if lu != "":
        if lu == 'sim' or lu == 's':
            st.warning(f"O Lucas {s}")
        elif lu == 'não' or lu == 'nao' or lu == 'n':
            st.info(f"{n}")
        else:
            st.error("🤦‍♂️ Estamos falando do cu do Lucas 🏳️‍🌈⚧!!!")

elif idade > 0 and idade < 18:
    # Se for menor de idade e já tiver digitado um número maior que zero
    st.error("Acesso Bloqueado 🔒")
    st.stop() # Esse comando para a execução do site aqui para menores de idade
