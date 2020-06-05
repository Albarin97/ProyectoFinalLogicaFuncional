import tkinter as tk
from tkinter import messagebox as MB
from tkinter import PhotoImage
#from PIL import Image, ImageTk

#Creacion login y Configuracion
login = tk.Tk()
login.iconbitmap("logear.ico")
login.title("Login")
login.geometry("300x300")
login.configure(bg="OldLace")

#Titulo
titulo=tk.Label(login,text="Albar's Moto Sport", bg="OldLace")
titulo.pack(fill=tk.X)
etiqueta=tk.Label(login,text="Introduce Los Siguientes Datos", bg="OldLace")
etiqueta.pack()

#etiquetas
usLabel=tk.Label(login, text="Usuario", bg="OldLace")
usLabel.place(x=20, y=80)
conLabel=tk.Label(login, text="Contraseña", bg="OldLace")
conLabel.place(x=20, y=180)

#cajas
usCaja=tk.Entry(login)
usCaja.place(x=100, y=80)
conCaja=tk.Entry(login,show="*")
conCaja.place(x=100, y=180)

#boton
img = PhotoImage(file='login.png')
btnIniciar=tk.Button(login, image=img, text="Iniciar", width=60, command=lambda: obtenerDatos())
btnIniciar.place(x=130, y=250)

#vars
strUs=tk.StringVar()
strCon=tk.StringVar()

#defs
def obtenerDatos():
	strUs.set(usCaja.get())
	strCon.set(conCaja.get())

	if not strUs.get() or not strCon.get():
		MB.showerror("Error", "Llena Los Campos")
	elif not strUs.get().isalpha():
		MB.showerror("Error", "Usuario Solo Puede Llevar LETRAS")
	else:
		if strUs.get()=="a" and strCon.get()=="a":
			abrirVentana()
		else:
			MB.showerror("Error", "Usuario o Contraseña Incorrectos")	


def abrirVentana():
	login.destroy()
	import ventana

#//////////////
login.mainloop()