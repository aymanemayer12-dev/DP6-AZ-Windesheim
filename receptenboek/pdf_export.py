from reportlab.pdfgen import canvas

def exporteer_recept_naar_pdf(recept):

    bestandsnaam = recept.naam.replace(" ", "_") + ".pdf"

    c = canvas.Canvas(bestandsnaam)

    y = 800

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, recept.naam)

    y -= 30
    c.setFont("Helvetica", 12)
    c.drawString(50, y, recept.omschrijving)

    y -= 40
    c.drawString(50, y, "Ingrediënten:")

    for ingredient in recept.ingredienten:
        y -= 20
        tekst = f"- {ingredient.naam} ({ingredient.hoeveelheid})"
        c.drawString(60, y, tekst)

    y -= 30
    c.drawString(50, y, "Stappen:")

    nummer = 1
    for stap in recept.stappen:
        y -= 20
        c.drawString(60, y, f"{nummer}. {stap.beschrijving}")
        nummer += 1

    c.save()

    print("PDF opgeslagen als:", bestandsnaam)