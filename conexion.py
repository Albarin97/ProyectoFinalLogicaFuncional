import pymysql

class DataBase:
	def __init__(self):
		self.connection = pymysql.connect(
			host="localhost",
			user="root",
			password="1234",
			db="replica"
			)

		self.cursor = self.connection.cursor()

		print("Conexion Exitosa")

	def select_one(self, nom):
		sql = "SELECT nombre, genero FROM games WHERE nombre = '{}'".format(nom)
		try:
			self.cursor.execute(sql)
			juego = self.cursor.fetchone()

			#print("Nombre: ", juego[0])
			#print("Genero: ", juego[1])

		except Exception as e:
			raise e
		return juego


	def select_all(self):
		sql = 'SELECT * FROM games'
		try:
			self.cursor.execute(sql)
			juego = self.cursor.fetchall()

			#for j in juego:
			#	print("Nombre: ", j[0])
			#	print("Genero: ", j[1])
			#	print("_________\n")

		except Exception as e:
			raise e
		return juego

#database = DataBase()
#database.select_one("A")
#database.select_all()
