from recept import Recept
from ingredient import Ingredient
from stap import Stap

def main():
    recepten = []

    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes.")
    recept1.voeg_ingredient_toe(Ingredient("kip", 500, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("rijst", 100, "gram"))

    recept1.voeg_stap_toe(Stap("Snijd de kip in blokjes."))
    recept1.voeg_stap_toe(Stap("Bak de kip gaar in een pan."))

    recepten.append(recept1)

    # Overzicht tonen
    print("Overzicht recepten:")
    for i, recept in enumerate(recepten, start=1):
        print(f"{i}. {recept.get_naam()}")

    keuze = int(input("Kies een receptnummer: "))
    if 1 <= keuze <= len(recepten):
        recepten[keuze - 1].toon_recept()
    else:
        print("Ongeldige keuze.")

if __name__ == "__main__":
    main()