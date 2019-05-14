import pygame
from pygame.sprite import Sprite
from pygame import *
from rombo import *
import util

class ObjetoPool:
    __instancia = None
    __rombo = list()

    def __init__(self):
        if ObjetoPool.__instancia != None:
            raise NotImplemented("Esta es una clase singleton.")

    @staticmethod
    def getInstancia():
        if ObjetoPool.__instancia == None:
            ObjetoPool.__instancia = ObjetoPool()
        return ObjetoPool.__instancia

    def getRombo(self):
        if len(self.__rombo) > 0:
            print "Usando rombo existente."
            return self.__rombo.pop(0)
        else:
            print "Creando nuevo rombo."
            return Rombo((100,100),0)



    def renovarRombo(self, retornado):
        retornado.resetear()
        self.__rombo.append(retornado)
