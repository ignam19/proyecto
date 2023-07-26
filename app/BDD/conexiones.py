import sqlite3

def mostrar_tablas():
    mi_conexion= sqlite3.connect("C:\python-vscode\proyecto\\app\BDD\primer_bdd2.db")
    mi_cursor= mi_conexion.cursor()     


    mi_cursor.execute("SELECT * FROM TABLA")
    datos = mi_cursor.fetchall()
    
    mi_conexion.commit()
    mi_conexion.close()
    
    return datos

def insertar(codigo, articulo, stock, precio):
#CREADOR DE BASE DE DATOS
    mi_conexion= sqlite3.connect("C:\python-vscode\proyecto\\app\BDD\primer_bdd2.db")

#CREADOR DE CURSOR
    mi_cursor= mi_conexion.cursor()

#INSERTAR TABLA
#mi_cursor.execute("INSERT INTO TABLA VALUES('123214', 'BUJIA', 12, 550)")    
    repuesto = [(codigo, articulo, stock, precio)]
    mi_cursor.executemany("INSERT INTO TABLA VALUES (?,?,?,?)", repuesto)   
    

#COMMIT
    mi_conexion.commit()

#CERRAR CONEXION
    mi_conexion.close()
    
     
#--------CREADOR DE TABLA--------------------------
#mi_cursor.execute("CREATE TABLE TABLA (CODIGO VARCHAR(50), ARTICULO VARCHAR(50), STOCK INTEGER, PRECIO INTEGER) ")
#--------------------------------------------------

def eliminar(codigo):
    mi_conexion= sqlite3.connect("C:\python-vscode\proyecto\\app\BDD\primer_bdd.db")
    mi_cursor= mi_conexion.cursor()
     
    mi_cursor.execute("DELETE FROM TABLA WHERE CODIGO= '%s'" %codigo)
    
    mi_conexion.commit()
    mi_conexion.close()
    
