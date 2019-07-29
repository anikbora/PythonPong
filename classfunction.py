import sys,pygame
import random
import time
pygame.init() #initilize pygame
x = input('ai or no ai')
display_width = 1980
display_height = 1080
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

location=[0]

points1, points2 = 0, 0
class Ball():
    def __init__(self, speed=1):
        self.ball = pygame.image.load('ball.png')
        self.ball = pygame.transform.scale(self.ball, (15,15))
        self.ball_rect = self.ball.get_rect()
        self.ball_rect = self.ball_rect.move((display_width/2,display_height/2))
        self.direction_x = 1
        self.direction_y = 1
        self.speed=speed
        self.xMovement = random.randint(5, 10) * speed
        self.yMovement = random.randint(5, 10) * speed

    def place(self):
        screen.blit(self.ball,self.ball_rect)

    def move(self, paddle1, paddle2):
        global points1, points2, location
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
            self.direction_x = -self.direction_x
            print("adas")
        if self.ball_rect.top <= 0 or self.ball_rect.bottom >= display_height:
            self.direction_y = -self.direction_y
            self.yMovement+=2

        if self.ball_rect.center[0] <= 0 or self.ball_rect.center[0] >= display_width:
            if self.ball_rect.center[0] <= 0:
                points2 += 1
            else:
                points1 += 1

            return True


        self.ball_rect = self.ball_rect.move(self.direction_x * self.xMovement, self.direction_y * self.yMovement)
        pygame.time.delay(10)
        Ball.place(self)
        pygame.display.update()
        return False
    def reset(self):
        self.ball_rect = self.ball_rect.move((990 - self.ball_rect.center[0], 540 - self.ball_rect.center[1]))
        self.xMovement = random.randint(5, 20)
        self.yMovement = random.randint(5, 20)
        self.direction_x=1
        self.direction_y=1
        screen.fill((0,0,0))
        time.sleep(1)
class FastBall(Ball):
    def __init__(self,xMovement,yMovement, speed=1):
        Ball.__init__(self, speed)
        self.xMovement=xMovement*speed
        self.yMovement=yMovement*speed

    def move(self, paddle1, paddle2):
        global points1, points2, location
        c1 = paddle1.bottomleft
        c2 = paddle1.topright
        c3 = paddle2.bottomleft
        c4 = paddle2.topright
        x1, y1, x2, y2 = c1[0], c2[1], c2[0], c1[1]
        a1, b1, a2, b2 = c3[0], c4[1], c4[0], c3[1]
        print(a1, b1, a2, b2)
        print(self.ball_rect.center)
        screen.fill((0, 0, 0), self.ball_rect)
        if self.ball_rect.center[0] <= 30:
            location[0]=(self.ball_rect.center[1])
            self.direction_x = -self.direction_x
        if self.ball_rect.center[0] >= 1880:
            self.direction_x = -self.direction_x
        if self.ball_rect.top <= 0 or self.ball_rect.bottom >= display_height:
            self.direction_y = -self.direction_y
            self.yMovement+=2*self.speed

        self.ball_rect = self.ball_rect.move(self.direction_x * self.xMovement, self.direction_y * self.yMovement)
        pygame.time.delay(10)


        Ball.place(self)
        screen.fill((0,0,0),self.ball_rect)
        pygame.display.update()
    def reset(self,xMovement,yMovement):
        Ball.reset(self)

        self.xMovement=xMovement*self.speed
        self.yMovement=yMovement*self.speed




class Paddle():
    def __init__(self,position):
        self.position = position
        self.paddle_image = pygame.image.load("paddle.png")
        self.paddle_image=pygame.transform.scale(self.paddle_image, (20,100))
        self.paddle_rect = self.paddle_image.get_rect()
        self.paddle_rect = self.paddle_rect.move(position)
        self.listnumber = 0

    def place(self):
        screen.blit(self.paddle_image, self.paddle_rect)
        pygame.display.update()
    def move(self,direction,ai=False):
            if direction=='up':
                if self.paddle_rect.top>=0:
                    screen.fill((0,0,0),self.paddle_rect)
                    self.paddle_rect = self.paddle_rect.move(0,-20)
                    Paddle.place(self)
                    pygame.display.update()
            if direction=='down':
                if self.paddle_rect.bottom<=display_height:
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
                return 'up'





def startScreen():
    while not keyboardReturn() == 'up':
        screen.fill((255,100,255))
        title = text(200,500,0,'Pong')
        title.draw()
        pygame.display.update()



def game(aiOrnot):
    theball = Ball()
    pball = FastBall(theball.xMovement,theball.yMovement,2)
    pball.place()
    listnumber=0
    theball.place()
    paddle1 = Paddle((10,500))
    paddle2 = Paddle((1880,500))
    pygame.key.set_repeat(1)
    while 1:
        global location
        textSize=100
        paddle1.place()
        paddle2.place()
        score1 = text(textSize, display_width/10, display_height/10, str(points1))
        score2 = text(textSize, display_width - display_width/10, display_height/10, str(points2))
        screen.fill((0,0,0), (display_width/10, display_height - display_height/10, display_width - display_width/10+textSize, display_height- display_height/10 + textSize))
        screen.fill((0,0,0), (display_width/10,display_height/10, display_width - display_width/10+textSize,display_height/10 + textSize))

        score1.draw()
        score2.draw()
        print(location)


        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_RETURN:
                    sys.exit()
                if keys[pygame.K_UP]:
                    paddle2.move("up")
                elif keys[pygame.K_DOWN]:
                    paddle2.move("down")
                elif keys[pygame.K_w]:
                    paddle1.move('up')
                elif keys[pygame.K_s]:
                    paddle1.move('down')
        print(listnumber)
        print('this is list numbet')
        if aiOrnot == 'ai':
            if len(location)>0 and len(location)>=listnumber:
                if location[0]>paddle1.paddle_rect.center[1]:
                    paddle1.move('down')
                elif location[0]<paddle1.paddle_rect.center[1]:
                    paddle1.move('up')
                if theball.ball_rect.center[0] <= 20:
                    print('hi')
                    location=[]
                if not len(location)>=listnumber+1:
                    listnumber+=1
                    print(listnumber)
                    print('this is listnumber')


        if theball.move(paddle1.paddle_rect, paddle2.paddle_rect):
            theball.reset()
            pball.reset(theball.xMovement,theball.yMovement)
        pball.move(paddle1.paddle_rect, paddle2.paddle_rect)
