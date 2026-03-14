from reportlab.lib.pagesizes import A5
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from itertools import chain
import datetime as dt
import calendar as cal
import xml.etree.ElementTree as ET

def small_calendar(year_actu, month_actu):
    """Dessine un petit calendrier du mois donné à la position (x,y) haut-gauche"""
    # Récupération des semaines du mois

    # En-têtes des jours
    jours = list(cal.Calendar().monthdayscalendar(year_actu, month_actu))
    

    return jours
    
if __name__ == "__main__":
    tree = ET.parse("calendar_XSsvg.svg")
    root = tree.getroot()
    print(list(chain.from_iterable(small_calendar(2026, 3))))
    cal = list(chain.from_iterable(small_calendar(2026, 3)))
 
    res_dict = { i: f"{i:2d}" for i in range(32)}
    res_dict[0]= "  "
    map_list =list(map(res_dict.get, cal))
    cal_xml ="".join(("  ".join(map_list)))
    print(cal_xml)
    
 
        
             
    

    
    
    

