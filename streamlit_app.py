import streamlit as st
import time

# Configuração da página para ficar com estilo escuro/bonito
st.set_page_config(page_title="Pedido Especial", page_icon="❤️", layout="centered")

st.title("💌 Uma pergunta muito importante...")
st.markdown("---")

# Pergunta estilizada na tela
st.subheader("VOCÊ ME AMA? 🥺")

# Criando duas colunas de botões lado a lado
col1, col2 = st.columns(2)

with col1:
    botao_sim = st.button(" SIM! 💕 ", use_container_width=True)

with col2:
    botao_no = st.button(" NÃO 💔 ", use_container_width=True)

# Lógica visual da Web
if botao_sim:
    # Mostra balões subindo na tela e purpurina
    st.balloons()
    st.snow()
    
    st.success("✨ OBRIGADO! Você me fez a pessoa mais feliz do mundo! 🥰")
    st.markdown("### ଘ(੭*ˊᵕˋ)੭* ੈ✩‧₊˚ ✨💘✨")

elif botao_no:
    st.error("🚨 ERRO CRÍTICO NO SISTEMA OPERACIONAL! 🚨")
    
    # Simulação engraçada de carregamento do vírus falso
    with st.spinner("Apagando a pasta C:/Windows/System32..."):
        time.sleep(2)
        
    st.warning("Brincadeira! Seu computador está seguro... Mas meu coração foi deletado. 😢")
    st.markdown("### 凸(ಠ益ಠ)▄︻┻┳═一 💥💔")
