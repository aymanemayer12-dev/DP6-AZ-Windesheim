class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid, kcal):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__basis_hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__basis_kcal = kcal  # kcal voor 1 persoon

    def get_naam(self):
        return self.__naam

    def get_hoeveelheid(self):
        return self.__hoeveelheid

    def get_eenheid(self):
        return self.__eenheid

    def update_hoeveelheid(self, aantal_personen):
        self.__hoeveelheid = self.__basis_hoeveelheid * aantal_personen

    def get_kcal(self):
        verhouding = self.__hoeveelheid / self.__basis_hoeveelheid
        return self.__basis_kcal * verhouding

    def __str__(self):
        return f"{self.__hoeveelheid} {self.__eenheid} {self.__naam}"