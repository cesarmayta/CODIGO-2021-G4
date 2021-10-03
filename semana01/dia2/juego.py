import sys    # para usar exit()
import pygame

ANCHO = 640 # Ancho de la pantalla.
ALTO = 480  # Alto de la pantalla.
color_azul = (0, 0, 64)  # Color azul para el fondo.

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('imagenes/pelota.png')
        # Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posición inicial centrada en pantalla.
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        # Establecer velocidad inicial.
        self.speed = [5, 5]

    def update(self):
        # Evitar que salga por debajo.
        if self.rect.bottom >= ALTO or self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        # Evitar que salga por la derecha.
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        # Mover en base a posición actual y velocidad.
        self.rect.move_ip(self.speed)

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('imagenes/jugador.png')
        # Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posición inicial centrada en pantalla en X.
        self.rect.midbottom = (ANCHO / 2, ALTO - 20)
        # Establecer velocidad inicial.
        self.speed = [0, 0]

    def update(self, evento):
        # Buscar si se presionó flecha izquierda.
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5, 0]
        # Si se presionó flecha derecha.
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5, 0]
        else:
            self.speed = [0, 0]
        # Mover en base a posición actual y velocidad.
        self.rect.move_ip(self.speed)

class Pc(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('imagenes/jugador.png')
        # Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posición inicial centrada en pantalla en X.
        self.rect.midbottom = (ANCHO / 2, ALTO - 450)
        # Establecer velocidad inicial.
        self.speed = [9,0]

    def update(self):
        # Evitar que salga por debajo.
        if self.rect.bottom >= ALTO or self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        # Evitar que salga por la derecha.
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        # Mover en base a posición actual y velocidad.
        self.rect.move_ip(self.speed)




# Inicializando pantalla.
pantalla = pygame.display.set_mode((ANCHO, ALTO))
# Configurar título de pantalla.
pygame.display.set_caption('Ping Pong')
# Crear el reloj.
reloj = pygame.time.Clock()
# Ajustar repetición de evento de tecla presionada.
pygame.key.set_repeat(30)

bolita = Pelota()
jugador = Jugador()
pc = Pc()

while True:
    # Establecer FPS.
    reloj.tick(60)

    # Revisar todos los eventos.
    for evento in pygame.event.get():
        # Si se presiona la tachita de la barra de título,
        if evento.type == pygame.QUIT:
            # cerrar el videojuego.
            sys.exit()
        # Buscar eventos del teclado,
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)

    # Actualizar posición de la bolita.
    bolita.update()
    pc.update()

    # Colisión entre bolita y jugador.
    if pygame.sprite.collide_rect(bolita, jugador):
        bolita.speed[1] = -bolita.speed[1]

    # Colisión entre bolita y pc.
    if pygame.sprite.collide_rect(bolita, pc):
        bolita.speed[1] = -bolita.speed[1]


    # Rellenar la pantalla.
    pantalla.fill(color_azul)
    # Dibujar bolita en pantalla.
    pantalla.blit(bolita.image, bolita.rect)
    # Dibujar jugador en pantalla.
    pantalla.blit(jugador.image, jugador.rect)

    pantalla.blit(pc.image, pc.rect)
    # Dibujar los ladrillos.
    # Actualizar los elementos en pantalla.
    pygame.display.flip()
