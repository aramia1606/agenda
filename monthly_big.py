from reportlab.lib.units import cm 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
from monthly import draw_month_calendar
##caelendrier
import datetime as dt 
import calendar as cal


HAUTEUR, LARGEUR = A5
cm = 0.5 * cm


if __name__ == "__main__": 
    c = canvas.Canvas("monthly.pdf", pagesize=A5, bottomup=0)  # ← bottomup=0 = origine en haut
    
    # Vos positions sur la grille (en unités de 0.5cm)
    y_grid = [i+1 for i in range(5)]
 
    draw_month_calendar(c, 2026, 2, 1*cm, 10*cm)  # Mois 2 (février) )
    draw_month_calendar(c, 2026, 4, 1*cm, 4 *cm)  # 
    c.line(20*cm ,1 LARGEUR, 1 )
 
    c.showPage()
    c.save()
    print("PDF généré !")