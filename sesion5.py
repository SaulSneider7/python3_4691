import pygame

class Game:
    screen = None
    aliens = []
    rockets = []
    lost = False

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False

        hero = Hero(self, width / 2, height - 20 )
        generator = Generator(self)
        rocket = None

        while not done:
            if len(self.aliens) == 44:
                self.displayText("YOU WIN!")
            
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                hero.x -= 2 if hero.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                hero.x += 2 if hero.x < width - 20 else 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(Rocket(self, hero.x, hero.y))
            
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for alien in self.aliens:
                alien.draw()
            for rocket in self.rockets:
                rocket.draw()

            if not self.lost:
                hero.draw()
    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (255, 255, 255))
        self.screen.blit(textsurface, (100, 100))

class Alien:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y 
        self.size = 30