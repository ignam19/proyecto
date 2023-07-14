from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Control de stock")
ventana.geometry("1000x600")
ventana.iconbitmap("C:\python-vscode\proyecto\\app\icono.ico")



#entrada
e_texto = Entry(ventana, font=("Calibri", 14))
e_codigo = Entry(ventana, font=("Calibri", 14))
e_articulo = Entry(ventana, font=("Calibri", 14))
e_stock = Entry(ventana, font=("Calibri", 14))
e_precio = Entry(ventana, font=("Calibri", 14))

#agregar entrada
e_texto.place(x= 5, y= 5)
e_codigo.place(x= 5, y= 270)
e_articulo.place(x= 5, y= 310)
e_stock.place(x= 5, y= 350)
e_precio.place(x= 5, y= 390)

#botones
boton_buscar = Button(ventana, text= "Buscar", width= 6, height= 1)
boton_agregar = Button(ventana, text= "Agregar", width= 10, height= 2)
boton_modificar = Button(ventana, text= "Modificar", width= 10, height= 2)
boton_eliminar = Button(ventana, text= "Eliminar", width= 10, height= 2)

#agregar botones
boton_buscar.place(x= 220, y= 5)
boton_agregar.place(x= 220, y= 270)
boton_modificar.place(x= 220, y= 310)
boton_eliminar.place(x= 220, y= 350)

#frame tabla
frame_tabla= Frame(ventana)
frame_tabla.place(x= 5, y= 30)

#tabla
tabla = ttk.Treeview(frame_tabla, columns=("column1", "column2", "column3"))

#estilo de columnas
tabla.column("#0", width= 220)
tabla.column("column1", width= 220, anchor= CENTER)
tabla.column("column2", width= 220, anchor= CENTER)
tabla.column("column3", width= 220, anchor= CENTER)

#estilo de cabecera de columnas
tabla.heading("#0", text= "Código", anchor= CENTER)
tabla.heading("column1", text= "Artículo", anchor= CENTER)
tabla.heading("column2", text= "Stock", anchor= CENTER)
tabla.heading("column3", text= "Precio", anchor= CENTER)

#insercion de tabla
tabla.grid(row= 0, column= 0, columnspan= 5, pady= 5)




ventana.mainloop()