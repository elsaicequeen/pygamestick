import pygame

pygame.init()

playspace = pygame.display.set_mode((500, 500))

pygame.display.set_caption("sidescroller 01")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png')]
background = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, playspace):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0

        if self.left:
            playspace.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            playspace.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            playspace.blit(char, (self.x, self.y))


def drawplayspace():
    playspace.blit(background, (0, 0))
    character.draw(playspace)

    pygame.display.update()


# mainloop
character = player(200, 200, 64, 64)
run = True
while run:
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and character.x > character.vel:
        character.x -= character.vel
        character.left = True
        character.right = False
    elif keys[pygame.K_RIGHT] and character.x < 500 - character.width - character.vel:
        character.x += character.vel
        character.right = True
        character.left = False
    else:
        character.right = False
        character.left = False
        character.walkCount = 0

    if not (character.isJump):
        if keys[pygame.K_SPACE]:
            character.isJump = True
            character.right = False
            character.left = False
            character.walkCount = 0
    else:
        if character.jumpCount >= -10:
            neg = 1
            if character.jumpCount < 0:
                neg = -1
            character.y -= (character.jumpCount ** 2) * 0.5 * neg
            character.jumpCount -= 1
        else:
            character.isJump = False
            character.jumpCount = 10

    drawplayspace()

pygame.quit()
