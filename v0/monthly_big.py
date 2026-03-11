from reportlab.lib.units import cm 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
from monthly2 import *
##caelendrier
import datetime as dt 
import calendar as cal


cm = 0.5 * cm
LARGEUR , HAUTEUR, = A5



if __name__ == "__main__": 
    c = canvas.Canvas("monthly2.pdf", bottomup=0, pagesize=A5)
    month = 3
    doted_canvas(c, 1, .02)
    year = 2026 
    for i,month in enumerate((month-1, month+1)): 
        draw_month_calendar(c, year, month, 2*cm, 2 *cm + (i*11*cm))
    c.showPage()
    c.save()