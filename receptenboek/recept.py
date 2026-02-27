class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []

    def get_naam(self):
        return self.__naam

    def voeg_ingredient_toe(self, ingredient):
        self.__ingredient_list.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def toon_recept(self):
        print(f"\n=== {self.__naam} ===")
        print(self.__omschrijving)

        print("\nIngrediënten:")
        for ingredient in self.__ingredient_list:
            print(f"- {ingredient}")

        print("\nBereidingsstappen:")
        for i, stap in enumerate(self.__stappen, start=1):
            print(f"{i}. {stap}")