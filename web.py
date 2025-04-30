import streamlit as st

#Terminal > New Terminal > pip install streamlit > pressiona enter que irá instalar o Streamlit

st.set_page_config(page_title="Hello Word")

st.title("Olá Mundo!")

st.write("Hello Word! I am back!")

#para rodar o código no navegador, é necessário colocar a função streamlit run web.py, se fizer alguma alteração, apenas atualizar o navegador que a alteração irá aparecer.

nome = st.text_input('Qual seu nome?')
idade = st.number_input('Idade?', step=1, value=0, format="%d")

st.write(f'Olá {nome} de {idade} anos!')

st.write('Fale um pouco sobre você')
bio = st.text_area('')
