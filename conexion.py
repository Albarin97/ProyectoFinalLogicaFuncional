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

		#print("Conexion Exitosa")

	def select_one(self, idp):
		sql = "SELECT * FROM productos WHERE idproducto = %d"%(idp,)
		try:
			self.cursor.execute(sql)
			producto = self.cursor.fetchone()
		except Exception as e:
			raise e
		return producto


	def select_all(self):
		sql = "SELECT * FROM productos"
		try:
			self.cursor.execute(sql)
			productos = self.cursor.fetchall()
		except Exception as e:
			raise e
		return productos

	def alta(self, m, mo, t, p, c):
		sql = "INSERT INTO productos (marca, modelo, tipo, precio, cantidad) VALUES ('%s', '%s', '%s', %d, %d)"%(m, mo, t, p, c,)
		try:
			self.cursor.execute(sql)
			self.connection.commit()
		except Exception as e:
			raise e

	def actualizar(self, idp, m, mo, t, p, c):
		sql = "UPDATE productos SET marca='%s', modelo='%s', tipo='%s', precio=%d, cantidad=%d WHERE idproducto=%d"%(m, mo, t, p, c, idp,)
		try:
			self.cursor.execute(sql)
			self.connection.commit()
		except Exception as e:
			raise e


	def baja(self, idp):
		sql = "DELETE FROM productos WHERE idproducto=%d" % (idp,)
		try:
			self.cursor.execute(sql)
			self.connection.commit()
		except Exception as e:
			raise e

	#def cambio


#database = DataBase()
#database.select_one("A")
#database.select_all()
#database.alta("H", "CBR", "Depo", 1000, 10)
#database.baja(10)