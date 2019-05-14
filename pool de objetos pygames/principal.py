# -*- coding: utf-8 -*-

import sys
import pygame
import util
from pygame.locals import *
from rombo import *
from objetoPool import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
ICON_SIZE = 32


def game():
    pygame.init()
    
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Ejercicio Pool de Objetos" )
    background_image = util.cargar_imagen('imagenes/fondo.jpg');
    pygame.mouse.set_visible(True)
    mousex, mousey = (0,0)
    ejecutando = True
    temporizador = pygame.time.Clock()
    pool = ObjetoPool.getInstancia()
    listo = True
    j = 5
    t = 0
    z = 0
    i = 0
    usuario1=0
    usuario2=0
    usuario3=0
    usuario4=0
    usuario5=0
    x = [50,160,270,380,490]
    y = [300,300,300,300,300]
    rombouno = Rombo((0,0),0)
    rombodos = Rombo((0,0),0)
    rombotres = Rombo((0,0),0)
    rombocuat = Rombo((0,0),0)
    rombocinco = Rombo((0,0),0)
    while ejecutando:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                ejecutando = False
                sys.exit()
        teclas = pygame.key.get_pressed()
        mousex, mousey = pygame.mouse.get_pos()
        
        if listo:
            screen.blit(background_image, (0,0))
            fuente = pygame.font.Font('MAGNETOB.TTF', 18)
            texto_total = fuente.render("TOTAL DE USUARIOS: "+str(j), 1, (255,255,255))
            screen.blit(texto_total, (25, 10))
            fuente = pygame.font.Font('MAGNETOB.TTF', 18)
            texto_turno = fuente.render("USUARIO ACTUAL: "+str(t), 1, (255,255,255))
            screen.blit(texto_turno, (25, 40))
            crear_image = util.cargar_imagen('imagenes/btncrear.png');
            resetear_image = util.cargar_imagen('imagenes/btnresetear.png');
            usu1_image = util.cargar_imagen('imagenes/1.png');
            usu2_image = util.cargar_imagen('imagenes/2.png');
            usu3_image = util.cargar_imagen('imagenes/3.png');
            usu4_image = util.cargar_imagen('imagenes/4.png');
            usu5_image = util.cargar_imagen('imagenes/5.png');


            if event.type == MOUSEBUTTONUP:
                if screen.blit(usu1_image, (50,70)).collidepoint(mousex, mousey):
                    t=1
                if screen.blit(usu2_image, (160,70)).collidepoint(mousex, mousey):
                    t=2
                if screen.blit(usu3_image, (270,70)).collidepoint(mousex, mousey):
                    t=3
                if screen.blit(usu4_image, (380,70)).collidepoint(mousex, mousey):
                    t=4
                if screen.blit(usu5_image, (490,70)).collidepoint(mousex, mousey):
                    t=5

               
            if event.type == MOUSEBUTTONUP:
                if screen.blit(crear_image, (20,120)).collidepoint(mousex, mousey):
                    z=1

            if event.type == MOUSEBUTTONUP:
                if screen.blit(resetear_image, (330,120)).collidepoint(mousex, mousey):
                    z=2
                   

            if t == 1 and z == 1:
                if usuario1 == 0:
                    rombouno = pool.getRombo()
                    rombouno.image = util.cargar_imagen('imagenes/rombo1.png')
                    rombouno.rect = rombouno.image.get_rect()
                    rombouno.rect.move_ip(x[i],y[i])
                    screen.blit(rombouno.image, rombouno.rect)
                    i=i+1
                    z=0
                    usuario1 = 1
                    
            if t == 1 and z == 2:          
                if usuario1 == 1:                   
                    pool.renovarRombo(rombouno)
                    usuario1 = 0
                    i=i-1
                    z=0
                    
            if t == 2 and z == 1:
                if usuario2 == 0:
                    rombodos = pool.getRombo()
                    rombodos.image = util.cargar_imagen('imagenes/rombo2.png')
                    rombodos.rect = rombodos.image.get_rect()
                    rombodos.rect.move_ip(x[i],y[i])
                    screen.blit(rombodos.image, rombodos.rect)
                    usuario2 = 1
                    i=i+1
                    z=0
                    
            if t == 2 and z == 2:          
                if usuario2 == 1:                   
                    pool.renovarRombo(rombodos)
                    usuario2 = 0
                    i=i-1
                    z=0


            if t == 3 and z == 1:
                if usuario3 == 0:
                    rombotres = pool.getRombo()
                    rombotres.image = util.cargar_imagen('imagenes/rombo3.png')
                    rombotres.rect = rombotres.image.get_rect()
                    rombotres.rect.move_ip(x[i],y[i])
                    screen.blit(rombotres.image, rombotres.rect)
                    usuario3 = 1
                    i=i+1
                    z=0
                    
            if t == 3 and z == 2:          
                if usuario3 == 1:                   
                    pool.renovarRombo(rombotres)
                    usuario3 = 0
                    i=i-1
                    z=0


            if t == 4 and z == 1:
                if usuario4 == 0:
                    rombocuat = pool.getRombo()
                    rombocuat.image = util.cargar_imagen('imagenes/rombo4.png')
                    rombocuat.rect = rombocuat.image.get_rect()
                    rombocuat.rect.move_ip(x[i],y[i])
                    screen.blit(rombocuat.image, rombocuat.rect)
                    usuario4 = 1
                    i=i+1
                    z=0
                    
            if t == 4 and z == 2:          
                if usuario4 == 1:                   
                    pool.renovarRombo(rombocuat)
                    usuario2 = 0
                    i=i-1
                    z=0

            if t == 5 and z == 1:
                if usuario5 == 0:
                    rombocinco = pool.getRombo()
                    rombocinco.image = util.cargar_imagen('imagenes/rombo5.png')
                    rombocinco.rect = rombocinco.image.get_rect()
                    rombocinco.rect.move_ip(x[i],y[i])
                    screen.blit(rombocinco.image, rombocinco.rect)
                    usuario5 = 1
                    i=i+1
                    z=0
                    
            if t == 5 and z == 2:          
                if usuario5 == 1:                   
                    pool.renovarRombo(rombocinco)
                    usuario5 = 0
                    i=i-1
                    z=0
            
            #if teclas[K_1]:
             #   t=1
   #         if teclas[K_2]:
    #            t=2
      #      if teclas[K_3]:
     #           t=3
       #     if teclas[K_4]:
        #        t=4
     #       if teclas[K_5]:
    #            t=5
    #        if t == 1:
    #            if usuario1 == 0:
    #                if teclas[K_c]:
    #                    rombo = Rombo((200,200),0)
    #                    rombouno = pool.getRombo()
    #                    rombouno.image = util.cargar_imagen('imagenes/rombo1.png')
   #                     rombouno.rect = rombouno.image.get_rect()
    #                    rombouno.rect.move_ip(x[i],y[i])
    #                    screen.blit(rombouno.image, rombouno.rect)
    #                    usuario1 = 1
    #                    i=i+1
     #                   screen.blit(rombo.image, rombo.rect)
     #                   
    #            if usuario1 == 1:
    #                if teclas[K_r]:
    #                    pool.renovarRombo(rombouno)
    #                    usuario1 = 0
   #                    rombouno = None
   #                     i=i-1

                        
    #        if t == 2:
    #            if usuario2 == 0:
    #                if teclas[K_c]:
   #                     rombodos = pool.getRombo()
    #                    rombodos.image = util.cargar_imagen('imagenes/rombo1.png')
    #                    rombodos.rect = rombodos.image.get_rect()
    #                    rombodos.rect.move_ip(x[i],y[i])
    #                    screen.blit(rombodos.image, rombodos.rect)
    #                    usuario2 = 1
     #                   i=i+1
                        
     #           if usuario2 == 1:
      #              if teclas[K_r]:
       #                 pool.renovarRombo(rombodos)
        #                usuario2 = 0
         #               rombodos = None
          #              i=i-1

                        
 #           if t == 3:
  #              if usuario3 == 0:
   #                 if teclas[K_c]:
    #                    rombotres = pool.getRombo()
     #                   rombotres.image = util.cargar_imagen('imagenes/rombo1.png')
      #                  rombotres.rect = rombotres.image.get_rect()
       #                 rombotres.rect.move_ip(x[i],y[i])
        #                screen.blit(rombotres.image, rombotres.rect)
         #               usuario3 = 1
          #              i=i+1
                        
 #               if usuario3 == 1:
  #                  if teclas[K_r]:
   #                     pool.renovarRombo(rombotres)
    #                    usuario3 = 0
     #                   rombotres = None
      #                  i=i-1

                        
