from reportlab.lib.units import cm 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5

##Celendrier
import datetime as dt 
import calendar as cal


HAUTEUR, LARGEUR = A5
cm = 0.5 * cm

def doted_canvas(c, space, radius):
    cmonth = c
    HAUTEUR, LARGEUR = A5
    for i in range(0,int(LARGEUR) ) : 
        for j in range(0, int(HAUTEUR)) : 
            cmonth.circle(j*space*cm,i*space*cm, radius*cm)

def draw_month_calendar(canvas_obj, year, month, x, y, 
                        font_name="Courier", 
                        font_size=9, 
                        day_width=3):
    """
    Dessine un calendrier mensuel à la position (x,y) - coin haut gauche.
    
    Args:
        canvas_obj: objet canvas ReportLab
        year: année (int)
        month: mois 1-12 (int)
        x, y: position en points ou cm (coin haut gauche)
        font_name: police (monospace recommandé pour l'alignement)
        font_size: taille de police
        day_width: largeur en caractères pour formatmonth
    """
    cldr = cal.TextCalendar()
    
    # Création et dessin
    text_obj = canvas_obj.beginText(x, y)
    text_obj.setFont(font_name, font_size)
    text_obj.textLines(cldr.formatmonth(year, month, day_width))
    canvas_obj.drawText(text_obj)
    
    # Retourne la hauteur approximative utilisée (utile pour placer le suivant)
    lines = len(cldr.formatmonth(year, month, day_width).split('\n'))
    return lines * (font_size * 1.2)  # hauteur estimée en points

def month1(year, months : list):
    doted_canvas(c,1, 0.01 )
    months = [i+1 for i in range(12)]
    year = 2026
    for i,month in enumerate(months[:6]):
        draw_month_calendar(c, year, month,3*cm, 3*cm+ (9*cm*i)) 
        c.line( 3*cm, 10*cm+ (9*cm*i), LARGEUR-3*cm, 10*cm+ (9*cm*i))
    

    c.showPage()
    
    doted_canvas(c,space, size )
    for i,month in enumerate(months[6:]):
        #draw_month_calendar(c, year, month,3*cm, 3*cm+ (9*cm*i)) 
        c.line( 3*cm, 10*cm+ (9*cm*i), LARGEUR-3*cm, 10*cm+ (9*cm*i))


if __name__ == "__main__":
    c = canvas.Canvas("monthly2.pdf", bottomup=0)
    #doted_canvas(c)
    months = [i+1 for i in range(12)]
    year = 2026
    for i,month in enumerate(months[:6]):
        draw_month_calendar(c, year, month,3*cm, 3*cm+ (9*cm*i)) 
        c.line( 3*cm, 10*cm+ (9*cm*i), LARGEUR-3*cm, 10*cm+ (9*cm*i))
    

    c.showPage()
    
    #doted_canvas(c,1, 0.01 )
    for i,month in enumerate(months[6:]):
        draw_month_calendar(c, year, month,3*cm, 3*cm+ (9*cm*i)) 
        c.line( 3*cm, 10*cm+ (9*cm*i), LARGEUR-3*cm, 10*cm+ (9*cm*i))
    c.showPage()
    c.save()
