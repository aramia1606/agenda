from reportlab.lib.pagesizes import A5, A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from enum import Enum
import calendar

nom_fichier = "test0.pdf"
chosen_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cal= calendar.Calendar()
largeur, hauteur = A5
cm = 0.5 *cm

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
from enum import Enum

class DayNames(Enum):
    MONDAY = {"fr": "Lundi", "fr3": "Lun", "en": "Monday", "en3": "Mon"}
    TUESDAY = {"fr": "Mardi", "fr3": "Mar", "en": "Tuesday", "en3": "Tue"}
    WEDNESDAY = {"fr": "Mercredi", "fr3": "Mer", "en": "Wednesday", "en3": "Wed"}
    THURSDAY = {"fr": "Jeudi", "fr3": "Jeu", "en": "Thursday", "en3": "Thu"}
    FRIDAY = {"fr": "Vendredi", "fr3": "Ven", "en": "Friday", "en3": "Fri"}
    SATURDAY = {"fr": "Samedi", "fr3": "Sam", "en": "Saturday", "en3": "Sat"}
    SUNDAY = {"fr": "Dimanche", "fr3": "Dim", "en": "Sunday", "en3": "Sun"}


def get_name_day(language="fr3"):
    try:
        return [day.value[language] for day in DayNames]
    except KeyError:
        raise ValueError("Langage non supporté")

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