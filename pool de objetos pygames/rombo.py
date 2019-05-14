import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Rombo(Sprite):
	def __init__(self,coord,vel):
		Sprite.__init__(self)
		print "aqui llegue."
		print vel
		print coord
		self.imagenes = [util.cargar_imagen('imagenes/rombox.png'),
                                        util.cargar_imagen('imagenes/rombo.png'),
                                        util.cargar_imagen('imagenes/rombo1.png'),
                                        util.cargar_imagen('imagenes/rombo2.png'),
                                        util.cargar_imagen('imagenes/rombo3.png'),
                                        util.cargar_imagen('imagenes/rombo4.png'),
                                        util.cargar_imagen('imagenes/rombo5.png')]
                self.i = vel
                self.image = self.imagenes[self.i]
                self.rect = self.image.get_rect()
                self.rect.move_ip(coord[0], coord[1])
    
        def resetear(self):
            self.image = self.imagenes[1]
            

