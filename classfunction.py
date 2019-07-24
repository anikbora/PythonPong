import sys,pygame
import random
import time
pygame.init() #initilize pygame
#screen

display_width = 1980
display_height = 1080
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
colorR = random.randint(0, 255)
colorG = random.randint(0, 255)
colorB = random.randint(0, 255)
colorCounter=0

points1, points2 = 0, 0
class Ball():
    def __init__(self):
        self.ball = pygame.image.load('ball.png')
        self.ball = pygame.transform.scale(self.ball, (15,15))
        self.ball_rect = self.ball.get_rect()
        self.ball_rect = self.ball_rect.move((display_width/2,display_height/2))
        self.x = 1
        self.y = 1
        self.xMovement = random.randint(5, 10)
        self.yMovement = random.randint(5, 10)


    def place(self):
        screen.blit(self.ball,self.ball_rect)

    def move(self, paddle1, paddle2):
        global points1, points2
        c1 = paddle1.bottomleft
        c2 = paddle1.topright
        c3 = paddle2.bottomleft
        c4 = paddle2.topright
        x1,y1,x2,y2 = c1[0], c2[1], c2[0], c1[1]
        a1,b1,a2,b2 = c3[0], c4[1], c4[0], c3[1]
        print(a1, b1, a2, b2)
        print(self.ball_rect.center)
        screen.fill((0, 0, 0),self.ball_rect)
        if (x1<=self.ball_rect.center[0]<=x2 and y1 <= self.ball_rect.center[1] <= y2) or (a1<=self.ball_rect.center[0]<=a2 and b1<=self.ball_rect.center[1]<=b2) :
            self.x = -self.x
            self.xMovement+=2
            print("adas")
        if self.ball_rect.top <= 0 or self.ball_rect.bottom >= 1080:
            self.y = -self.y
            self.yMovement+=2

        if self.ball_rect.center[0] <= 0 or self.ball_rect.center[0] >= 1980:
            if self.ball_rect.center[0] <= 0:
                points2 += 1
            else:
                points1 += 1
            self.ball_rect = self.ball_rect.move((990 - self.ball_rect.center[0], 540 - self.ball_rect.center[1]))
            self.xMovement = random.randint(5, 20)
            self.yMovement = random.randint(5, 20)
            time.sleep(1)


        self.ball_rect = self.ball_rect.move(self.x * self.xMovement, self.y * self.yMovement)
        pygame.time.delay(10)


        Ball.place(self)
        pygame.display.update()

class Paddle():
    def __init__(self,position):
        self.position = position
        self.paddle_image = pygame.image.load("paddle.png")
        self.paddle_image=pygame.transform.scale(self.paddle_image, (20,100))
        self.paddle_rect = self.paddle_image.get_rect()
        self.paddle_rect = self.paddle_rect.move(position)

    def place(self):
        screen.blit(self.paddle_image, self.paddle_rect)
        pygame.display.update()
    def move(self,direction):
        if direction=='up':
            if self.paddle_rect.top>=0:
                screen.fill((0,0,0),self.paddle_rect)
                self.paddle_rect = self.paddle_rect.move(0,-20)
                Paddle.place(self)
                pygame.display.update()
        if direction=='down':
            if self.paddle_rect.bottom<=1080:
                screen.fill((0,0,0),self.paddle_rect)
                self.paddle_rect = self.paddle_rect.move(0,20)
                Paddle.place(self)
                pygame.display.update()

class text:

    def __init__(self, size, x, y, value):
        self.size = size
        self.x  = x
        self.y = y
        self.value = value

    def draw(self):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', self.size)
        textsurface = myfont.render(self.value, False, (255, 255, 255))
        screen.blit(textsurface, (self.x, self.y))


def keyboardReturn():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if event.key == pygame.K_RETURN:
                sys.exit()
            if keys[pygame.K_UP]:
                return True
def startScreen():
    while not keyboardReturn() == True :
        screen.fill((255,100,255))
        title = text(200,500,0,'Pong')
        title.draw()
        pygame.display.update()


def game():
    theball = Ball()

    theball.place()
    paddle1 = Paddle((10,500))
    paddle2 = Paddle((1880,500))
    pygame.key.set_repeat(1)
    while 1:
        textSize=100
        paddle1.place()
        paddle2.place()
        score1 = text(textSize, display_width/10, display_height/10, str(points1))
        score2 = text(textSize, display_width - display_width/10, display_height/10, str(points2))
        screen.fill((0,0,0), (display_width/10, display_height - display_height/10, display_width - display_width/10+textSize, display_height- display_height/10 + textSize))
        screen.fill((0,0,0), (display_width/10,display_height/10, display_width - display_width/10+textSize,display_height/10 + textSize))

        score1.draw()
        score2.draw()



        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_RETURN:
                    sys.exit()
                if keys[pygame.K_UP]:
                     paddle2.move("up")
                if keys[pygame.K_DOWN]:
                    paddle2.move("down")
                if keys[pygame.K_w]:
                    paddle1.move('up')
                if keys[pygame.K_s]:
                    paddle1.move('down')
        theball.move(paddle1.paddle_rect, paddle2.paddle_rect)