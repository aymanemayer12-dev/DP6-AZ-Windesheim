from recept import Recept
from ingredient import Ingredient
from stap import Stap

def main():
    recepten = []

    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes.")
    
    kip = Ingredient("kip", 500, "gram", 600)
    kip.set_plantaardig_alternatief("vegetarische kipstukjes")
    recept1.voeg_ingredient_toe(kip)

    recept1.voeg_ingredient_toe(Ingredient("rijst", 100, "gram", 300))

    recept1.voeg_stap_toe(Stap("Snijd de kip in blokjes."))
    recept1.voeg_stap_toe(Stap("Bak de kip gaar in een pan."))

    recept2 = Recept("Pasta Pesto", "Pasta met zelfgemaakte pesto.")
    
    recept2.voeg_ingredient_toe(Ingredient("pasta", 100, "gram", 300))
    recept2.voeg_ingredient_toe(Ingredient("basilicum", 50, "gram", 10))

    kaas = Ingredient("parmezaanse kaas", 30, "gram", 400)
    kaas.set_plantaardig_alternatief("vegan parmezaan")
    recept2.voeg_ingredient_toe(kaas)

    recept2.voeg_ingredient_toe(Ingredient("pijnboompitten", 20, "gram", 40))

    recept2.voeg_stap_toe(Stap("Kook de pasta volgens de aanwijzingen op de verpakking."))
    recept2.voeg_stap_toe(Stap("Maak de pesto door basilicum, parmezaanse kaas en pijnboompitten te mengen."))
    stap_met_tip = Stap("Roer de pesto door de gekookte pasta.")
    stap_met_tip.voeg_tip_toe("Voeg een scheutje olijfolie toe aan de pesto voor een romigere smaak.")
    recept2.voeg_stap_toe(stap_met_tip)

    recept3 = Recept("Tropical Cheesecake Taco's", "Cheesecake taco's met een tropische twist.")

    recept3.voeg_ingredient_toe(Ingredient("Debic Cheesecake", 5, "dL", 500))
    recept3.voeg_ingredient_toe(Ingredient("Mangopuree", 1, "dL", 200))
    recept3.voeg_ingredient_toe(Ingredient("Taco schelpen", 4, "stuks", 200))
    recept3.voeg_ingredient_toe(Ingredient("Verse basilicum", 2, "takjes", 50))
    recept3.voeg_ingredient_toe(Ingredient("Kokosflakes", 4, "el", 100))
    recept3.voeg_ingredient_toe(Ingredient("Rode peper", 0.16, "stuk", 20))

    recept3.voeg_stap_toe(Stap("Houd de fles Debic cheesecake onder de warme kraan zodat de inhoud licht smelt."))
    recept3.voeg_stap_toe(Stap("Schenk in de kom van de planeetmenger en klop de cheesecake in 5 minuten zeer luchtig."))

    stap_met_tip = Stap("Snijd ondertussen de rode peper ragfijn en rooster de kokosflakes.")
    stap_met_tip.voeg_tip_toe("Rooster de kokosflakes op laag vuur zodat ze niet verbranden.")
    recept3.voeg_stap_toe(stap_met_tip)

    recept3.voeg_stap_toe(Stap("Voeg de mangopuree toe en meng alles goed door."))
    recept3.voeg_stap_toe(Stap("Spuit de massa in de taco’s."))
    recept3.voeg_stap_toe(Stap("Garneer met kokosflakes en basilicum."))

    recepten.append(recept1)
    recepten.append(recept2)
    recepten.append(recept3)

    print("Overzicht recepten:")
    for i, recept in enumerate(recepten, start=1):
        print(f"{i}. {recept.get_naam()}")

    try:
        keuze = int(input("Kies een receptnummer: "))

        if 1 <= keuze <= len(recepten):
            gekozen_recept = recepten[keuze - 1]

            aantal = int(input("Voor hoeveel personen? "))
            gekozen_recept.set_aantal_personen(aantal)

            plant_keuze = input("Wil je de plantaardige versie? (ja/nee): ").lower()
            if plant_keuze == "ja":
                gekozen_recept.gebruik_plantaardige_versie()

            gekozen_recept.toon_recept()

        else:
            print("Ongeldige keuze.")

    except ValueError:
        print("Voer een geldig nummer in.")

if __name__ == "__main__":
    main()