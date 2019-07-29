class Ball():
    def __init__(self, speed=1, xmove=1, ymove=1):
        self.ball = pygame.image.load('ball.png')
        self.ball = pygame.transform.scale(self.ball, (15,15))
        self.ball_rect = self.ball.get_rect()
        self.ball_rect = self.ball_rect.move((display_width/2,display_height/2))
        self.direction_x = 1
        self.direction_y = 1
        self.speed=speed
        if xmove==1 and ymove==1:
            self.xMovement = random.randint(5, 10) * speed
            self.yMovement = random.randint(5, 10) * speed
        else:
            self.xMovement = xmove * speed
            self.yMovement = ymove * speed




    def place(self):
        screen.blit(self.ball,self.ball_rect)

    def move(self, paddle1, paddle2,fastball=0,xspeed=1,yspeed=1,didhit=False):
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
        if fastball == 0:
            if (x1<=self.ball_rect.center[0]<=x2 and y1 <= self.ball_rect.center[1] <= y2) or (a1<=self.ball_rect.center[0]<=a2 and b1<=self.ball_rect.center[1]<=b2) and fastball == 0 :
                self.direction_x = -self.direction_x
                print("adas")
            if self.ball_rect.top <= 0 or self.ball_rect.bottom >= display_height and fastball == 0:
                self.direction_y = -self.direction_y
                self.yMovement+=2

            if self.ball_rect.center[0] <= 0 or self.ball_rect.center[0] >= display_width and fastball == 0:
                if self.ball_rect.center[0] <= 0:
                    points2 += 1
                else:
                    points1 += 1
                self.ball_rect = self.ball_rect.move((990 - self.ball_rect.center[0], 540 - self.ball_rect.center[1]))
                self.xMovement = random.randint(5, 20)
                self.yMovement = random.randint(5, 20)
                time.sleep(1)
                return True
        if fastball == 1:
            if self.ball_rect.center[0] <= 30:
                location[0]=(self.ball_rect.center[1])
                self.direction_x = -self.direction_x
            if self.ball_rect.center[0] >= 1880:
                self.direction_x = -self.direction_x
            if self.ball_rect.top <= 0 or self.ball_rect.bottom >= display_height:
                self.direction_y = -self.direction_y
                self.yMovement+=2*self.speed
            if didhit==True:
                self.xMovement=xspeed
                self.yMovement=yspeed
                self.ball_rect = self.ball_rect.move((990 - self.ball_rect.center[0], 540 - self.ball_rect.center[1]))

        self.ball_rect = self.ball_rect.move(self.direction_x * self.xMovement, self.direction_y * self.yMovement)
        pygame.time.delay(10)


        Ball.place(self)
        pygame.display.update()


