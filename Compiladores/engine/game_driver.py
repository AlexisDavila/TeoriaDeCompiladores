"""
Game Driver - Motor 2D con Pygame
Gestiona el juego y ejecuta comandos del intérprete
"""

import pygame
import sys
from engine.sprite_object import SpriteObject


class GameDriver:
    """Driver del juego que gestiona sprites y renderizado"""
    
    def __init__(self, width=800, height=600, title="Mini2DLang Engine"):
        # Inicializar Pygame
        pygame.init()
        
        # Configuración de ventana
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        
        # Reloj para controlar FPS
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        # Sprites
        self.sprites = {}
        
        # Configuración del mundo
        self.gravity = 0.8
        self.player_speed = 5
        
        # Estado del juego
        self.running = True
        
        # Cola de comandos pendientes
        self.command_queue = []
        
        print(f"✓ Motor 2D inicializado: {width}x{height}")
    
    def load_sprite(self, name, x, y):
        """Carga un sprite en el motor"""
        if name in self.sprites:
            print(f"⚠ Sprite '{name}' ya existe, se reemplazará")
        
        sprite = SpriteObject(name, x, y)
        sprite.gravity = self.gravity
        self.sprites[name] = sprite
        print(f"  ✓ Sprite '{name}' cargado en ({x}, {y})")
    
    def execute_action(self, sprite_name, action, *args):
        """Ejecuta una acción sobre un sprite"""
        if sprite_name not in self.sprites:
            print(f"✗ Error: Sprite '{sprite_name}' no existe")
            return
        
        sprite = self.sprites[sprite_name]
        
        if action == 'move':
            sprite.move(args[0], args[1])
        elif action == 'jump':
            sprite.jump()
        elif action == 'run':
            sprite.run(args[0])
        elif action == 'crouch':
            sprite.crouch()
        elif action == 'stop':
            sprite.stop()
        elif action == 'set_animation':
            sprite.set_animation(args[0])
    
    def set_gravity(self, value):
        """Configura la gravedad global"""
        self.gravity = value
        for sprite in self.sprites.values():
            sprite.gravity = value
    
    def set_world_width(self, value):
        """Configura el ancho del mundo"""
        self.width = int(value)
    
    def set_world_height(self, value):
        """Configura la altura del mundo"""
        self.height = int(value)
    
    def set_player_speed(self, value):
        """Configura la velocidad del jugador"""
        self.player_speed = value
    
    def update(self):
        """Actualiza el estado de todos los sprites"""
        for sprite in self.sprites.values():
            sprite.update(self.height)
    
    def render(self):
        """Renderiza todos los sprites"""
        # Fondo
        self.screen.fill((50, 50, 80))  # Azul oscuro
        
        # Dibujar suelo
        ground_y = self.height - 10
        pygame.draw.line(self.screen, (100, 100, 100), 
                        (0, ground_y), (self.width, ground_y), 5)
        
        # Renderizar sprites
        for sprite in self.sprites.values():
            sprite.render(self.screen)
        
        # Información en pantalla
        self._draw_info()
        
        # Actualizar pantalla
        pygame.display.flip()
    
    def _draw_info(self):
        """Dibuja información del juego"""
        font = pygame.font.Font(None, 28)
        
        # Título
        title = font.render("Mini2DLang Engine", True, (255, 255, 255))
        self.screen.blit(title, (10, 10))
        
        # Información de sprites
        y_offset = 40
        for name, sprite in self.sprites.items():
            info = f"{name}: ({int(sprite.x)}, {int(sprite.y)}) | {sprite.current_animation}"
            text = font.render(info, True, (200, 200, 200))
            self.screen.blit(text, (10, y_offset))
            y_offset += 25
        
        # Instrucciones
        instructions = [
            "ESC: Salir",
            "SPACE: Pausar"
        ]
        
        y_offset = self.height - 60
        small_font = pygame.font.Font(None, 20)
        for instruction in instructions:
            text = small_font.render(instruction, True, (150, 150, 150))
            self.screen.blit(text, (10, y_offset))
            y_offset += 20
    
    def handle_events(self):
        """Maneja eventos de Pygame"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def run(self, duration_seconds=10):
        """Ejecuta el game loop por un tiempo determinado"""
        print(f"\n=== Ejecutando motor 2D por {duration_seconds} segundos ===")
        
        frames = 0
        max_frames = duration_seconds * self.fps
        
        while self.running and frames < max_frames:
            # Eventos
            self.handle_events()
            
            # Actualizar
            self.update()
            
            # Renderizar
            self.render()
            
            # Control de FPS
            self.clock.tick(self.fps)
            frames += 1
        
        print(f"=== Motor 2D finalizado ({frames} frames) ===\n")
        self.quit()
    
    def quit(self):
        """Cierra el motor"""
        pygame.quit()
