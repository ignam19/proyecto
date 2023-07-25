import sqlite3
def insertar(codigo, articulo, stock, precio):
#CREADOR DE BASE DE DATOS
    mi_conexion= sqlite3.connect("C:\python-vscode\proyecto\\app\BDD\primer_bdd.db")

#CREADOR DE CURSOR
    mi_cursor= mi_conexion.cursor()
    

#--------CREADOR DE TABLA--------------------------
#mi_cursor.execute("CREATE TABLE TABLA (CODIGO VARCHAR(50), ARTICULO VARCHAR(50), STOCK INTEGER, PRECIO INTEGER) ")
#--------------------------------------------------

#INSERTAR TABLA
#mi_cursor.execute("INSERT INTO TABLA VALUES('123214', 'BUJIA', 12, 550)")    
    repuesto = [(codigo, articulo, stock, precio)]
    mi_cursor.executemany("INSERT INTO TABLA VALUES (?,?,?,?)", repuesto)


#COMMIT
    mi_conexion.commit()

#CERRAR CONEXION
    mi_conexion.close()

def eliminar(tabla):
    mi_conexion= sqlite3.connect("C:\python-vscode\proyecto\\app\BDD\primer_bdd.db")
    mi_cursor= mi_conexion.cursor()
    repuesto = [(tabla)]
    
    
    #### INCOMPLETA ####
    
    mi_cursor.executemany("DELETE FROM TABLA WHERE CODIGO= VALUES(?)", repuesto)
    
    
    mi_conexion.commit()
    mi_conexion.close()