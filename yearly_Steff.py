from reportlab.lib.pagesizes import A5
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from itertools import chain
import datetime as dt
import calendar as cal
import xml.etree.ElementTree as ET

def small_calendar(year_actu, month_actu):
    """Dessine un petit calendrier du mois donné à la position (x,y) haut-gauche"""
    # En-têtes des jours
    jours = list(cal.Calendar().monthdayscalendar(year_actu, month_actu))
    return jours
    
def make_calendar_XS(name_file : str , year =2026 ,month= 3 ):
    tree = ET.parse(name_file)
    root = tree.getroot()


    # print(list(chain.from_iterable(small_calendar(2026, 2))))
    cal = list(chain.from_iterable(small_calendar(year, month)))
 
    res_dict = { i: f"{i:2d}" for i in range(32)}
    res_dict[0]= "  "
    map_list =list(map(res_dict.get, cal))
    cal_xml ="".join(("  ".join(map_list)))
    # print(cal_xml)

    for i in range(6):
        root[2][0][i+1].text = cal_xml[i*28 : i*28 + 26]


    # root[2][0][6].text = cal_xml[(28+28+28+28+28+28):(28+28+28+28+28+28+26)]


    # 6. Sauvegarder le fichier (CRUCIAL !)
    tree.write(name_file[:""]+str(month) + "svg")
 

if __name__ == "__main__":
    make_calendar_XS("calendar_XS.svg", 2026, 4 )




    
    
    

