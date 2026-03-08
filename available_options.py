"""
available_options.py
Définition de toutes les options disponibles pour le générateur de calendrier.
"""
from enum import Enum
from reportlab.lib.pagesizes import A4, A5
from reportlab.lib.units import cm


class PageFormat(Enum):
    A4 = A4
    A5 = A5


class Orientation(Enum):
    PORTRAIT = "portrait"
    PAYSAGE = "paysage"


class BgColor(Enum):
    BEIGE = "#ECE7D2"
    BLANC = "#FFFFFF"
    NOIR = "#000000"


class Font(Enum):
    COURIER              = "Courier"
    COURIER_BOLD         = "Courier-Bold"
    COURIER_OBLIQUE      = "Courier-Oblique"
    COURIER_BOLD_OBLIQUE = "Courier-BoldOblique"
    HELVETICA            = "Helvetica"
    HELVETICA_BOLD       = "Helvetica-Bold"
    HELVETICA_OBLIQUE    = "Helvetica-Oblique"
    HELVETICA_BOLD_OBLIQUE = "Helvetica-BoldOblique"
    TIMES                = "Times-Roman"
    TIMES_BOLD           = "Times-Bold"
    TIMES_ITALIC         = "Times-Italic"
    TIMES_BOLD_ITALIC    = "Times-BoldItalic"
    SYMBOL               = "Symbol"
    ZAPF_DINGBATS        = "ZapfDingbats"


class ViewMode(Enum):
    JOURNALIERE   = "journalière"
    HEBDOMADAIRE  = "hebdomadaire"
    MENSUELLE     = "mensuelle"


class WeekStart(Enum):
    LUNDI    = 0   # valeur utilisée par calendar.Calendar(firstweekday=...)
    DIMANCHE = 6


class TimeSlot(Enum):
    QUINZE_MIN  = "15 min"
    TRENTE_MIN  = "30 min"
    UNE_HEURE   = "1h"


class SectionType(Enum):
    PRO    = "pro"
    PERSO  = "perso"
    ETUDES = "études"


class Language(Enum):
    FR3 = "fr3"   # Lun, Mar …
    FR  = "fr"    # Lundi, Mardi …
    EN3 = "en3"   # Mon, Tue …
    EN  = "en"    # Monday, Tuesday …


# Noms des jours par langue
DAY_NAMES: dict[str, list[str]] = {
    Language.FR3.value: ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"],
    Language.FR.value:  ["Lundi", "Mardi", "Mercredi", "Jeudi",
                         "Vendredi", "Samedi", "Dimanche"],
    Language.EN3.value: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    Language.EN.value:  ["Monday", "Tuesday", "Wednesday", "Thursday",
                         "Friday", "Saturday", "Sunday"],
}


def get_day_names(language: Language = Language.FR3) -> list[str]:
    """Retourne la liste des noms de jours pour la langue choisie."""
    try:
        return DAY_NAMES[language.value]
    except KeyError:
        raise ValueError(f"Langue non supportée : {language}")
