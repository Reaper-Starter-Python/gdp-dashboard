import streamlit as st

# Título do Site
st.title('📅 Meu Gerenciador de Tarefas Diárias')
st.markdown('---')

# As suas variáveis com as tarefas
seg = 'Tomar café, Tomar banho, Estudar programação'
ter = 'Tomar café, Tomar banho, Estudar LIBRAS'
qua = 'Tomar café, Tomar banho, Estudar sobre Cyberdecks'
qui = 'Tomar café, Tomar banho, Estudar Hardware'
sex = 'Tomar café, Tomar banho, Estudar Francês'

# Criando um menu de seleção no site para o seu amigo clicar
dia_selecionado = st.selectbox(
    'Deseja ver as tarefas de qual dia?',
    ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
)

st.markdown('### 📋 Suas obrigações de hoje:')

# Lógica dos IFs adaptada para a Web
if dia_selecionado == 'Segunda-feira':
    st.info(seg)
elif dia_selecionado == 'Terça-feira':
    st.info(ter)
elif dia_selecionado == 'Quarta-feira':
    st.info(qua)
elif dia_selecionado == 'Quinta-feira':
    st.info(qui)
elif dia_selecionado == 'Sexta-feira':
    st.info(sex)
