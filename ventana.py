import tkinter as tk
from tkinter import messagebox as MB
from tkinter import ttk
from tkinter import PhotoImage
import conexion as con

#Creacion ventana y Configuracion
ventana = tk.Tk()
ventana.iconbitmap("Logo.ico")
ventana.title("Menu Albar's Moto Sport")
ventana.geometry("1000x600")
ventana.configure(bg="OldLace")

#Titulos
titulo=tk.Label(ventana,text="Albar's Moto Sport", bg="OldLace")
etiqueta=tk.Label(ventana,text="Bienvenido Al Sistema ABCC", bg="OldLace")
titulo.pack(fill=tk.X)
etiqueta.pack()

#etiquetas
idLabel=tk.Label(ventana,text="ID", bg="OldLace")
idLabel.place(x=30, y=60)
marcaLabel=tk.Label(ventana,text="Marca", bg="OldLace")
marcaLabel.place(x=30, y=85)
modeloLabel=tk.Label(ventana,text="Modelo", bg="OldLace")
modeloLabel.place(x=30, y=110)
tipoLabel=tk.Label(ventana,text="Tipo", bg="OldLace")
tipoLabel.place(x=30, y=135)
precioLabel=tk.Label(ventana,text="Precio", bg="OldLace")
precioLabel.place(x=30, y=160)
cantidadLabel=tk.Label(ventana,text="Cantidad", bg="OldLace")
cantidadLabel.place(x=30, y=185)

proLabel=tk.Label(ventana,text="PRODUCTOS DISPONIBLES", bg="OldLace")
proLabel.place(x=460, y=210)
venLabel=tk.Label(ventana,text="VENTAS REALIZADAS", bg="OldLace")
venLabel.place(x=490, y=410)


#cajas
idCaja = tk.Entry(ventana)
idCaja.place(x=150, y=60)
marcaCaja = ttk.Combobox(ventana, state="readonly", width=17)
marcaCaja["values"] = ["Italika", "BMW", "Honda", "Bajaj", "Yamaha", "Suzuki"]
marcaCaja.place(x=150, y=85)
modeCaja = tk.Entry(ventana)
modeCaja.place(x=150, y=110)
tipoCaja = ttk.Combobox(ventana, state="readonly", width=17)
tipoCaja["values"] = ["Doble Proposito", "Enduro", "Scooter", "Deportiva", "Crucero"]
tipoCaja.place(x=150, y=135)
precioCaja = tk.Entry(ventana)
precioCaja.place(x=150, y=160)
cantCaja = tk.Entry(ventana)
cantCaja.place(x=150, y=185)

#botones
btnAlta=tk.Button(ventana, text="Realizar ALTA", width=15, command=lambda: obtenerDatosA())
btnAlta.place(x=300, y=75)
btnBaja=tk.Button(ventana, text="Realizar BAJA", width=15, command=lambda: obtenerId())
btnBaja.place(x=300, y=105)
btnCambio=tk.Button(ventana, text="Realizar CAMBIOS", width=15, command=lambda: obtenerDatosC())
btnCambio.place(x=300, y=135)
btnLimpiar=tk.Button(ventana, text="Limpiar", width=15, command=lambda: limpiar())
btnLimpiar.place(x=300, y=165)

img = PhotoImage(file='vender.png')
img2 = PhotoImage(file='actualizar.png')
btnObtener=tk.Button(ventana, text="Obtener", width=15, command=lambda: sacar())
btnObtener.place(x=30, y=385)
btnVender=tk.Button(ventana, text="Vender", image=img, width=40, command=lambda: vender())
btnVender.place(x=150, y=385)
def azr():
	actualizarT()
	actualizarTP()
btnActualizar=tk.Button(ventana, text="Actualizar", image=img2, width=40, command=lambda: azr())
btnActualizar.place(x=200, y=385)



#Variables
strID=tk.StringVar()
strMarca=tk.StringVar()
strModelo=tk.StringVar()
strTipo=tk.StringVar()
strPrecio=tk.StringVar()
strCantidad=tk.StringVar()

#Funciones
#Treeview
lb = ttk.Treeview(ventana, columns=("mar", "mod", "tip", "pre","can"));
lb.heading("#0", text="ID")
lb.column("#0", width=10)
lb.heading("mar", text="Marca")
lb.column("mar", width=50)
lb.heading("mod", text="Modelo")
lb.column("mod", width=50)
lb.heading("tip", text="Tipo")
lb.column("tip", width=50)
lb.heading("pre", text="Precio")
lb.column("pre", width=50)
lb.heading("can", text="Cantidad")
lb.column("can", width=50)

