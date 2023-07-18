import sqlite3

#CREADOR DE BASE DE DATOS
mi_conexion= sqlite3.connect("C:\python-vscode\proyecto\\app\BDD\primer_bdd.db")

#CREADOR DE CURSOR
mi_cursor= mi_conexion.cursor()

#--------CREADOR DE TABLA--------------------------
#mi_cursor.execute("CREATE TABLE TABLA (CODIGO VARCHAR(50), ARTICULO VARCHAR(50), STOCK INTEGER, PRECIO INTEGER) ")
#--------------------------------------------------

#INSERTAR TABLA
mi_cursor.execute("INSERT INTO TABLA VALUES('123214', 'BUJIA', 12, 550)")
mi_conexion.commit()

#CERRAR CONEXION
mi_conexion.close()

