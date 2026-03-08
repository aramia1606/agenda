from enum import Enum


nom_fichier = "test0.pdf"
chosen_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cal= calendar.Calendar()
largeur, hauteur = A5
cm = 0.5 *cm


# Définition des Enums pour les choix
class Orientation(Enum):
    A4 = "A4"
    A5 = "A5"
    AUTRE = "Autre"

class Landscape(Enum):
    PORTRAIT = "portrait"
    PAYSAGE = "paysage"

class BgColor(Enum):
    BEIGE = ("beige", "#ECE7D2")
    BLANC = ("blanc", "#FFFFFF")
    NOIR = ("noir", "#000000")

class PrincipalFont(Enum):
    ARIAL = "Arial"
    HELVETICA = "Helvetica"
    TIMES = "Times-Roman"
    COURIER = "Courier"
    COURIER_BOLD = "Courier-Bold"
    COURIER_OBLIQUE = "Courier-Oblique"
    COURIER_BOLD_OBLIQUE = "Courier-BoldOblique"
    HELVETICA_BOLD = "Helvetica-Bold"
    HELVETICA_OBLIQUE = "Helvetica-Oblique"
    HELVETICA_BOLD_OBLIQUE = "Helvetica-BoldOblique"
    TIMES_BOLD = "Times-Bold"
    TIMES_ITALIC = "Times-Italic"
    TIMES_BOLD_ITALIC = "Times-BoldItalic"
    SYMBOL = "Symbol"
    ZAPF_DINGBATS = "ZapfDingbats"

class ViewMode(Enum):
    JOURNALIERE = "journalière"
    HEBDOMADAIRE = "hebdomadaire"
    MENSUELLE = "mensuelle"

class WeekStart(Enum):
    LUNDI = "lundi"
    DIMANCHE = "dimanche"

class TimeSlot(Enum):
    QUINZE_MIN = "15 min"
    TRENTE_MIN = "30 min"
    UNE_HEURE = "1h"

class SectionType(Enum):
    PRO = "pro"
    PERSO = "perso"
    ETUDES = "études"

# Variables de configuration
config = {
    # Choix de base
    "format_doc": Orientation.A5,
    "orientation": Landscape.PORTRAIT,
    "couleur_papier": BgColor.BEIGE.value[1],
    "couleur_dominante": "#146698",

    # Polices
    "police_principale": PrincipalFont.ARIAL,
    "police_secondaire": "Helvetica",

    # Options avancées
    "taille_cases": "moyenne",
    "week_ends": "regroupés",
    "espace_notes": True,
    "marges": "min",

    # Nouveaux choix
    "vue_principale": ViewMode.JOURNALIERE,
    "semaine_1_page": True,
    "debut_semaine": WeekStart.LUNDI,
    "plage_horaire": [6,22],
    "decoupage_horaire": TimeSlot.TRENTE_MIN,
    "todo_list_quotidienne": True,
    "espace_priorites": True,
    "vue_mensuelle_recap": True,
    "page_annuelle": True,

    # Fonctionnalités organisationnelles avancées
    "oraganisation_avancee" : True,
    "sections_separees": [SectionType.PRO, SectionType.PERSO],
    "code_couleur_activites": {
        "pro": "#FF5733",
        "perso": "#33FF57",
        "etudes": "#3357FF"
    },
    "suivi_habitudes": True,
    "suivi_budget": True,
    "suivi_sport_sante": True,
    "modele_page_projet": True,
    "planification_mensuelle": True,
    "planification_annuelle": True,
    "index_personnalisable": True,
    "renvoi_pages": True,
    "pages_notes_libres": True,
    "revue_hebdomadaire": {
        "structurée": True,
        "sections": ["réflexion", "planification", "gratitude"]
    },
    "revue_mensuelle": {
        "structurée": True,
        "sections": ["bilan", "objectifs", "améliorations"]
    }
}

from enum import Enum

