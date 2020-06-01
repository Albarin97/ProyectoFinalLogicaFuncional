import tkinter as tk

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

#cajas
idcaja = tk.Entry(ventana)
idcaja.place(x=20, y=20)

#//////////////
ventana.mainloop()