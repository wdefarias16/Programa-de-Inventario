from reportlab.lib.pagesizes import LETTER, landscape
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame,
    Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# 1) Datos de prueba
records = [
    {"codigo": f"P{i:03}", "descripcion": f"Producto número {i} con descripción muy larga",
     "cantidad": (i % 5) + 1, "precio": round(1.0 + (i % 10)*0.75,2)}
    for i in range(1, 101)
]

# 2) Preparar 'data' con encabezado y totales
data = [["Código", "Descripción", "Cant.", "Precio U.", "Subtotal"]]
total_general = 0
for rec in records:
    subtotal = rec["cantidad"] * rec["precio"]
    total_general += subtotal
    data.append([
        rec["codigo"],
        rec["descripcion"],
        rec["cantidad"],
        f"${rec['precio']:.2f}",
        f"${subtotal:.2f}"
    ])
# Fila de total general
data.append(["", "TOTAL GENERAL", "", "", f"${total_general:.2f}"])

# 3) Estilos y wrapping
styles = getSampleStyleSheet()
wrap = ParagraphStyle("wrap", parent=styles["BodyText"], fontSize=8, leading=10)
for i in range(1, len(data)-1):
    data[i][1] = Paragraph(data[i][1], wrap)

# 4) Crear doc con espacio inferior para notas (footHeight)
footHeight = 50
doc = BaseDocTemplate(
    "multipage_footer.pdf",
    pagesize=landscape(LETTER),
    leftMargin=20,
    rightMargin=20,
    topMargin=30,
    bottomMargin=20 + footHeight  # margen inferior + espacio reservado
)

# 5) Definir un frame para contenido (tabla) reservando footHeight pt abajo
frame_table = Frame(
    doc.leftMargin,
    doc.bottomMargin - footHeight,      # empieza justo arriba del espacio reservado
    doc.width,
    doc.height - (footHeight),          # altura menor para dejar área libre
    id="table_frame"
)

# 6) Función para dibujar en cada página: numeración y texto en zona inferior
def footer_canvas(canvas, doc):
    # Número de página arriba a la derecha
    page_num = canvas.getPageNumber()
    txt = f"Página {page_num}"
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(
        doc.pagesize[0] - doc.rightMargin,
        doc.pagesize[1] - 15,
        txt
    )
    # Texto fijo en área inferior
    canvas.setFont("Helvetica-Oblique", 8)
    canvas.drawString(
        doc.leftMargin,
        doc.bottomMargin - footHeight + 15,
        "Aquí va tu nota o pie de página."
    )

# 7) Crear la PageTemplate con el frame y el callback
template = PageTemplate(id="withFooter", frames=[frame_table], onPage=footer_canvas)
doc.addPageTemplates([template])

# 8) Construir la tabla
col_widths = [40, doc.width * 0.50, 40, 60, 60]
table = Table(data, colWidths=col_widths, hAlign="LEFT", repeatRows=1)
table.setStyle(TableStyle([
    ("GRID",           (0,0), (-1,-1),      0.4, colors.grey),
    ("BACKGROUND",     (0,0), (-1,0),        colors.HexColor("#333333")),
    ("TEXTCOLOR",      (0,0), (-1,0),        colors.whitesmoke),
    ("FONTNAME",       (0,0), (-1,0),        "Helvetica-Bold"),
    ("ROWBACKGROUNDS", (0,1), (-1,-2),       [colors.white, colors.HexColor("#f0f0f0")]),
    ("BACKGROUND",     (0,-1), (-1,-1),      colors.HexColor("#d9edf7")),
    ("FONTNAME",       (0,-1), (-1,-1),      "Helvetica-Bold"),
    ("SPAN",           (0,-1),  (3,-1)),
    ("ALIGN",          (4,-1),  (4,-1),      "RIGHT"),
    ("ALIGN",          (2,1),   (2,-2),      "CENTER"),
    ("ALIGN",          (3,1),   (-1,-2),      "RIGHT"),
]))

# 9) Montar el story y generar el PDF
story = [Paragraph("Reporte con nota inferior y numeración", styles["Title"]), Spacer(1,12), table]
doc.build(story)