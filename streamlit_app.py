import streamlit as st

# Configuração visual com o tema de amor
st.set_page_config(page_title="Nosso Espaço 💕", page_icon="❤️", layout="centered")

st.title("🔒 Sistema de Verificação Especial")
st.markdown('=' * 45)

# 🔥 CORREÇÃO: Mudamos para text_input para aceitar as barras da data
data_namoro = st.text_input("👉 Qual a data do nosso aniversário de namoro? (DD/MM/AAAA)").strip()
st.markdown('=' * 45)

# Verificação exata da data do aniversário de namoro
if data_namoro == '30/11/2023':
    # Efeito cascata de balões subindo no site ao acertar a data!
    st.balloons()
    
    st.success("Acesso Liberado 🔓 Bem-vinda ao nosso espaço!")
    st.markdown('=' * 45)

    # Pergunta romântica na web
    amor = st.text_input("❓ Você me ama? 🥺").lower().strip()

    s = 'Sempre soube disso. EU TAMBÉM TE AMO! 💖'
    n = 'Oxi, existe essa opção? 😒'

    # Só exibe o resultado se a pessoa já tiver digitado a resposta
    if amor != "":
        if amor in ['sim', 's', 'muito', 'com certeza']:
            # Caixa verde de sucesso absoluto
            st.success(f"🥰 {s}")
            st.markdown("### ଘ(=^‥^=)੭🐾✨")
        elif amor in ['não', 'nao', 'n', 'nem um pouco']:
            # Caixa amarela de aviso/brincadeira
            st.warning(f"🤨 {n}")
        else:
            # Caixa vermelha de erro se digitar outra coisa
            st.error("A resposta é simples: sim ou não! 😝")

elif data_namoro != "":
    # Se a pessoa digitou algo, mas errou a data de namoro
    st.error("Acesso Bloqueado 🔒 Data incorreta! Tente se lembrar... 😥")
