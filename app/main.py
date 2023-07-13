from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Control de stock")
ventana.geometry("1000x600")
ventana.iconbitmap("C:\python-vscode\proyecto\\app\icono.ico")

#entrada
e_texto = Entry(ventana, font= ("Calibri 15"))
e_texto.grid(row= 0, column= 0, columnspan= 4, padx= 5, pady= 5)


#botones
boton_buscar = Button(ventana, text= "Buscar", width= 6, height= 1)


#agregar botones
boton_buscar.grid(row= 0, column= 4, padx= 5, pady= 5)

#tabla
tabla = ttk.Treeview(ventana, columns=("column1", "column2", "column3"))

#estilo de columnas
tabla.column("#0", width= 80)
tabla.column("column1", width= 80, anchor= CENTER)
tabla.column("column2", width= 80, anchor= CENTER)
tabla.column("column3", width= 80, anchor= CENTER)

#estilo de cabecera de columnas
tabla.heading("#0", text= "Código", anchor= CENTER)
tabla.heading("column1", text= "Artículo", anchor= CENTER)
tabla.heading("column2", text= "Stock", anchor= CENTER)
tabla.heading("column3", text= "Precio", anchor= CENTER)

#insercion de tabla
tabla.grid(row= 1, column= 0, columnspan= 5, padx= 5, pady= 5)




ventana.mainloop()