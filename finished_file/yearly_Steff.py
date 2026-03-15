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
    tree.write(".\\finished_file\\"+name_file[:-4]+str(month)+ ".svg")


import xml.etree.ElementTree as ET
import os

def clean_xml(input_file):
    # Vérifier que le fichier existe
    if not os.path.exists(input_file):
        print(f"Erreur: Le fichier {input_file} n'existe pas")
        return False

    try:
        # Charger le SVG
        tree = ET.parse(input_file)
        root = tree.getroot()

        # Supprimer les namespaces (méthode plus robuste)
        for elem in root.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]  # Supprime le namespace
            # Supprimer les attributs de namespace
            elem.attrib = {
                k.split('}')[-1]: v
                for k, v in elem.attrib.items()
                if '}' in k
            } or {
                k: v
                for k, v in elem.attrib.items()
                if '}' not in k
            }

        # Créer le nom de fichier de sortie
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_clean.svg"

        # Sauvegarder le SVG nettoyé
        tree.write(output_file, encoding="utf-8", xml_declaration=True)
        print(f"Fichier nettoyé sauvegardé sous: {output_file}")
        return True

    except ET.ParseError as e:
        print(f"Erreur de parsing XML: {e}")
        return False
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return False
def call_clean_xml() : 
    for i in range(1, 13):
        # Chemin relatif vers le fichier (ajustez selon votre structure)
            input_file = os.path.join("finished_file", f"calendar_XS{i}.svg")
            clean_xml(input_file)
import xml.etree.ElementTree as ET
import os
from copy import deepcopy

def clean_xml(input_file):
    try:
        # Charger le SVG
        tree = ET.parse(input_file)
        root = tree.getroot()

        # 1. Nettoyer les namespaces dans les balises
        for elem in root.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]

        # 2. Nettoyer les namespaces dans les attributs
        for elem in root.iter():
            new_attrs = {}
            for attr, value in elem.attrib.items():
                if '}' in attr:
                    new_attr = attr.split('}', 1)[1]
                    new_attrs[new_attr] = value
                else:
                    new_attrs[attr] = value
            elem.attrib = new_attrs

        # 3. Supprimer les éléments inutiles (namedview, defs)
        for elem in root.findall('namedview'):
            root.remove(elem)
        for elem in root.findall('defs'):
            root.remove(elem)

        # 4. Créer le nom de fichier de sortie
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_clean.svg"

        # 5. Sauvegarder le SVG nettoyé
        tree.write(output_file, encoding="utf-8", xml_declaration=True)
        print(f"Fichier nettoyé sauvegardé sous: {output_file}")

        return output_file

    except Exception as e:
        print(f"Erreur: {e}")
        return None

def create_main_svg(calendar_files, output_file="final_product.svg"):
    # Créer l'élément SVG principal
    svg = ET.Element("svg", {
        "xmlns": "http://www.w3.org/2000/svg",
        "width": "210mm",
        "height": "297mm",
        "viewBox": "0 0 210 297"
    })

    # Ajouter un groupe pour contenir tous les calendriers
    calendars_group = ET.SubElement(svg, "g", {
        "transform": "translate(10, 20)"
    })

    # Position initiale
    x, y = 0, 0
    max_width = 60  # Largeur maximale pour un calendrier

    for i, calendar_file in enumerate(calendar_files):
        # Nettoyer le fichier si ce n'est pas déjà fait
        if not calendar_file.endswith("_clean.svg"):
            calendar_file = clean_xml(calendar_file)

        if calendar_file:
            # Charger le calendrier nettoyé
            calendar_tree = ET.parse(calendar_file)
            calendar_root = calendar_tree.getroot()

            # Cloner le groupe principal du calendrier
            calendar_group = calendar_root.find(".//g[@id='layer1']")
            if calendar_group is not None:
                cloned_group = deepcopy(calendar_group)

                # Ajouter une transformation pour positionner le calendrier
                current_transform = cloned_group.get("transform", "")
                cloned_group.set("transform", f"{current_transform} translate({x}, {y})")

                # Ajouter au groupe principal
                calendars_group.append(cloned_group)

                # Calculer la position du prochain calendrier
                x += max_width
                if x > 180:  # Si on dépasse la largeur de la page
                    x = 0
                    y += 40  # Hauteur d'un calendrier + marge

    # Sauvegarder le SVG final
    ET.ElementTree(svg).write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"Fichier final sauvegardé sous: {output_file}")

