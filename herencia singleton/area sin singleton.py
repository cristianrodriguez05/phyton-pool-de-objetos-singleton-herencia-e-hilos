from math import pi

class Figura(object):
    """ Una figura en el plano. """
    def area(self):
        " Este m�todo debe ser redefinido. "
        pass


class Circulo(Figura):
    """ Un c�rculo en el plano. """
    def __init__(self, radio=0):
        " Constructor de c�rculo. "
        self.radio = radio

    def area(self):
        " Devuelve el �rea del c�rculo. "
        return pi * self.radio * self.radio
