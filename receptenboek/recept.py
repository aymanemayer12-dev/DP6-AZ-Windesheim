class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []
        self.__aantal_personen = 1  # standaard 1 persoon

    # Getters
    def get_naam(self):
        return self.__naam

    def get_aantal_personen(self):
        return self.__aantal_personen

    def voeg_ingredient_toe(self, ingredient):
        self.__ingredient_list.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def set_aantal_personen(self, aantal):
        if aantal > 0:
            self.__aantal_personen = aantal
            for ingredient in self.__ingredient_list:
                ingredient.update_hoeveelheid(aantal)
        else:
            print("Aantal personen moet groter dan 0 zijn.")

    def bereken_calorieen(self):
        totaal_kcal = 0
        for ingredient in self.__ingredient_list:
            totaal_kcal += ingredient.get_kcal()
        return totaal_kcal

    def toon_recept(self):
        print(f"\n=== {self.__naam} ===")
        print(self.__omschrijving)
        print(f"\nAantal personen: {self.__aantal_personen}")

        print("\nIngrediënten:")
        for ingredient in self.__ingredient_list:
            print(f"- {ingredient}")

        print("\nBereidingsstappen:")
        for i, stap in enumerate(self.__stappen, start=1):
            print(f"{i}. {stap}")
            if stap.get_tip():
                print(f"   Tip: {stap.get_tip()}")

        print(f"\nTotale calorieën: {self.bereken_calorieen()} kcal")