if __name__ == "__main__":
    # Chemin vers les fichiers
    folder = "finished_file"
    calendar_files = [
        os.path.join(folder, f"calendar_XSimport xml.etree.ElementTree as ET
import os
from copy import deepcopy

def clean_xml(input_file):
    try:
        # Charger le SVG
        tree = ET.parse(input_file)
        root = tree.getroot()

        # 1. Nettoyer les namespaces dans les balises
        for elem in root.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]

        # 2. Nettoyer les namespaces dans les attributs
        for elem in root.iter():
            new_attrs = {}
            for attr, value in elem.attrib.items():
                if '}' in attr:
                    new_attr = attr.split('}', 1)[1]
                    new_attrs[new_attr] = value
                else:
                    new_attrs[attr] = value
            elem.attrib = new_attrs

        # 3. Supprimer les éléments inutiles (namedview, defs)
        for elem in root.findall('namedview'):
            root.remove(elem)
        for elem in root.findall('defs'):
            root.remove(elem)

        # 4. Créer le nom de fichier de sortie
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_clean.svg"

        # 5. Sauvegarder le SVG nettoyé
        tree.write(output_file, encoding="utf-8", xml_declaration=True)
        print(f"Fichier nettoyé sauvegardé sous: {output_file}")

        return output_file

    except Exception as e:
        print(f"Erreur: {e}")
        return None

def create_main_svg(calendar_files, output_file="final_product.svg"):
    # Créer l'élément SVG principal
    svg = ET.Element("svg", {
        "xmlns": "http://www.w3.org/2000/svg",
        "width": "210mm",
        "height": "297mm",
        "viewBox": "0 0 210 297"
    })

    # Ajouter un groupe pour contenir tous les calendriers
    calendars_group = ET.SubElement(svg, "g", {
        "transform": "translate(10, 20)"
    })

    # Position initiale
    x, y = 0, 0
    max_width = 60  # Largeur maximale pour un calendrier

    for i, calendar_file in enumerate(calendar_files):
        # Nettoyer le fichier si ce n'est pas déjà fait
        if not calendar_file.endswith("_clean.svg"):
            calendar_file = clean_xml(calendar_file)

        if calendar_file:
            # Charger le calendrier nettoyé
            calendar_tree = ET.parse(calendar_file)
            calendar_root = calendar_tree.getroot()

            # Cloner le groupe principal du calendrier
            calendar_group = calendar_root.find(".//g[@id='layer1']")
            if calendar_group is not None:
                cloned_group = deepcopy(calendar_group)

                # Ajouter une transformation pour positionner le calendrier
                current_transform = cloned_group.get("transform", "")
                cloned_group.set("transform", f"{current_transform} translate({x}, {y})")

                # Ajouter au groupe principal
                calendars_group.append(cloned_group)

                # Calculer la position du prochain calendrier
                x += max_width
                if x > 180:  # Si on dépasse la largeur de la page
                    x = 0
                    y += 40  # Hauteur d'un calendrier + marge

    # Sauvegarder le SVG final
    ET.ElementTree(svg).write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"Fichier final sauvegardé sous: {output_file}")

if __name__ == "__main__":
    # Chemin vers les fichiers
    folder = "finished_file"
    calendar_files = [
        os.path.join(folder, "calendar_XS22026.svg")
    ]

    # Créer le SVG final
    create_main_svg(calendar_files)

    # Créer le SVG final
    create_main_svg(calendar_files)


