import tkinter as tk
ventana = tk.Tk()

ventana.title("ventanana Python")
ventana.geometry("1000x600")
ventana.configure(bg="OldLace")
titulo=tk.Label(ventana,text="Albar's Moto Sport", bg="OldLace")
etiqueta=tk.Label(ventana,text="Bienvenido Al Sistema ABCC", bg="OldLace")
titulo.pack(fill=tk.X)
etiqueta.pack()
ventana.mainloop()