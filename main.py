from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import Image, ImageTk

from tkcalendar import Calendar, DateEntry
from datetime import date

#importando views
from view import *

#cores

co0 = "#2e2d2b" #preto
co1= "#feffff" #branco
co2 = "#4fa882" #verde
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e06636" # - profit
co6 = "#038cfc" #azul
co7 = "#3fbfb9" #verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde

#criando janela 

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#Criando frames

frameTop = Frame(janela, width=1043, height=50, bg=co1, relief= FLAT)
frameTop.grid(row=0, column=0)

frameMid = Frame(janela, width=1043, height=303, bg=co1,pady= 20, relief= FLAT)
frameMid.grid(row=1, column=0, pady=1,padx=0, sticky=NSEW)

frameDown = Frame(janela, width=1043, height=300, bg=co1, relief= FLAT)
frameDown.grid(row=2, column=0, pady=0,padx=1, sticky=NSEW)

#criando funções
global tree

#função inserir 
def inserir():
    
    
    nome = entrada_nome.get()
    barra = entrada_barra.get()
    descricao = entrada_desc.get()
    valor = entrada_valor.get()
    marca = entrada_marca.get()
    data = entrada_data.get_date()
    estoque = entrada_estoque.get()
    imagem = imagem_string
    
    list_inserir = [nome, barra, descricao, valor, marca, data, estoque, imagem]
    
    for i in list_inserir:
        if i == "":
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    inserir_form(list_inserir)
    
    messagebox.showinfo('Sucesso','Dados inseridos com sucesso')
    
    entrada_nome.delete(0,'end')
    entrada_barra.delete(0,'end')
    entrada_desc.delete(0,'end')
    entrada_valor.delete(0,'end')
    entrada_marca.delete(0,'end')
    entrada_data.delete(0,'end')
    entrada_estoque.delete(0,'end')
      

    mostrar()

#função atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treever_dados = tree.focus()
        treever_dicionario = tree.item(treever_dados)
        #print(treever_dicionario)
        treever_lista = treever_dicionario['values']
        valor = treever_lista[0]
        
        entrada_nome.delete(0,'end')
        entrada_barra.delete(0,'end')
        entrada_desc.delete(0,'end')
        entrada_valor.delete(0,'end')
        entrada_marca.delete(0,'end')
        entrada_data.delete(0,'end')
        entrada_estoque.delete(0,'end')
        
        id = int(treever_lista[0])
        entrada_nome.insert(0,treever_lista[1])
        entrada_barra.insert(0,treever_lista[2])
        entrada_desc.insert(0,treever_lista[3])
        entrada_valor.insert(0,treever_lista[4])
        entrada_marca.insert(0,treever_lista[5])
        entrada_data.insert(0,treever_lista[6])
        entrada_estoque.insert(0,treever_lista[7])
        imagem_string = treever_lista[8]
        print(treever_lista)
        
        def update():
            global imagem, imagem_string, l_imagem
            
            nome = entrada_nome.get()
            barra = entrada_barra.get()
            descricao = entrada_desc.get()
            valor = entrada_valor.get()
            marca = entrada_marca.get()
            data = entrada_data.get_date()
            estoque = entrada_estoque.get()
            imagem = imagem_string
            
            lista_atualizar = [nome, barra, descricao,valor,marca,data,estoque,imagem, id]
            for i in lista_atualizar:
                print(i)
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
            
            atualizar_form(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Dados foram atualizados com sucesso')
            
            entrada_nome.delete(0,'end')
            entrada_barra.delete(0,'end')
            entrada_desc.delete(0,'end')
            entrada_valor.delete(0,'end')
            entrada_marca.delete(0,'end')
            entrada_data.delete(0,'end')
            entrada_estoque.delete(0,'end')
            btn_confirmar.destroy()
            mostrar()
        
        btn_confirmar= Button(frameMid,command=update, width=13, text='  confirmar'.upper(),overrelief=RIDGE, font=('Ivy 8 bold'), bg=co2, fg=co1)
        btn_confirmar.place(x=330, y=185)
    
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados da tabela')            
        

#função deletar
def deletar():
    
    try:
        treever_dados = tree.focus()
        treever_dicionario = tree.item(treever_dados)
        #print(treever_dicionario)
        treever_lista = treever_dicionario['values']
        valor = treever_lista[0]
        
        deletar_form([valor])
        
        
        messagebox.showinfo('Sucesso', 'Dados foram deletados com sucesso')
            
        
        mostrar()
        
        
    
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados da tabela')            
        
# função para escolher imagem 

def escolher_imagem():
    global imagem, imagem_string, l_imagem
    
    imagem = fd.askopenfilename()
    imagem_string = imagem
    
    # Abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMid, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)


#função para ver item

def ver_imagem():
    global imagem, imagem_string, l_imagem
    
    treever_dados = tree.focus()
    treever_dicionario = tree.item(treever_dados)
    #print(treever_dicionario)
    treever_lista = treever_dicionario['values']
    
    
    valor_id = [int(treever_lista[0])]
    
    item = ver_dados_individual_form(valor_id)
    imagem = item[0][8]  
    
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMid, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)
          
    


