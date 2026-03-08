from reportlab.pdfgen import canvas

def exporteer_recept_naar_pdf(recept):

    naam = recept.get_naam()
    bestandsnaam = naam.replace(" ", "_") + ".pdf"

    c = canvas.Canvas(bestandsnaam)

    y = 800

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, naam)

    y -= 30
    c.setFont("Helvetica", 12)
    c.drawString(50, y, "Aantal personen: " + str(recept.get_aantal_personen()))

    y -= 40
    c.drawString(50, y, "Ingredienten:")

    for ingredient in recept._Recept__ingredient_list:
        y -= 20
        tekst = f"- {ingredient}"
        c.drawString(60, y, tekst)

    y -= 30
    c.drawString(50, y, "Stappen:")

    nummer = 1
    for stap in recept._Recept__stappen:
        y -= 20
        c.drawString(60, y, f"{nummer}. {stap}")
        nummer += 1

    y -= 30
    kcal = recept.bereken_calorieen()
    c.drawString(50, y, f"Totale calorieen: {kcal} kcal")

    c.save()

    print("PDF opgeslagen als:", bestandsnaam)