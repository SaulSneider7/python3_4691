import pygame


"""
CREAMOS LA CLASE GAME
"""
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



"""
CREAMOS LA CLASE ALIEN
"""
class Alien:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y 
        self.size = 30

    def draw(self):
        pygame.draw.rect(self.game.screen, (81, 43, 88), pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += 0.05

    def checkCollision(self, game):
        for rocket in game.rockets:
            if( rocket.x < self.x + self.size and rocket.x > self.x - self.size and rocket.y < self.y + self.size and rocket.y > self.y - self.size):
                game.rockets.remove(rocket)
                game.aliens.remove(self)

"""
CREAMOS LA CLASE HERO
"""
class Hero:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
    
    def draw(self):
        pygame.draw.rect(self.game.screen,(210, 250, 251),pygame.Rect(self.x, self.y, 8, 5))

"""
CREAMOS LA CLASE GENERATOR
"""
class Generator:
    def __init__(self, game):
        margin = 30
        width = 50
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y))

"""
CREAMOS LA CLASE ROCKET
"""
class Rocket:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
    
    def draw(self):
        pygame.draw.rect(self.game.screen,(254, 52, 110), pygame.Rect(self.x , self.y, 2, 4))
        self.y -= 2

if __name__ == "__main__":
    game = Game(600, 400)