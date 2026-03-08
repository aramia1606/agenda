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


def dessiner_grille(c, cases_x, cases_y, texte=None):
    """Dessine une grille et ajoute du texte si spécifié"""
    c.grid(cases_x, cases_y)

    if texte is not None:
        for i, x in enumerate(cases_x[:-1]):
            for j, y in enumerate(cases_y[:-1]):
                c.drawString(x, y+13, texte[i % len(texte)])



if __name__ == "__main__":
    # Créer un nouveau PDF
    c = canvas.Canvas("monthly.pdf", pagesize=ucc["format_doc"], bottomup=0)

    # Dimensions de la page
    largeur, hauteur = ucc["format_doc"]

    # Dessiner une grille pointillée
    dessiner_grille_pointillee(c, largeur, hauteur)

    # Dessiner une première grille avec les noms des jours
    case_x1 = [(i*5+14)*cm for i in range(3)]
    case_y1 = [(3+5*i)*cm for i in range(4)]


    # Passer à une nouvelle page
    c.showPage()

    # Dessiner une deuxième grille
    case_x2 = [(i*5+1)*cm for i in range(4)]
    case_y2 = [(i*5+3)*cm for i in range(4)]
    dessiner_grille(c, case_x2, case_y2, texte=uc.get_name_day())

    # Dessiner un calendrier mensuel pour l'année 2025, mois 2 (février)
    dessiner_calendrier_mensuel(c, 2025, 2, ucc["debut_semaine"])

    # Enregistrer le PDF
    c.save()
    print("PDF généré avec succès !")
