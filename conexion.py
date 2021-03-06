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

	def select_filtro(self, x, y):
		sql = "SELECT * FROM productos WHERE %s LIKE '%%%s%%'"%(x, y,)
		try:
			self.cursor.execute(sql)
			filtrado = self.cursor.fetchall()
		except Exception as e:
			raise e
		return filtrado

	def select_pedidos(self):
		sql = "SELECT * FROM pedidos"
		try:
			self.cursor.execute(sql)
			pedidos = self.cursor.fetchall()
		except Exception as e:
			raise e
		return pedidos

	def select_ventas(self):
		sql = "SELECT * FROM ventas"
		try:
			self.cursor.execute(sql)
			ventas = self.cursor.fetchall()
		except Exception as e:
			raise e
		return ventas

	def select_pb(self):
		sql = "SELECT * FROM productos ORDER BY precio DESC"
		try:
			self.cursor.execute(sql)
			productos = self.cursor.fetchall()
		except Exception as e:
			raise e
		return productos

	def select_pa(self):
		sql = "SELECT * FROM productos ORDER BY precio ASC"
		try:
			self.cursor.execute(sql)
			productos = self.cursor.fetchall()
		except Exception as e:
			raise e
		return productos

	def select_cb(self):
		sql = "SELECT * FROM productos ORDER BY cantidad DESC"
		try:
			self.cursor.execute(sql)
			productos = self.cursor.fetchall()
		except Exception as e:
			raise e
		return productos

	def select_ca(self):
		sql = "SELECT * FROM productos ORDER BY cantidad ASC"
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

	def venta(self, idp, cl, ca, co, t, d):
		sql = "INSERT INTO ventas (idproducto, cliente, cantidad, costo, telefono, direccion) VALUES (%d, '%s', %d, %d, '%s', '%s')"%(idp, cl, ca, co, t, d,)
		try:
			self.cursor.execute(sql)
			self.connection.commit()
		except Exception as e:
			raise e

	def graficaTipo(self):
		sql="SELECT SUM(cantidad), tipo FROM productos GROUP BY tipo;"
		try:
			self.cursor.execute(sql)
			datos = self.cursor.fetchall()
		except Exception as e:
			raise e
		return datos

	def vaciarVentas(self):
		sql="DELETE FROM ventas"
		try:
			self.cursor.execute(sql)
			self.connection.commit()
		except Exception as e:
			raise e

#database = DataBase()
#database.select_one("A")
#database.select_all()
#database.alta("H", "CBR", "Depo", 1000, 10)
#database.baja(10)