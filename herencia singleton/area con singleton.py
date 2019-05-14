from math import pi

class Figura(object):
    __instance = None
    area = None
    radio = None
    
    """ Una figura en el plano. """

    def __new__(cls):
        if Circulo.__instance is None:
            Circulo.__instance = object.__new__(cls)
        return Circulo.__instance
    
    def area(self):
        " Este método debe ser redefinido. "
        pass


class Circulo(Figura):
    """ Un círculo en el plano. """

    def area(self):
        " Devuelve el área del círculo. "
        return pi * self.radio * self.radio
