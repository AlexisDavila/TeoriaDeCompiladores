"""
Objeto Sprite para el motor 2D
Representa un sprite con física básica
"""

import pygame


class SpriteObject:
    """Clase que representa un sprite en el motor 2D"""
    
    def __init__(self, name, x, y, width=50, height=50):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # Física
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.8
        self.on_ground = False
        self.base_speed = 5
        
        # Estado
        self.is_running = False
        self.is_crouching = False
        self.is_jumping = False
        self.current_animation = "idle"
        
        # Animaciones (colores por defecto)
        self.animations = {
            "idle": (100, 150, 255),      # Azul claro
            "running": (255, 200, 100),   # Naranja
            "jumping": (150, 255, 150),   # Verde claro
            "crouching": (200, 100, 200)  # Púrpura
        }
        
        self.current_color = self.animations["idle"]
    
    def update(self, world_height):
        """Actualiza la posición y física del sprite"""
        # Aplicar gravedad
        if not self.on_ground:
            self.velocity_y += self.gravity
        
        # Actualizar posición
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Colisión con el suelo
        ground_level = world_height - self.height - 10
        if self.y >= ground_level:
            self.y = ground_level
            self.velocity_y = 0
            self.on_ground = True
            self.is_jumping = False
        else:
            self.on_ground = False
        
        # Fricción
        self.velocity_x *= 0.85
    
    def render(self, screen):
        """Dibuja el sprite en pantalla"""
        # Determinar color según animación
        self.current_color = self.animations.get(self.current_animation, 
                                                  self.animations["idle"])
        
        # Ajustar altura si está agachado
        height = self.height // 2 if self.is_crouching else self.height
        y_pos = self.y + (self.height - height)
        
        # Dibujar rectángulo
        rect = pygame.Rect(self.x, y_pos, self.width, height)
        pygame.draw.rect(screen, self.current_color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)  # Borde negro
        
        # Dibujar nombre
        font = pygame.font.Font(None, 24)
        text = font.render(self.name, True, (255, 255, 255))
        screen.blit(text, (self.x, self.y - 20))
    
    def move(self, dx, dy):
        """Mueve el sprite"""
        self.velocity_x = dx
        self.velocity_y = dy
    
    def jump(self):
        """Hace que el sprite salte"""
        if self.on_ground:
            self.velocity_y = -15
            self.is_jumping = True
            self.current_animation = "jumping"
    
    def run(self, speed):
        """Hace que el sprite corra"""
        self.velocity_x = speed
        self.is_running = True
        self.current_animation = "running"
    
    def crouch(self):
        """Hace que el sprite se agache"""
        self.is_crouching = True
        self.current_animation = "crouching"
    
    def stop(self):
        """Detiene el sprite"""
        self.velocity_x = 0
        self.is_running = False
        self.is_crouching = False
        self.current_animation = "idle"
    
    def set_animation(self, anim_name):
        """Cambia la animación del sprite"""
        if anim_name in self.animations:
            self.current_animation = anim_name
        else:
            print(f"⚠ Animación '{anim_name}' no existe")
