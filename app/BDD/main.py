from tkinter import *
from tkinter import ttk
import tkinter as tk
import conexiones

#--------funcion boton agregar articulo----------------
def agregar_articulo():
    entradas = [e_codigo, e_articulo, e_stock, e_precio]
    valores = []
    for i in range(len(entradas)):
        valores.append(entradas[i].get())
        
    conexiones.insertar(valores[0], valores[1], valores[2], valores[3])
    insertar_tabla(valores[0], valores[1], valores[2], valores[3])
#-------------------------------------------------------

#--------funcion boton eliminar articulo---------------    
def eliminar_articulo():
    seleccion = tabla.focus()  # Obtener el ID del elemento seleccionado
    if seleccion:  # Asegurarse de que haya algo seleccionado
        tabla.delete(seleccion)
        conexiones.eliminar(e_codigo.get())
        
#------------------------------------------------------


ventana = Tk()
ventana.title("Control de stock")
ventana.geometry("1200x600")
ventana.iconbitmap("C:\python-vscode\proyecto\\app\icono.ico")

#frame entradas
frame_entradas = Frame(ventana)
frame_entradas.place(x= 5, y= 270)

#label de entradas
label_codigo = Label(frame_entradas, text= "Codigo:", font=("Calibri", 14))
label_articulo = Label(frame_entradas, text= "Articulo:", font=("Calibri", 14))
label_stock = Label(frame_entradas, text= "Stock:", font=("Calibri", 14))
label_precio = Label(frame_entradas, text= "Precio:", font=("Calibri", 14))

#agregar label
label_codigo.grid(row= 0, column= 0, sticky= "e")
label_articulo.grid(row= 1, column= 0, sticky= "e")
label_stock.grid(row= 2, column= 0, sticky= "e")
label_precio.grid(row= 3, column= 0, sticky= "e")

#entrada
e_texto = Entry(ventana, font=("Calibri", 14))
e_codigo = Entry(frame_entradas, font=("Calibri", 14))
e_articulo = Entry(frame_entradas, font=("Calibri", 14))
e_stock = Entry(frame_entradas, font=("Calibri", 14))
e_precio = Entry(frame_entradas, font=("Calibri", 14))

#agregar entrada
e_texto.place(x= 5, y= 5)
e_codigo.grid(row= 0, column= 1)
e_articulo.grid(row= 1, column= 1)
e_stock.grid(row= 2, column= 1)
e_precio.grid(row= 3, column= 1)

#frame botones agr,elim,mod
frame_3botones = Frame(ventana)
frame_3botones.place(x=350, y=270)

#botones
boton_buscar = Button(ventana, text= "Buscar", width= 6, height= 1)
boton_agregar = Button(frame_3botones, text= "Agregar", width= 10, height= 2,
                       command= lambda: agregar_articulo())
boton_modificar = Button(frame_3botones, text= "Modificar", width= 10, height= 2)
boton_eliminar = Button(frame_3botones, text= "Eliminar", width= 10, height= 2,
                        command= lambda: eliminar_articulo())

#agregar botones
boton_buscar.place(x= 230, y= 5)
boton_agregar.grid(row=0, column=0, padx= 5, pady= 5)
boton_eliminar.grid(row=0, column=1, padx= 5, pady= 5)
boton_modificar.grid(row=0, column=2, padx= 5, pady= 5)

#frame tabla
frame_tabla= Frame(ventana)
frame_tabla.place(x= 5, y= 30)

#tabla
tabla = ttk.Treeview(frame_tabla, columns=("column1", "column2", "column3", "column4"))

#estilo de columnas
tabla.column("#0", width= 220)
tabla.column("column1", width= 220, anchor= CENTER)
tabla.column("column2", width= 220, anchor= CENTER)
tabla.column("column3", width= 220, anchor= CENTER)
tabla.column("column4", width= 220, anchor= CENTER)

#estilo de cabecera de columnas
tabla.heading("#0", text= "ID")
tabla.heading("column1", text= "Código", anchor= CENTER)
tabla.heading("column2", text= "Artículo", anchor= CENTER)
tabla.heading("column3", text= "Stock", anchor= CENTER)
tabla.heading("column4", text= "Precio", anchor= CENTER)

#insercion de tabla en frame
tabla.grid(row= 0, column= 0, columnspan= 5, pady= 5)

def cargar_entry(event):
    # Obtener la selección actual del Treeview
    seleccion = tabla.focus()

    # Obtener los valores asociados a los items seleccionados
    valores = tabla.item(seleccion, 'values')

    # Cargar los valores en el Entry correspondiente
    if valores:
        e_codigo.delete(0, tk.END)  # Limpiar el Entry antes de cargar nuevos datos
        e_articulo.delete(0, tk.END)
        e_stock.delete(0, tk.END)
        e_precio.delete(0, tk.END)
        e_codigo.insert(0, valores[0])  # Insertar el valor en el Entry
        e_articulo.insert(0, valores[1])
        e_stock.insert(0, valores[2]) 
        e_precio.insert(0, valores[3]) 
        
# Vincular el evento de clic a la función cargar_datos
tabla.bind("<ButtonRelease-1>", cargar_entry)

#insercion de valores en la bd
def cargar_datos():
    for fila in conexiones.mostrar_tablas():
        tabla.insert("",END, values=(fila[0], fila[1], fila[2], fila[3]))
cargar_datos()

#insercion de valores en tabla
def insertar_tabla(codigo, articulo, stock, precio):
    tabla.insert("",END, values=(codigo, articulo, stock, precio))

#eliminacion de una fila 
def eliminar_fila():
    seleccion = tabla.focus()  # Obtener el ID del elemento seleccionado
    if seleccion:  # Asegurarse de que haya algo seleccionado
        tabla.delete(seleccion)

#scrollbar de tabla
scrollvert = Scrollbar(frame_tabla, command= tabla.yview, width= 20)
scrollvert.grid(row= 0, column= 6, sticky="nsew")
tabla.config(yscrollcommand=scrollvert.set)



ventana.mainloop()