#            if t == 4:
 #               if usuario4 == 0:
  #                  if teclas[K_c]:
   #                     rombocuat = pool.getRombo()
    #                    rombocuat.image = util.cargar_imagen('imagenes/rombo1.png')
     #                   rombocuat.rect = rombocuat.image.get_rect()
      #                  rombocuat.rect.move_ip(x[i],y[i])
       #                 screen.blit(rombocuat.image, rombocuat.rect)
        #                usuario4 = 1
         #               i=i+1
                        
  #              if usuario4 == 1:
   #                 if teclas[K_r]:
    #                    pool.renovarRombo(rombocuat)
     #                   usuario4 = 0
      #                  rombocuat = None
       #                 i=i-1

                        
 #           if t == 5:
  #              if usuario1 == 0:
   #                 if teclas[K_c]:
    #                    rombocinco = pool.getRombo()
     #                   rombocinco.image = util.cargar_imagen('imagenes/rombo1.png')
      #                  rombocinco.rect = rombocinco.image.get_rect()
       #                 rombocinco.rect.move_ip(x[i],y[i])
        #                screen.blit(rombocinco.image, rombocinco.rect)
         #               usuario5 = 1
          #              i=i+1
                        
#                if usuario1 == 1:
 #                   if teclas[K_r]:
  #                      pool.renovarRombo(rombocinco)
   #                     usuario5 = 0
    #                    rombocinco = None
     #                   i=i-1

                
            screen.blit(rombouno.image, rombouno.rect)
            screen.blit(rombodos.image, rombodos.rect)
            screen.blit(rombotres.image, rombotres.rect)                
            screen.blit(rombocuat.image, rombocuat.rect)
            screen.blit(rombocinco.image, rombocinco.rect)
            screen.blit(usu1_image, (50,70))
            screen.blit(usu2_image, (160,70))
            screen.blit(usu3_image, (270,70))
            screen.blit(usu4_image, (380,70))
            screen.blit(usu5_image, (490,70))
            screen.blit(crear_image, (20,120))
            screen.blit(resetear_image, (330,120))
        pygame.display.update()
        pygame.time.delay(10)
        
if __name__ == '__main__':
    game()
