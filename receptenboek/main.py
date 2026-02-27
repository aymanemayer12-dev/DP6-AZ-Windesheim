from recept import Recept
from ingredient import Ingredient
from stap import Stap

def main():
    recepten = []

    # Recept 1
    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes.")
    recept1.voeg_ingredient_toe(Ingredient("kip", 500, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("rijst", 100, "gram"))

    recept1.voeg_stap_toe(Stap("Snijd de kip in blokjes."))
    recept1.voeg_stap_toe(Stap("Bak de kip gaar in een pan."))

    # Recept 2
    recept2 = Recept("Pasta Pesto", "Pasta met zelfgemaakte pesto.")
    
    recept2.voeg_ingredient_toe(Ingredient("pasta", 100, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("basilicum", 50, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("parmezaanse kaas", 30, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("pijnboompitten", 20, "gram"))

    recept2.voeg_stap_toe(Stap("Kook de pasta volgens de aanwijzingen op de verpakking."))
    recept2.voeg_stap_toe(Stap("Maak de pesto door basilicum, parmezaanse kaas en pijnboompitten te mengen."))
    recept2.voeg_stap_toe(Stap("Meng de pesto door de gekookte pasta."))

    #Recept 3
    recept3 = Recept("Tropical Cheesecake Taco's", "Cheesecake taco's met een tropische twist.")

    recept3.voeg_ingredient_toe(Ingredient("Debic Cheesecake", 5, "dL"))
    recept3.voeg_ingredient_toe(Ingredient("Mangopuree", 1, "dL"))
    recept3.voeg_ingredient_toe(Ingredient("Taco schelpen", 4, "stuks"))
    recept3.voeg_ingredient_toe(Ingredient("Verse basilicum", 2, "takjes"))
    recept3.voeg_ingredient_toe(Ingredient("Kokosflakes", 4, "el"))
    recept3.voeg_ingredient_toe(Ingredient("Rode peper", 0.16, "stuk"))

    recept3.voeg_stap_toe(Stap("Houd de fles Debic cheesecake onder de warme kraan zodat de inhoud licht smelt."))
    recept3.voeg_stap_toe(Stap("Schenk in de kom van de planeetmenger en klop de cheesecake in 5 minuten zeer luchtig. Optioneel kun je dit ook doen met de handmixer."))
    recept3.voeg_stap_toe(Stap("Snijd ondertussen de rode peper ragfijn. Houd enkele topjes Thaise basilicum apart en snijd de rest van de blaadjes ragfijn. Rooster de kokosflakes in een droge pan."))
    recept3.voeg_stap_toe(Stap("Voeg de mangopuree toe aan de cheesecake en laat nog kort kloppen. Meng er de Thaise basilicum en de rode peper naar smaak doorheen"))
    recept3.voeg_stap_toe(Stap("Schep de massa in een spuitzak met een gekarteld mondje en spuit de massa in de chocoladetaco’s. Spuit aan de buitenrand de massa als een mooi patroon erop."))
    recept3.voeg_stap_toe(Stap("Bestrooi met de geroosterde kokosflakes en garneer naar eigen inzicht met de topjes Thaise basilicum en mango-passie crunch."))


    recepten.append(recept1)
    recepten.append(recept2)
    recepten.append(recept3)

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