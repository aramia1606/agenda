from reportlab.lib.pagesizes import A5
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
import datetime as dt
import calendar as cal

LARGEUR, HAUTEUR = A5
year_actu = 2026
month_actu = 3

# ✅ Correction : pas de crochets supplémentaires, monthdayscalendar retourne déjà une liste
cal_prev = cal.Calendar().monthdayscalendar(year_actu, month_actu-1)
cal_now = cal.Calendar().monthdayscalendar(year_actu, month_actu)
cal_after = cal.Calendar().monthdayscalendar(year_actu, month_actu+1)

# ✅ Division flottante pour ReportLab (// donne un int, / donne un float nécessaire)
x_o = [1*cm, LARGEUR/2]
y_o = [1*cm, 1*cm]

size = 10  # square
c = canvas.Canvas("yearly_Staff.pdf", pagesize=A5)  # ✅ .pdf pas .pdr
dates = " L   M   M   J   V   S   D"

print(f'{cal_prev=}\n{cal_now=}\n{cal_after=}')

# ✅ Ton one-liner fonctionne, juste une typo dans le print final
str_answer_prev =dates + "\n".join(
    "  ".join("  " if j == 0 else f"{j:2d}" for j in week)
    for week in cal_prev
)

print(f"{str_answer_prev}")  # ✅ str_answer_prev pas str_answern_prev

# N'oublie pas à la fin :
# c.save()
