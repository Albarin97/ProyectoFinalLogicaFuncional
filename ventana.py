import tkinter as tk
from tkinter import messagebox as MB

#Creacion ventana y Configuracion
ventana = tk.Tk()
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


#cajas
idCaja = tk.Entry(ventana)
idCaja.place(x=150, y=60)
marcaCaja = tk.Entry(ventana)
marcaCaja.place(x=150, y=85)
modeCaja = tk.Entry(ventana)
modeCaja.place(x=150, y=110)
tipoCaja = tk.Entry(ventana)
tipoCaja.place(x=150, y=135)
precioCaja = tk.Entry(ventana)
precioCaja.place(x=150, y=160)
cantCaja = tk.Entry(ventana)
cantCaja.place(x=150, y=185)

#botones
btnAlta=tk.Button(ventana, text="Realizar ALTA", command=lambda: obtenerDatos())
btnAlta.place(x=300, y=85)
btnBaja=tk.Button(ventana, text="Realizar BAJA", command=lambda: obtenerId())
btnBaja.place(x=300, y=115)
btnCambio=tk.Button(ventana, text="Realizar CAMBIOS", command=lambda: obtenerDatos())
btnCambio.place(x=300, y=145)

#Variables
strID=tk.StringVar()
strMarca=tk.StringVar()
strModelo=tk.StringVar()
strTipo=tk.StringVar()
strPrecio=tk.StringVar()
strCantidad=tk.StringVar()

#Funciones
def obtenerDatos():
	strID.set(idCaja.get())
	strMarca.set(marcaCaja.get())
	strModelo.set(modeCaja.get())
	strTipo.set(tipoCaja.get())
	strPrecio.set(precioCaja.get())
	strCantidad.set(cantCaja.get())
	if not strID.get() or not strMarca.get() or not strModelo.get() or not strTipo.get() or not strPrecio.get() or not strCantidad.get():
		MB.showerror("Error", "Faltan Datos")
	else:
		print(strID.get())

def obtenerId():
	strID.set(idCaja.get())
	if strID.get():
		print("Si esta")
	else:
		MB.showerror("Error", "Introduce un ID")

def imprimir():
	print(strID.get()+strMarca.get())

#//////////////
ventana.mainloop()