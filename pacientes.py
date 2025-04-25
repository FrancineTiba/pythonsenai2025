import tkinter as tk
from tkinter import ttk, messagebox, filedialog

#Salvar a lista, banco de dados permanete
import json #Import necessário 

def carregar_de_json():
    global pacientes, next_paciente_id
    
    arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivos JSON", "*.json")],
        title="Selecionar arquivo JSON para carregar"
    )
    
    if not arquivo:  # Se o usuário cancelar
        return
    
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            pacientes_carregados = json.load(f)
        
        # Atualiza a lista de pacientes e o próximo ID
        pacientes = pacientes_carregados
        if pacientes:
            next_paciente_id=max(paciente['id'] for paciente in pacientes)+1
        else:
            next_paciente_id = 1
            
        carregar_pacientes(pacientes)
        messagebox.showinfo("Sucesso", 
           f"Dados carregados com sucesso de:\n{arquivo}")
    except Exception as e:
        messagebox.showerror("Erro", 
            f"Ocorreu um erro ao carregar:\n{str(e)}")


def salvar_para_json():
    if not pacientes:
        messagebox.showwarning("Aviso", "Não há pacientes !")
        return
    
#Abre a janela para selecionar onde salvar o arquivo
    arquivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Arquivos JSON", "*.json")], title="Salvar lista de pacientes como JSON")

    if not arquivo: #Se o usuário cancelar
        return
    
    try:   
        with open (arquivo, 'w', encoding='utf-8')as f:
            json.dump(pacientes, f, ensure_ascii=False, indent=4)


        messagebox.showinfo("Sucesso", f"Dados salvos com sucesso em: \n{arquivo}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao salvar:\n{str(e)}")



#def=função , a função é um bloco de código, que aguarda o usuário chamar por ele
def carregar_pacientes(pacientes_list=None):
    for item in tree.get_children():
        tree.delete(item)

    pacientes_to_load = pacientes_list if pacientes_list is not None else pacientes

    for paciente in pacientes_to_load:
        tree.insert('', 'end', values=(
            paciente['id'],
            paciente['nome'],
            paciente['data'],
            paciente['genero'],
            paciente['estCivil'],
            paciente['profissao'],
            paciente['celular'],
        ))

def adicionar_paciente():
    global next_paciente_id
    nome = entry_nome.get()
    data = entry_data.get()
    genero = entry_genero.get()
    estCivil = entry_estCivil.get()
    profissao = entry_profissao.get()
    celular = entry_celular.get()

    if not nome:
        messagebox.showerror("Erro", "Nome do pacinte é obrigatório")
        return
  

    novo_paciente = {
        'id': next_paciente_id,
        'nome': nome,
        'data': data,
        'genero': genero,
        'estCivil': estCivil,
        'profissao': profissao,
        'celular': celular
    }       

    pacientes.append(novo_paciente)
    next_paciente_id += 1

    messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
    carregar_pacientes()
    limpar_campos()

def selecionar_paciente(event):
    selected_item = tree.selection()
    if not selected_item:
        return

    values = tree.item(selected_item)['values']
    limpar_campos()

    entry_nome.insert(0, values[1])
    entry_data.insert(0, values[2])
    entry_genero.insert(0, values[3])
    entry_estCivil.insert(0, values[4])
    entry_profissao.insert(0, values[5])
    entry_celular.insert(0, str(values[6]))

def limpar_campos():
    entry_nome.delete(0, 'end')
    entry_data.delete(0, 'end') 
    entry_genero.delete(0, 'end')
    entry_estCivil.delete(0, 'end')
    entry_profissao.delete(0, 'end')
    entry_celular.delete(0, 'end')

def editar_paciente():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione um paciente para editar!")
        return
    
    paciente_id = tree.item(selected_item)['values'][0]
    nome = entry_nome.get()
    data = entry_data.get()
    genero = entry_genero.get()
    estCivil = entry_estCivil.get()
    profissao = entry_profissao.get()
    celular = entry_celular.get()

    if not nome or not data:
        messagebox.showerror("Erro", "Nome e data de nascimento do paciente são obrigatórios!")
        return
    
    
    for paciente in pacientes:
        if paciente['id'] == paciente_id:
            paciente.update({
                'nome': nome,
                'data': data,
                'genero': genero,
                'estCivil': estCivil,
                'profissao': profissao,
                'celular': celular
                
            })
            break

    messagebox.showinfo("Sucesso", "Paciente atualizado com sucesso!")
    carregar_pacientes()    

