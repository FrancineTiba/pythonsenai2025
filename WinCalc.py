import tkinter as tk

def fnAdicao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x + y
    lblResultado.config(text=f'A soma é {resultado}')

def fnSubtracao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x - y
    lblResultado.config(text=f'A subtração é {resultado}')

def fnMultiplicacao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x * y
    lblResultado.config(text=f'A multiplicação é {resultado}')        

def fnDivisao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x / y
    lblResultado.config(text=f'A divisão é {resultado}')          

janela = tk.Tk() # desenha uma janela 
janela.title("WinCalc - A Super Calculadora")
janela.geometry('800x650')

lblTitulo = tk.Label(janela,
                     text='WinCalc',
                     font=('Pristina',66),
                     fg='White',
                     bg='Blue',
                     width=800)
lblTitulo.pack(padx=5,pady=5)

lblNumero1 = tk.Label(janela,
                      text='Digite um número:',
                      font=('Calibri',24))
lblNumero1.pack(padx=5,pady=5)

entryNumero1 = tk.Entry(janela,
                        width=800,
                        font=('Calibri',24))
entryNumero1.pack(padx=5,pady=5)

lblNumero2 = tk.Label(janela,
                      text='Digite outro número:',
                      font=('Calibri',24))
lblNumero2.pack(padx=5,pady=5)

entryNumero2 = tk.Entry(janela,
                        width=800,
                        font=('Calibri',24))
entryNumero2.pack(padx=5,pady=5)

btnAdicao = tk.Button(janela,
                      text='Adição',
                      font=('Calibri',16),
                      width=800,
                      command=fnAdicao)
btnAdicao.pack(padx=5,pady=5)

btnSubtracao = tk.Button(janela,
                      text='Subtração',
                      font=('Calibri',16),
                      width=800,
                      command=fnSubtracao)
btnSubtracao.pack(padx=5,pady=5)

btnMultiplicacao = tk.Button(janela,
                      text='Multiplicação',
                      font=('Calibri',16),
                      width=800,
                      command=fnMultiplicacao)
btnMultiplicacao.pack(padx=5,pady=5)

btnDivisao = tk.Button(janela,
                      text='Divisão',
                      font=('Calibri',16),
                      width=800,
                      command=fnDivisao)
btnDivisao.pack(padx=5,pady=5)

lblResultado = tk.Label(janela,
                        text='0.00',
                        font=('Calibri', 22))
lblResultado.pack(padx=5,pady=5)


janela.mainloop() #mantem o programa rodando, colocar sempre no final do código