class DayNames(Enum):
    class Fr3:
        LUN = "Lun"
        MAR = "Mar"
        MER = "Mer"
        JEU = "Jeu"
        VEN = "Ven"
        SAM = "Sam"
        DIM = "Dim"

    class Fr:
        LUNDI = "Lundi"
        MARDI = "Mardi"
        MERCREDI = "Mercredi"
        JEUDI = "Jeudi"
        VENDREDI = "Vendredi"
        SAMEDI = "Samedi"
        DIMANCHE = "Dimanche"

    class En3:
        MON = "Mon"
        TUE = "Tue"
        WED = "Wed"
        THU = "Thu"
        FRI = "Fri"
        SAT = "Sat"
        SUN = "Sun"

    class En:
        MONDAY = "Monday"
        TUESDAY = "Tuesday"
        WEDNESDAY = "Wednesday"
        THURSDAY = "Thursday"
        FRIDAY = "Friday"
        SATURDAY = "Saturday"
        SUNDAY = "Sunday"

def get_name_day(langage="fr3"):
    if langage == "fr3":
        return [DayNames.Fr3.LUN.value, DayNames.Fr3.MAR.value,
                DayNames.Fr3.MER.value, DayNames.Fr3.JEU.value,
                DayNames.Fr3.VEN.value, DayNames.Fr3.SAM.value,
                DayNames.Fr3.DIM.value]
    elif langage == "fr":
        return [DayNames.Fr.LUNDI.value, DayNames.Fr.MARDI.value,
                DayNames.Fr.MERCREDI.value, DayNames.Fr.JEUDI.value,
                DayNames.Fr.VENDREDI.value, DayNames.Fr.SAMEDI.value,
                DayNames.Fr.DIMANCHE.value]
    elif langage == "en3":
        return [DayNames.En3.MON.value, DayNames.En3.TUE.value,
                DayNames.En3.WED.value, DayNames.En3.THU.value,
                DayNames.En3.FRI.value, DayNames.En3.SAT.value,
                DayNames.En3.SUN.value]
    elif langage == "en":
        return [DayNames.En.MONDAY.value, DayNames.En.TUESDAY.value,
                DayNames.En.WEDNESDAY.value, DayNames.En.THURSDAY.value,
                DayNames.En.FRIDAY.value, DayNames.En.SATURDAY.value,
                DayNames.En.SUNDAY.value]
    else:
        raise ValueError("Langage non supporté")


if __init__ == "__main__":
# Exemple d'utilisation
    print("Configuration du document :")
    print(f"Format: {config['format_doc']}")
    print(f"Orientation: {config['orientation']}")
    print(f"Couleur papier: {config['couleur_papier']}")
    print(f"Couleur dominante: {config['couleur_dominante']}")
    print(f"Vue principale: {config['vue_principale']}")
    print(f"Semaine sur 1 page: {'Oui' if config['semaine_1_page'] else 'Non'}")
    print(f"Début de semaine: {config['debut_semaine']}")
    print(f"Plage horaire: {config['plage_horaire']}")
    print(f"Découpage horaire: {config['decoupage_horaire']}")
    print(f"To-do list quotidienne: {'Oui' if config['todo_list_quotidienne'] else 'Non'}")
    print(f"Espace priorités: {'Oui' if config['espace_priorites'] else 'Non'}")
    print(f"Vue mensuelle récapitulative: {'Oui' if config['vue_mensuelle_recap'] else 'Non'}")
    print(f"Page annuelle: {'Oui' if config['page_annuelle'] else 'Non'}")

    # Affichage des sections séparées
    print("\nSections séparées:")
    for section in config['sections_separees']:
        print(f"- {section}")

    # Affichage des codes couleur
    print("\nCodes couleur par type d'activité:")
    for type_act, couleur in config['code_couleur_activites'].items():
        print(f"- {type_act}: {couleur}")

    # Affichage des revues
    print("\nRevue hebdomadaire:")
    print(f"Structurée: {'Oui' if config['revue_hebdomadaire']['structurée'] else 'Non'}")
    print("Sections:")
    for section in config['revue_hebdomadaire']['sections']:
        print(f"- {section}")

    print("\nRevue mensuelle:")
    print(f"Structurée: {'Oui' if config['revue_mensuelle']['structurée'] else 'Non'}")
    print("Sections:")
    for section in config['revue_mensuelle']['sections']:
        print(f"- {section}")