def remover_paciente():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione um paciente para remover!")
        return
    paciente_id = tree.item(selected_item)['values'][0]

    if messagebox.askyesno("Confirmação", "Tem certeza que deseja remover este paciente?"):
        global pacientes
        pacientes = [paciente for paciente in pacientes if paciente['id'] !=paciente_id]
        messagebox.showinfo("Sucesso", "Paciente removido com sucesso!")
        limpar_campos()
        carregar_pacientes()

def pesquisar_por_nome():
    termo_pesquisa = entry_nome.get().lower()

    if not termo_pesquisa:
        carregar_pacientes()
        return
    
    pacientes_encontrados = [paciente for paciente in pacientes
        if termo_pesquisa in paciente['nome'].lower()]
    
    if not pacientes_encontrados:
        messagebox.showinfo("Pesquisa", "Nenhum paciente encontrado com este nome")
        carregar_pacientes()
    else:
        carregar_pacientes(pacientes_encontrados)    




# Dados em memória
pacientes = []  #array = lista
next_paciente_id = 1 # contador

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Cadastro de Pacientes")
root.geometry("950x500")

# Frame formulário
frame_form = ttk.LabelFrame(root, text = "Formulário de Paciente")
frame_form.pack(padx=10, pady=5, fill='x')

# Campos do formulário
ttk.Label(frame_form, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_nome = ttk.Entry(frame_form, width=40)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Data de nascimento:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_data = ttk.Entry(frame_form, width=40)
entry_data.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Gênero:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_genero = ttk.Entry(frame_form, width=40)
entry_genero.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Estado Civil:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
entry_estCivil = ttk.Entry(frame_form, width=40)
entry_estCivil.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Profissão:").grid(row=4, column=0, padx=5, pady=5, sticky='e')
entry_profissao = ttk.Entry(frame_form, width=40)
entry_profissao.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Celular:").grid(row=5, column=0, padx=5, pady=5, sticky='e')
entry_celular = ttk.Entry(frame_form, width=40)
entry_celular.grid(row=5, column=1, padx=5, pady=5)

# Frame de botões
frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=5)

btn_adicionar = ttk.Button(frame_botoes, text="Adicionar", command=adicionar_paciente)
btn_adicionar.grid(row=0, column=0, padx=5)

btn_editar = ttk.Button(frame_botoes, text="Editar", command=editar_paciente)
btn_editar.grid(row=0, column=1, padx=5)

btn_remover = ttk.Button(frame_botoes, text="Remover", command=remover_paciente)
btn_remover.grid(row=0, column=2, padx=5)

btn_limpar = ttk.Button(frame_botoes, text="Limpar", command=limpar_campos)
btn_limpar.grid(row=0, column=3, padx=5)

btn_pesquisar = ttk.Button(frame_botoes, text="Pesquisar", command=pesquisar_por_nome)
btn_pesquisar.grid(row=0, column=4, padx=5)

btn_salvar = ttk.Button(frame_botoes, text="Salvar", command=salvar_para_json)
btn_salvar.grid(row=0, column=5, padx=5)

btn_carregar = ttk.Button(frame_botoes, text="Carregar de JSON", command=carregar_de_json)
btn_carregar.grid(row=0, column=6, padx=5)

# Tabela de pacientes
frame_tabela = ttk.Frame(root)
frame_tabela.pack(padx=10, pady=5, fill='both', expand=True)

tree = ttk.Treeview(frame_tabela, columns=('ID', 'Nome', 'Data de nascimento', 'Gênero', 'Estado Civil', 'Profissão', 'Celular'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Nome', text='Nome')
tree.heading('Data de nascimento', text='Data de nascimento')
tree.heading('Gênero', text='Gênero')
tree.heading('Estado Civil', text='Estado Civil')
tree.heading('Profissão', text='Profissão')
tree.heading('Celular', text='Celular')

#lista ou array [] é uma variável - [] é uma lista e {} é dicionário, ou conseguimos montar uma lista com vários dicionários [{}]

tree.column('ID', width=25)
tree.column('Nome', width=150)
tree.column('Data de nascimento', width=100)
tree.column('Gênero', width=100)
tree.column('Estado Civil', width=75)
tree.column('Profissão', width=75)
tree.column('Celular', width=75)

scrollbar = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
tree.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')


tree.bind('<<TreeviewSelect>>', selecionar_paciente)




root.mainloop()