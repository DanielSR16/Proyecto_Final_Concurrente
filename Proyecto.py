import pygame,sys, threading
from pygame.locals import *
import random

def carrito(x,y, color, pantalla,bandera,spedd_x,spedd_y):
    #velocidad a mover el cuadrado 

    

    #logica
    if(x < 800 and bandera == False):
        x += spedd_x
    if(x > 800):       
        y += spedd_y
        
    if(y > 900):
        spedd_x = spedd_x * -1
        x += spedd_x
        bandera = True
        
    if(x < 220 and bandera == True):
        spedd_y = spedd_y * -1
        y += spedd_y
        
    if(x < 300 and y == 300):
        bandera = False
        
    # print('parada: ',x,' , ',y,'bandera xd: ',bandera)    
    
    pygame.draw.circle(pantalla,color,(x,y),50)
    return x,y,bandera
    
def dibujar():
    #colores
    BLACK = (0,0,0)
    white = (255,255,255)
    green = (0,255,0)
    red = (255,0,0)
    blue = (0,0,255)

    pygame.init()

    pantalla = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption('Mi primer juego')
    #controlar FPS
    clock = pygame.time.Clock()

    #cordenadas del cuadro
    cordenada_x = 220
    cordenada_y = 300
    cordenada_x2 = 240
    cordenada_y2 = 300
    cordenada_x3 = 245
    cordenada_y3 = 300
    
    bandera =  False
    bandera2 =  False
    bandera3 =  False
    
    velocidad = random.choice([6,9,12])
    velocidad2 = random.choice([6,9,12])
    velocidad3 = random.choice([6,9,12])
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
       
       
     
        #color de fondo
        pantalla.fill(white)
        
        # ------- zona de dibujo
        pygame.draw.rect(pantalla,BLACK,(200,300,600,600),30,1)
        cordenada_x,cordenada_y,bandera = carrito(cordenada_x, cordenada_y, red , pantalla,bandera,velocidad,velocidad)
        cordenada_x2,cordenada_y2,bandera2 = carrito(cordenada_x2, cordenada_y2, green , pantalla,bandera2,velocidad2,velocidad2)
        cordenada_x3,cordenada_y3,bandera3 = carrito(cordenada_x3, cordenada_y3, blue , pantalla,bandera3,velocidad3,velocidad3)
        
        # ------- zona de dibujo
  
        #actualizar pantalla
        pygame.display.flip()
        clock.tick(60)

dibujar() 