class Stap:
    def __init__(self, beschrijving):
        self.__beschrijving = beschrijving
        self.__tip = None  # standaard geen tip

    def get_beschrijving(self):
        return self.__beschrijving

    def voeg_tip_toe(self, tip):
        self.__tip = tip

    def get_tip(self):
        return self.__tip

    def __str__(self):
        return self.__beschrijving