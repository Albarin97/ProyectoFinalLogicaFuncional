import tkinter as tk

#Creacion login y Configuracion
login = tk.Tk()
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
btnIniciar=tk.Button(login, text="Iniciar")
btnIniciar.place(x=130, y=250)

#//////////////
login.mainloop()