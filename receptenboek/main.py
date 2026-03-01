from recept import Recept
from ingredient import Ingredient
from stap import Stap

def maak_start_recepten():
    recepten = []

    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes.")
    kip = Ingredient("kip", 500, "gram", 600)
    kip.set_plantaardig_alternatief("vegetarische kipstukjes")
    recept1.voeg_ingredient_toe(kip)
    recept1.voeg_ingredient_toe(Ingredient("rijst", 100, "gram", 300))
    recept1.voeg_stap_toe(Stap("Snijd de kip in blokjes."))
    recept1.voeg_stap_toe(Stap("Bak de kip gaar in een pan."))
    recepten.append(recept1)

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
    recepten.append(recept2)

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
    recepten.append(recept3)

    return recepten


def toon_recept_flow(recepten):
    if not recepten:
        print("Er zijn nog geen recepten.")
        return

    print("\nOverzicht recepten:")
    for i, recept in enumerate(recepten, start=1):
        print(f"{i}. {recept.get_naam()}")

    try:
        keuze = int(input("Kies een receptnummer (0 = terug): "))

        if keuze == 0:
            return

        if 1 <= keuze <= len(recepten):
            gekozen_recept = recepten[keuze - 1]

            aantal = int(input("Voor hoeveel personen? "))
            gekozen_recept.set_aantal_personen(aantal)

            plant_keuze = input("Wil je de plantaardige versie? (ja/nee): ").lower()
            if plant_keuze == "ja":
                gekozen_recept.gebruik_plantaardige_versie()

            gekozen_recept.toon_recept()

            vervolg = input("\n1. Verwijderen\n2. Terug\nMaak een keuze: ")

            if vervolg == "1":
                recepten.remove(gekozen_recept)
                print("Recept verwijderd.")

        else:
            print("Ongeldige keuze.")

    except ValueError:
        print("Foutieve invoer.")


def main():
    recepten = maak_start_recepten()

    while True:
        print("\n--- Receptenboek ---")
        print("1. Toon overzicht recepten")
        print("2. Voeg recept toe")
        print("3. Exit")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            toon_recept_flow(recepten)

        elif keuze == "2":
            print("Toevoegen volgt.")

        elif keuze == "3":
            break

        else:
            print("Foutieve invoer. Kies 1, 2 of 3.")


if __name__ == "__main__":
    main()