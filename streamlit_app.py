import streamlit as st

# Configuração da página estilo gatinho fofo
st.set_page_config(page_title="Pedido do Gatinho 🐾", page_icon="🐱", layout="centered")

# Título e Mensagem Inicial
st.markdown("<h2 style='text-align: center; color: #ff69b4;'>(=^-ω-^=) Nyah! Um pedido especial...</h2>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>VOCÊ ME AMA? 🥺🐾</h1>", unsafe_allow_html=True)
st.write("")

# Injetando o código mágico (HTML + JavaScript) para fazer o botão fugir
html_botao_fujao = """
<div style="display: flex; justify-content: center; gap: 30px; margin-top: 20px; height: 150px; position: relative;">
    
    <!-- Botão SIM: Envia um sinal para o Streamlit saber que foi clicado -->
    <button onclick="parent.postMessage({type: 'streamlit:setComponentValue', value: 'sim'}, '*')" 
            style="background-color: #4CAF50; color: white; padding: 15px 32px; text-align: center; 
                   font-size: 18px; font-weight: bold; border: none; border-radius: 12px; cursor: pointer; height: 55px;">
        SIM! ✨🐱
    </button>

    <!-- Botão NÃO: O botão fujão que se move sozinho com JavaScript -->
    <button id="btnNao" onmouseover="fugir()" onclick="fugir()"
            style="background-color: #f44336; color: white; padding: 15px 32px; text-align: center; 
                   font-size: 18px; font-weight: bold; border: none; border-radius: 12px; cursor: pointer; 
                   position: absolute; left: 55%; transition: all 0.1s ease; height: 55px;">
        NÃO 😿
    </button>
</div>

<script>
function fugir() {
    var btn = document.getElementById('btnNao');
    
    // Gera posições aleatórias na tela (entre 10% e 80% para não sumir do mapa)
    var larguraAleatoria = Math.floor(Math.random() * 70) + 10;
    var alturaAleatoria = Math.floor(Math.random() * 70) + 10;
    
    // Aplica a nova posição imediatamente
    btn.style.position = 'fixed';
    btn.style.left = larguraAleatoria + '%';
    btn.style.top = alturaAleatoria + '%';
}
</script>
"""

# Executa o HTML do botão fujão no site e guarda o clique do usuário
clique = st.components.v1.html(html_botao_fujao, height=180)

# Se o JavaScript avisar o Python que o botão "SIM" foi clicado:
if st.session_state.get("clique_sim") or str(clique).strip() == "sim" or "value='sim'" in str(clique):
    st.balloons()
    st.success("MIAU! Você aceitou! Agora somos o casal mais feliz do mundo! 💖(=^·ܫ·^=)ﾉ💰")
    st.markdown("<h2 style='text-align: center;'>ଘ(=^‥^=)੭🐾✨ PEGUE SEU CORAÇÃO!</h2>", unsafe_allow_html=True)
