class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid, kcal):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal = kcal
        self.__basis_hoeveelheid = hoeveelheid
        self.__basis_kcal = kcal

        self.__plantaardig_alternatief = None
        self.__gebruik_alternatief = False

    def get_naam(self):
        if self.__gebruik_alternatief and self.__plantaardig_alternatief:
            return self.__plantaardig_alternatief
        return self.__naam

    def get_hoeveelheid(self):
        return self.__hoeveelheid

    def get_eenheid(self):
        return self.__eenheid

    def get_kcal(self):
        return self.__kcal

    def update_hoeveelheid(self, aantal_personen):
        self.__hoeveelheid = self.__basis_hoeveelheid * aantal_personen
        self.__kcal = self.__basis_kcal * aantal_personen

    def set_plantaardig_alternatief(self, alternatief_naam):
        self.__plantaardig_alternatief = alternatief_naam

    def gebruik_plantaardig(self):
        if self.__plantaardig_alternatief:
            self.__gebruik_alternatief = True

    def __str__(self):
        return f"{self.__hoeveelheid} {self.__eenheid} {self.get_naam()}"