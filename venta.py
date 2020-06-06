import tkinter as tk
from tkinter import messagebox as MB
from tkinter import ttk
from tkinter import PhotoImage
import conexion as con

class vent:
	def __init__(self):
		

	def f(self, n):
		idCaja.insert(0, n)
		print(n)

#Creacion venta y Configuracion
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
idCaja = tk.Entry(venta, state='readonly')
idCaja.place(x=150, y=60)
marcaCaja = tk.Entry(venta, state='readonly')
marcaCaja.place(x=150, y=85)
modeCaja = tk.Entry(venta, state='readonly')
modeCaja.place(x=150, y=110)
tipoCaja = tk.Entry(venta, state='readonly')
tipoCaja.place(x=150, y=135)
precioCaja = tk.Entry(venta, state='readonly')
precioCaja.place(x=150, y=160)
cantCaja = tk.Entry(venta, state='readonly')
cantCaja.place(x=150, y=185)
clienCaja = tk.Entry(venta)
clienCaja.place(x=150, y=225)
cantSpn = tk.Spinbox(venta, from_=0, to=1000, width=18, state='readonly')
cantSpn.place(x=150, y=250)
telCaja = tk.Entry(venta)
telCaja.place(x=150, y=275)
direCaja = tk.Entry(venta)
direCaja.place(x=150, y=300)

#Boton
imgi = PhotoImage(file='vender.png')
btnVen=tk.Button(venta, text="vender", image=imgi, width=60, command=lambda: obtenerDatos())
btnVen.place(x=120, y=350)


#////////////////////////////////
venta.mainloop()