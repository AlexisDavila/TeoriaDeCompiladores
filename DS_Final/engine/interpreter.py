import pygame
import time

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Mini Lenguaje - Demo Game")
        self.clock = pygame.time.Clock()
        self.player = pygame.Rect(280, 300, 40, 40)
        self.color = (0, 128, 255)
        self.running = True

    def draw(self):
        self.screen.fill((30, 30, 30))
        pygame.draw.rect(self.screen, self.color, self.player)
        pygame.display.flip()

    def move(self, direction, steps):
        dx, dy = 0, 0
        step_size = 10

        if direction == "right":
            dx = step_size
        elif direction == "left":
            dx = -step_size
        elif direction == "up":
            dy = -step_size
        elif direction == "down":
            dy = step_size

        for _ in range(steps):
            self.player.move_ip(dx, dy)
            self.update()
            time.sleep(0.1)

    def jump(self):
        original_y = self.player.y
        for _ in range(5):
            self.player.y -= 10
            self.update()
            time.sleep(0.05)
        for _ in range(5):
            self.player.y += 10
            self.update()
            time.sleep(0.05)
        self.player.y = original_y

    def attack(self, target):
        print(f"⚔️ Atacando a {target}")
        self.color = (255, 0, 0)
        self.update()
        time.sleep(0.3)
        self.color = (0, 128, 255)
        self.update()

    def wait(self, seconds):
        print(f"⏳ Esperando {seconds} segundos...")
        start = time.time()
        while time.time() - start < seconds:
            self.update()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.draw()
        self.clock.tick(30)
