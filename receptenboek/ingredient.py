class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid, kcal):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal = kcal

    def get_naam(self):
        return self.__naam

    def get_hoeveelheid(self):
        return self.__hoeveelheid

    def get_eenheid(self):
        return self.__eenheid

    def get_kcal(self):
        return self.__kcal

    def __str__(self):
        return f"{self.__hoeveelheid} {self.__eenheid} {self.__naam}"