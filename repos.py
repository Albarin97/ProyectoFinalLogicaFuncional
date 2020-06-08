import itertools
from random import randint
import webbrowser as wb
from statistics import mean
from reportlab.lib.pagesizes import *
from reportlab.lib.fonts import *
from reportlab.pdfgen import canvas
import conexion as con

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(args)
def export_to_pdf(nombre):
    registros = con.DataBase().select_pedidos()
    #print(registros)
    data = [("idventa", "marca", "modelo", "tipo", "cliente", "cantidad", "costo")]
    for row in registros:
        data.append((str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6])))
    c = canvas.Canvas("reportes/"+nombre, pagesize=A4)
    text=c.beginText(10,810,None)
    text.setFont("Times-Roman", 12)
    text.textLine("ALBAR'S MOTO SPORT: --REPORTE DE VENTAS--")
    c.drawText(text)
    w, h = A4
    max_rows_per_page = 45
    # Margin.
    x_offset = 50
    y_offset = 50
    # Space between rows.
    padding = 15
    #ipadding = 60

    xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]

    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()

    c.save()
    wb.open_new('C:/Users/albar/Desktop/ProyectoLogicaFuncional/ProyectoFinalLogicaFuncional/'+nombre)

export_to_pdf("test.pdf")