lb2 = ttk.Treeview(ventana, columns=("mar2", "mod2", "tip2", "cli2", "pre2", "can2", "cos2"));
lb2.heading("#0", text="ID Venta")
lb2.column("#0", width=50)
lb2.heading("mar2", text="Marca")
lb2.column("mar2", width=50)
lb2.heading("mod2", text="Modelo")
lb2.column("mod2", width=50)
lb2.heading("tip2", text="Tipo")
lb2.column("tip2", width=50)
lb2.heading("cli2", text="Cliente")
lb2.column("cli2", width=50)
lb2.heading("pre2", text="Precio")
lb2.column("pre2", width=50)
lb2.heading("can2", text="Cantidad")
lb2.column("can2", width=30)
lb2.heading("cos2", text="Costo")
lb2.column("cos2", width=50)


def actualizarT():
	lb.delete(*lb.get_children())
	items = con.DataBase().select_all()
	for p in items:
		lb.insert("", tk.END, text=p[0], values=(p[1], p[2], p[3], p[4], p[5]))
	lb.place(x=10, y=230, width=600, height=150)
	lb.selection_remove()
	return lb

def actualizarTP():
	lb2.delete(*lb2.get_children())
	items2 = con.DataBase().select_pedidos()
	for p2 in items2:
		lb2.insert("", tk.END, text=p2[0], values=(p2[1], p2[2], p2[3], p2[4], p2[5], p2[6]))
	lb2.place(x=10, y=430, width=600, height=150)
	lb2.selection_remove()
	return lb2

def sacar():
	try:
		seleccionado = lb.selection()[0]
		id = lb.item(seleccionado, option="text")
		#print(id)
		cargar(id)
	except Exception as e:
		MB.showerror("Error", "Seleccione un Registro de la Tabla")

def vender():
	try:
		seleccionadoV = lb.selection()[0]
		id = lb.item(seleccionadoV, option="text")
		print(id)
		ventanaVender(id)
	except Exception as e:
		print(e)
		MB.showerror("Error", "Seleccione un Articulo a Vender")

def cargar(id):
	limpiar()
	lista = con.DataBase().select_one(id)
	idCaja.insert(0, lista[0])
	marcaCaja.set(lista[1])
	modeCaja.insert(0, lista[2])
	tipoCaja.set(lista[3])
	precioCaja.insert(0, lista[4])
	cantCaja.insert(0, lista[5])

def obtenerDatosA():
	strID.set(idCaja.get())
	strMarca.set(marcaCaja.get())
	strModelo.set(modeCaja.get())
	strTipo.set(tipoCaja.get())
	strPrecio.set(precioCaja.get())
	strCantidad.set(cantCaja.get())
	if not strMarca.get() or not strModelo.get() or not strTipo.get() or not strPrecio.get() or not strCantidad.get():
		MB.showerror("Error", "Faltan Datos")
	elif not strPrecio.get().isdigit() or not strCantidad.get().isdigit():
		MB.showerror("Error", "Precio y Cantidad Deben Llevar Solo NUMEROS")
	else:
		realizarAlta(strMarca.get(), strModelo.get(), strTipo.get(), int(strPrecio.get()), int(strCantidad.get()))
		actualizarT()
		actualizarTP()

def obtenerDatosC():
	strID.set(idCaja.get())
	strMarca.set(marcaCaja.get())
	strModelo.set(modeCaja.get())
	strTipo.set(tipoCaja.get())
	strPrecio.set(precioCaja.get())
	strCantidad.set(cantCaja.get())
	if not strID.get() or not strMarca.get() or not strModelo.get() or not strTipo.get() or not strPrecio.get() or not strCantidad.get():
		MB.showerror("Error", "Faltan Datos")
	elif not strPrecio.get().isdigit() or not strCantidad.get().isdigit():
		MB.showerror("Error", "Precio y Cantidad Deben Llevar Solo NUMEROS")
	else:
		realizarCambio(int(strID.get()), strMarca.get(), strModelo.get(), strTipo.get(), int(strPrecio.get()), int(strCantidad.get()))
		actualizarT()
		actualizarTP()

def obtenerId():
	strID.set(idCaja.get())
	if strID.get():
		con.DataBase().baja(int(strID.get()))
		actualizarT();
		actualizarTP()
		MB.showinfo("Exito", "Baja Realizada")
	else:
		MB.showerror("Error", "Introduce un ID")

def imprimir():
	print(strID.get()+strMarca.get())

