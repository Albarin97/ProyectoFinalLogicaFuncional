import pymysql

class DataBase:
	def __init__(self):
		self.connection = pymysql.connect(
			host="localhost",
			user="root",
			password="1234",
			db="AMS"
			)

		self.cursor = self.connection.cursor()

		print("Conexion Exitosa")

	def select_one(self, nom):
		sql = "SELECT * FROM productos WHERE idproducto = '{}'".format(nom)
		try:
			self.cursor.execute(sql)
			juego = self.cursor.fetchone()

			#print("Nombre: ", juego[0])
			#print("Genero: ", juego[1])

		except Exception as e:
			raise e
		return juego


	def select_all(self):
		sql = "SELECT * FROM productos"
		try:
			self.cursor.execute(sql)
			productos = self.cursor.fetchall()

			#for j in juego:
			#	print("Nombre: ", j[0])
			#	print("Genero: ", j[1])
			#	print("_________\n")

		except Exception as e:
			raise e
		return productos

	def alta(self, m, mo, t, p, c):
		sql = "INSERT INTO productos (marca, modelo, tipo, precio, cantidad) VALUES ('{}', '{}', '{}', {}, {})".format(m, mo, t, p, c)
		try:
			self.cursor.execute(sql)
			self.connection.commit()
		except Exception as e:
			raise e

	def baja(self, id):
		sql = "DELETE FROM productos WHERE idproducto={}".format(id)
		try:
			self.cursor.execute(sql)
			self.connection.commit()
		except Exception as e:
			raise e

database = DataBase()
#database.select_one("A")
#database.select_all()
#database.alta("H", "CBR", "Depo", 1000, 10)
