from reportlab.pdfgen import canvas
import datetime as dt
from reportlab.lib.units import cm
import calendar
import user_config as uc

# Configuration utilisateur
ucc = uc.config

def dessiner_grille_pointillee(c, largeur, hauteur, espacement=1*cm, rayon_point=0.1):
    """Dessine une grille pointillée sur le PDF"""
    x = 0
    while x <= largeur:
        y = 0
        while y <= hauteur:
            c.circle(x, y, rayon_point, fill=1)
            y += espacement
        x += espacement



if __name__ == "__main__":
    # Créer un nouveau PDF
    print(f"{uc.config["format_doc"].value}")
    c = canvas.Canvas("monthly.pdf", pagesize=uc.config["format_doc"].value, bottomup=0)

    # Dimensions de la page
    largeur, hauteur = ucc["format_doc"]

    # Dessiner une grille pointillée
    #dessiner_grille_pointillee(c, largeur, hauteur)

    # Dessiner une première grille avec les noms des jours
    case_x1 = [(i*5+14)*cm for i in range(3)]
    case_y1 = [(3+5*i)*cm for i in range(4)]


    # Passer à une nouvelle page
    c.showPage()

    # Dessiner une deuxième grille
    case_x2 = [(i*5+1)*cm for i in range(4)]
    case_y2 = [(i*5+3)*cm for i in range(4)]
    c.grid(case_x2, case_y2)

    

    # Enregistrer le PDF
    c.save()
    print("PDF généré avec succès !")