def limpiar():
	idCaja.delete(0, tk.END)
	marcaCaja.set("")
	modeCaja.delete(0, tk.END)
	tipoCaja.set("")
	precioCaja.delete(0, tk.END)
	cantCaja.delete(0, tk.END)

def realizarAlta(m, mo, t, p, c):
	con.DataBase().alta(m, mo, t, p, c)
	MB.showinfo("Exito", "Alta Realizada")

def realizarCambio(idp, m, mo, t, p, c):
	con.DataBase().actualizar(idp, m, mo, t, p, c)
	MB.showinfo("Exito", "Cambio Realizado")


def ventanaVender(id):
	venta = tk.Tk()
	venta.iconbitmap("vender.ico")
	venta.title("AMS Proceso Venta")
	venta.geometry("300x400")
	venta.resizable(0, 0)
	venta.configure(bg="OldLace")
	#Titulo
	titulo=tk.Label(venta,text="Albar's Moto Sport", bg="OldLace")
	titulo.pack(fill=tk.X)
	etiqueta=tk.Label(venta,text="Menu De Venta", bg="OldLace")
	etiqueta.pack()

	#etiquetas
	idLabel=tk.Label(venta,text="ID", bg="OldLace")
	idLabel.place(x=30, y=60)
	marcaLabel=tk.Label(venta,text="Marca", bg="OldLace")
	marcaLabel.place(x=30, y=85)
	modeloLabel=tk.Label(venta,text="Modelo", bg="OldLace")
	modeloLabel.place(x=30, y=110)
	tipoLabel=tk.Label(venta,text="Tipo", bg="OldLace")
	tipoLabel.place(x=30, y=135)
	precioLabel=tk.Label(venta,text="Precio", bg="OldLace")
	precioLabel.place(x=30, y=160)
	cantidadLabel=tk.Label(venta,text="Cantidad", bg="OldLace")
	cantidadLabel.place(x=30, y=185)
	divLabel=tk.Label(venta,text="_____________________________________________________________", bg="OldLace")
	divLabel.place(x=0, y=200)
	clienteLabel=tk.Label(venta,text="Cliente", bg="OldLace")
	clienteLabel.place(x=30, y=225)
	cantidadLabel=tk.Label(venta,text="Cantidad", bg="OldLace")
	cantidadLabel.place(x=30, y=250)
	telefonoLabel=tk.Label(venta,text="Telefono", bg="OldLace")
	telefonoLabel.place(x=30, y=275)
	direcLabel=tk.Label(venta,text="Direccion", bg="OldLace")
	direcLabel.place(x=30, y=300)


	#cajas
	listav = con.DataBase().select_one(id)
	
	idCajaV = tk.Entry(venta)
	idCajaV.place(x=150, y=60)
	marcaCajaV = tk.Entry(venta)
	marcaCajaV.place(x=150, y=85)
	modeCajaV = tk.Entry(venta)
	modeCajaV.place(x=150, y=110)
	tipoCajaV = tk.Entry(venta)
	tipoCajaV.place(x=150, y=135)
	precioCajaV = tk.Entry(venta)
	precioCajaV.place(x=150, y=160)
	cantCajaV = tk.Entry(venta)
	cantCajaV.place(x=150, y=185)
	
	idCajaV.insert(0, listav[0])
	marcaCajaV.insert(0, listav[1])
	modeCajaV.insert(0, listav[2])
	tipoCajaV.insert(0, listav[3])
	precioCajaV.insert(0, listav[4])
	cantCajaV.insert(0, listav[5])

	clienCaja = tk.Entry(venta)
	clienCaja.place(x=150, y=225)
	cantSpn = tk.Spinbox(venta, from_=0, to=1000, width=18, state='readonly')
	cantSpn.place(x=150, y=250)
	telCaja = tk.Entry(venta)
	telCaja.place(x=150, y=275)
	direCaja = tk.Entry(venta)
	direCaja.place(x=150, y=300)

	#Boton
	imgVenta = PhotoImage(file='login.png')
	btnVen=tk.Button(venta, text="vender", command=lambda: realizarVenta())
	btnVen.place(x=120, y=350)

	def realizarVenta():
		con.DataBase().venta(int(idCajaV.get()), clienCaja.get(), int(cantSpn.get()), (int(cantSpn.get())*int(precioCajaV.get())), telCaja.get(), direCaja.get())
		MB.showinfo("Exito", "Venta Realizada")
		venta.destroy()
		actualizarTP()
	#////////////////////////////////
	venta.mainloop()


lb=actualizarT()
lb2=actualizarTP()
#//////////////
ventana.mainloop()