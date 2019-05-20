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
    charecter.draw(playspace)

    pygame.display.update()


# mainloop
charecter = player(200, 200, 64, 64)
run = True
while run:
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and charecter.x > charecter.vel:
        charecter.x -= charecter.vel
        charecter.left = True
        charecter.right = False
    elif keys[pygame.K_RIGHT] and charecter.x < 500 - charecter.width - charecter.vel:
        charecter.x += charecter.vel
        charecter.right = True
        charecter.left = False
    else:
        charecter.right = False
        charecter.left = False
        charecter.walkCount = 0

    if not (charecter.isJump):
        if keys[pygame.K_SPACE]:
            charecter.isJump = True
            charecter.right = False
            charecter.left = False
            charecter.walkCount = 0
    else:
        if charecter.jumpCount >= -10:
            neg = 1
            if charecter.jumpCount < 0:
                neg = -1
            charecter.y -= (charecter.jumpCount ** 2) * 0.5 * neg
            charecter.jumpCount -= 1
        else:
            charecter.isJump = False
            charecter.jumpCount = 10

    drawplayspace()

pygame.quit()