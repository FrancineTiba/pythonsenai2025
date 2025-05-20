import streamlit as st
import json
import os #OS Operation System - Abrir e Salvar arquivo
from datetime import datetime

# Nome do arquivo JSON
ARQUIVO_DADOS = "colaboradores.json"

# Funções para manipulação do arquivo JSON
def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def criar_colaborador(cpf, nome, data_nascimento, sexo, endereco, telefone, email, experiencia=None):
    return {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "experiencia": experiencia or [],
        "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "data_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

# Funções CRUD
def cadastrar_colaborador():
    st.subheader("Cadastrar Novo Colaborador")
    
    with st.form(key="form_cadastro"):
        col1, col2 = st.columns(2)
        
        with col1:
            cpf = st.text_input("CPF (somente números)", max_chars=11)
            nome = st.text_input("Nome Completo")
            data_nascimento = st.date_input("Data de Nascimento", min_value=datetime(1900, 1, 1))
            sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        
        with col2:
            endereco = st.text_input("Endereço")
            telefone = st.text_input("Telefone")
            email = st.text_input("E-mail")
            experiencia = st.text_area("Experiêcia (opcional)")
        
        submit_button = st.form_submit_button("Cadastrar Colaborador")
    
    if submit_button:
        if not cpf or not nome:
            st.error("CPF e Nome são campos obrigatórios!")
            return
        
        dados = carregar_dados()
        
        if cpf in dados:
            st.error("Colaborador com este CPF já cadastrado!")
            return
        
        colaborador = criar_colaborador(
            cpf=cpf,
            nome=nome,
            data_nascimento=data_nascimento.strftime("%d/%m/%Y"),
            sexo=sexo,
            endereco=endereco,
            telefone=telefone,
            email=email,
            experiencia=experiencia.split("\n") if experiencia else []
        )
        
        dados[cpf] = colaborador
        salvar_dados(dados)
        
        st.success("Colaborador cadastrado com sucesso!")
        st.balloons()

def listar_colaboradores():
    st.subheader("Lista de Colaboradores Cadastrados")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhum colaborador cadastrado ainda.")
        return
    
    # Filtro por nome
    filtro_nome = st.text_input("Filtrar por nome:")
    
    colaboradores_filtrados = []
    for cpf, colaborador in dados.items():
        if filtro_nome.lower() in colaborador["nome"].lower():
            colaboradores_filtrados.append((cpf, colaborador))
    
    if not colaboradores_filtrados:
        st.warning("Nenhum colaborador encontrado com o filtro aplicado.")
        return
    
    for cpf, colaborador in colaboradores_filtrados:
        with st.expander(f"{colaborador['nome']} - CPF: {cpf}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Data de Nascimento:** {colaborador['data_nascimento']}")
                st.write(f"**Sexo:** {colaborador['sexo']}")
                st.write(f"**Endereço:** {colaborador['endereco']}")
            
            with col2:
                st.write(f"**Telefone:** {colaborador['telefone']}")
                st.write(f"**E-mail:** {colaborador['email']}")
                st.write(f"**Cadastrado em:** {colaborador['data_cadastro']}")
            
            if colaborador["experiencia"]:
                st.write("**Experiência:**")
                for item in colaborador["experiencia"]:
                    st.write(f"- {item}")

def editar_colaborador():
    st.subheader("Editar colaborador")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhum colaborador cadastrado para editar.")
        return
    
    cpf_selecionado = st.selectbox(
        "Selecione o colaborador pelo CPF",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['nome']} - {x}"
    )
    
    colaborador = dados[cpf_selecionado]
    
    with st.form(key="form_edicao"):
        col1, col2 = st.columns(2)
        
        with col1:
            novo_cpf = st.text_input("CPF (somente números)", value=colaborador["cpf"], max_chars=11)
            nome = st.text_input("Nome Completo", value=colaborador["nome"])
            data_nascimento = st.text_input("Data de Nascimento", value=colaborador["data_nascimento"])
            sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"], index=["Masculino", "Feminino", "Outro"].index(colaborador["sexo"]))
        
        with col2:
            endereco = st.text_input("Endereço", value=colaborador["endereco"])
            telefone = st.text_input("Telefone", value=colaborador["telefone"])
            email = st.text_input("E-mail", value=colaborador["email"])
            experiencia = st.text_area("Histórico Médico", value="\n".join(colaborador["experiencia"]))
        
        submit_button = st.form_submit_button("Atualizar colaborador")
    
    if submit_button:
        if not novo_cpf or not nome:
            st.error("CPF e Nome são campos obrigatórios!")
            return
        
        # Se o CPF foi alterado, precisamos verificar se o novo CPF já existe (e não é o mesmo colaborador)
        if novo_cpf != cpf_selecionado and novo_cpf in dados:
            st.error("Já existe um colaborador com este novo CPF!")
            return
        
        # Remove o colaborador antigo se o CPF foi alterado
        if novo_cpf != cpf_selecionado:
            dados.pop(cpf_selecionado)
        
        # Atualiza os dados do colaborador
        colaborador_atualizado = {
            "cpf": novo_cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "sexo": sexo,
            "endereco": endereco,
            "telefone": telefone,
            "email": email,
            "experiencia": experiencia.split("\n") if experiencia else [],
            "data_cadastro": colaborador["data_cadastro"],
            "data_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        dados[novo_cpf] = colaborador_atualizado
        salvar_dados(dados)
        
        st.success("colaborador atualizado com sucesso!")

def excluir_colaborador():
    st.subheader("Excluir colaborador")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhum colaborador cadastrado para excluir.")
        return
    
    cpf_selecionado = st.selectbox(
        "Selecione o colaborador pelo CPF para excluir",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['nome']} - {x}"
    )
    
    colaborador = dados[cpf_selecionado]
    
    st.warning("Você está prestes a excluir o seguinte colaborador:")
    st.json(colaborador)
    
    if st.button("Confirmar Exclusão"):
        dados.pop(cpf_selecionado)
        salvar_dados(dados)
        st.success("colaborador excluído com sucesso!")

# Menu lateral
st.sidebar.title("Menu")
opcao = st.sidebar.radio(
    "Selecione uma opção:",
    ("Cadastrar colaborador","Listar colaboradores", 
     "Editar colaborador", "Excluir colaborador")
)

# Navegação entre páginas
if opcao == "Cadastrar colaborador":
    cadastrar_colaborador()
elif opcao == "Listar colaboradores":
    listar_colaboradores()
elif opcao == "Editar colaborador":
    editar_colaborador()
elif opcao == "Excluir colaborador":
    excluir_colaborador()

# Rodapé
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por Gilberto")
st.sidebar.markdown(f"Total de colaboradores: ")   #{len(carregar_dados())}