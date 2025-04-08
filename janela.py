import tkinter 

root = tkinter.Tk()
root.title("Senai")
root.geometry("800x600")

labelFrase = tkinter.Label(root,
                           text='Olá, Developer!',
                           font=('Magneto',72),
                           fg='#FF97CF',
                           bg='lightblue')
labelFrase.pack(padx=5,pady=5)

labelNome = tkinter.Label(root,
                          text='Digite seu nome:',
                          font=('Lucida Calligraphy',25),
                          fg='#6B3FA0')
labelNome.pack(padx=5,pady=5)

entryNome = tkinter.Entry(root,width=50,
                          font=('Verdana',22))
entryNome.pack(padx=5,pady=5)

buttonGravar = tkinter.Button(root,text="Gravar",
                              command=None)
buttonGravar.pack(padx=5,pady=5)



root.mainloop()