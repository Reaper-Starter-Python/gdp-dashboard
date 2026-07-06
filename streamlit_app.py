import streamlit as st

# Configuração da página estilo gatinho fofo pixel art
st.set_page_config(page_title="Pedido Pixel Art 🐾", page_icon="🐱", layout="centered")

# Links de GIFs estáveis de gatinhos em pixel art (Hospedados no GIPHY/Pinterest)
gato_piscando = "https://giphy.com"  # Gatinho fofo de pixel piscando
gato_coracao = "https://giphy.com"   # Gatinho comemorando com coração

# Título com estilo retrô/computador antigo
st.markdown("<h2 style='text-align: center; color: #ff69b4; font-family: monospace;'>(=ↀωↀ=) SYSTEM_NEKO_ONLINE </h2>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-family: sans-serif;'>QUER NAMORAR COMIGO? 🥺🐾</h1>", unsafe_allow_html=True)

# Centralizando o gatinho de pixel art inicial na tela
st.markdown(f"<div style='display: flex; justify-content: center;'><img src='{gato_piscando}' width='150'></div>", unsafe_allow_html=True)
st.write("")

# Injetando o código do botão fujão (HTML + JavaScript)
html_botao_fujao = """
<div style="display: flex; justify-content: center; gap: 30px; margin-top: 20px; height: 150px; position: relative;">
    
    <!-- Botão SIM: Comunica com o Streamlit -->
    <button onclick="parent.postMessage({type: 'streamlit:setComponentValue', value: 'sim'}, '*')" 
            style="background-color: #4CAF50; color: white; padding: 15px 32px; text-align: center; 
                   font-size: 18px; font-weight: bold; border: none; border-radius: 12px; cursor: pointer; height: 55px; font-family: monospace;">
        SIM! ✨🐱
    </button>

    <!-- Botão NÃO: O botão fujão -->
    <button id="btnNao" onmouseover="fugir()" onclick="fugir()"
            style="background-color: #f44336; color: white; padding: 15px 32px; text-align: center; 
                   font-size: 18px; font-weight: bold; border: none; border-radius: 12px; cursor: pointer; 
                   position: absolute; left: 55%; transition: all 0.1s ease; height: 55px; font-family: monospace;">
        NÃO 😿
    </button>
</div>

<script>
function fugir() {
    var btn = document.getElementById('btnNao');
    
    // Sorteia uma posição aleatória na tela do usuário
    var larguraAleatoria = Math.floor(Math.random() * 70) + 10;
    var alturaAleatoria = Math.floor(Math.random() * 60) + 20;
    
    btn.style.position = 'fixed';
    btn.style.left = larguraAleatoria + '%';
    btn.style.top = alturaAleatoria + '%';
}
</script>
"""

# Renderiza os botões e escuta as ações do JavaScript
clique = st.components.v1.html(html_botao_fujao, height=180)

# Verificação: Se o botão SIM for clicado, o Python assume o controle e faz a festa!
if str(clique).strip() == "sim" or "value='sim'" in str(clique):
    st.balloons() # Solta balões subindo na tela
    st.snow()     # Solta efeito de brilho caindo
    
    # Substitui a interface por uma mensagem de sucesso linda!
    st.success("MIAU! O gatinho de pixel art diz que você aceitou! 🎉💖")
    
    # Mostra o segundo gatinho comemorando com corações
    st.markdown(f"<div style='display: flex; justify-content: center;'><img src='{gato_coracao}' width='180'></div>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #ff1493;'>ଘ(=^‥^=)੭🐾 VOCÊ FEZ A ESCOLHA CERTA!</h2>", unsafe_allow_html=True)
