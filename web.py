import streamlit as st
import datetime

# Define a data mínima permitida (1º de janeiro de 1970)
data_minima = datetime.date(1970, 1, 1)

# Define a data máxima permitida (você pode ajustar conforme necessário,
# por exemplo, a data atual ou um ano futuro razoável)
data_maxima = datetime.date.today() # Usando a data atual como exemplo

#Terminal > New Terminal > pip install streamlit > pressiona enter que irá instalar o Streamlit

st.set_page_config(page_title="Hello Word")

st.title("Olá Mundo!")

st.write("Hello Word! I am back!")

#para rodar o código no navegador, é necessário colocar a função streamlit run web.py, se fizer alguma alteração, apenas atualizar o navegador que a alteração irá aparecer.

nome = st.text_input('Qual seu nome?')
idade = st.number_input('Idade?', step=1, value=0, format="%d")
dtNasc = st.date_input('Data de nascimento?', min_value=data_minima, max_value=data_maxima)

st.write(f'Olá {nome} de {idade} anos!')

st.write('Fale um pouco sobre você')
bio = st.text_area('')
