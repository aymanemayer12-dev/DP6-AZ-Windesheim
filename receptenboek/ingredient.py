class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid

    def get_naam(self):
        return self.__naam

    def get_hoeveelheid(self):
        return self.__hoeveelheid

    def get_eenheid(self):
        return self.__eenheid

    def __str__(self):
        return f"{self.__hoeveelheid} {self.__eenheid} {self.__naam}"