# trabalhando no frameTop

# Abrindo imagem
app_img = Image.open('product.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameTop, image=app_img, text=' Cadastro de Produto', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# trabalhando no frameMid

#criando entradas

label_nome= Label(frameMid, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
label_nome.place(x=10, y=10)
entrada_nome = Entry(frameMid, width=30, justify='left', relief=SOLID)
entrada_nome.place(x=130,y=11)

label_barra= Label(frameMid, text='Barra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
label_barra.place(x=10, y=40)
entrada_barra = Entry(frameMid, width=30, justify='left', relief=SOLID)
entrada_barra.place(x=130,y=41)

label_desc= Label(frameMid, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
label_desc.place(x=10, y=70)
entrada_desc = Entry(frameMid, width=30, justify='left', relief=SOLID)
entrada_desc.place(x=130,y=71)

label_valor= Label(frameMid, text='Valor', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
label_valor.place(x=10, y=100)
entrada_valor = Entry(frameMid, width=30, justify='left', relief=SOLID)
entrada_valor.place(x=130,y=101)

label_marca= Label(frameMid, text='Marca', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
label_marca.place(x=10, y=130)
entrada_marca = Entry(frameMid, width=30, justify='left', relief=SOLID)
entrada_marca.place(x=130,y=131)



label_data= Label(frameMid, text='Data de Compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
label_data.place(x=10, y=160)
entrada_data = DateEntry(frameMid, width=12, Background='darkblue', borderwidth=2, year=2023)
entrada_data.place(x=130,y=161)

label_estoque= Label(frameMid, text='Estoque', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
label_estoque.place(x=10, y=190)
entrada_estoque = Entry(frameMid, width=30, justify='left', relief=SOLID)
entrada_estoque.place(x=130,y=191)

#criando botoes

#botao carregar

label_carregar= Label(frameMid, text='Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
label_carregar.place(x=10, y=220)
btn_carregar= Button(frameMid,command=escolher_imagem,width=29, text='carregar'.upper(),compound=CENTER, anchor=CENTER,overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
btn_carregar.place(x=130, y=221)

#botao inserir

img_add = Image.open('add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)


btn_inserir= Button(frameMid,command=inserir,image=img_add, width=95, text='  adicionar'.upper(),compound=LEFT, anchor=NW,overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
btn_inserir.place(x=330, y=10)

#botao atualizar

img_update = Image.open('update.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)


btn_update= Button(frameMid,command=atualizar,image=img_update, width=95, text='  atualizar'.upper(),compound=LEFT, anchor=NW,overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
btn_update.place(x=330, y=50)

#botao deletar
img_delete = Image.open('delete.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)


btn_delete= Button(frameMid,command=deletar,image=img_delete, width=95, text='  deletar'.upper(),compound=LEFT, anchor=NW,overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
btn_delete.place(x=330, y=90)


#botao ver imagem

img_item = Image.open('item.png')
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)


btn_item= Button(frameMid,command=ver_imagem, image=img_item, width=100, text=' ver produto'.upper(),compound=LEFT, anchor=NW,overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
btn_item.place(x=330, y=221)


# labels quantidade total e valores

label_total= Label(frameMid, text='', height=2,width=14, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
label_total.place(x=450, y=17)
label_total_= Label(frameMid, text=' Valor total de todos os itens    ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
label_total_.place(x=450, y=12)

label_qtd= Label(frameMid, text='', height=2,pady=5, width=14, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
label_qtd.place(x=450, y=90)
label_qtd_= Label(frameMid, text='  Quantidade total de itens  ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
label_qtd_.place(x=450, y=92)


# tabela -----------------------------------------------------------
def mostrar():
    global tree
    # creating a treeview with dual scrollbars
    tabela_head = ['#Item','Nome', 'Barra','Descrição', 'Valor', 'Marca','Data de compra', 'Estoque']

    lista_itens = ver_dados_form()



    tree = ttk.Treeview(frameDown, selectmode="extended",columns=tabela_head, show="headings")


    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDown, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameDown, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameDown.grid_rowconfigure(0, weight=12)

    position=["center","center","center","center","center","center","center", 'center']
    head_width=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=head_width[n],anchor=position[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = []

    for item in lista_itens:
        print(item)
        quantidade.append(item[4])

    Total_valor = float(sum(quantidade))
    Total_itens = len(quantidade)

    label_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    label_qtd['text'] = Total_itens

 

mostrar()





janela.mainloop()

