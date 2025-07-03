from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# DEFINIR EL DOCUMENTO Y EL TAMAÑO
doc = SimpleDocTemplate('Hello.pdf',pagesize=LETTER)

# OBTENER ESTILOS PREDEFINIDOS
styles = getSampleStyleSheet()

# CONSTRUIT LISTA DE ELEMENTOS FLOWABLES O FLUIBLES
story = []
story.append(Paragraph("Hola ReportLab", styles['Title']))
story.append(Spacer(1,12))
story.append(Paragraph("Este es mi primer PDF generado con Platypus",styles['Normal']))

# GENERAR EL PDF
doc.build(story)