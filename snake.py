import pygame
import random 
pygame.init()
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height))
running = True

colors = [
    "red",
    "blue",
    "purple"
]

class Food:
    x, y = random.randint(0, window_width-20), random.randint(0, window_height-20) 
    color = random.choice(colors)
    size = 20

    def createFood(self):
        
        pygame.draw.circle(window, self.color, (self.x,self.y), self.size)
        # pygame.draw.rect(window,"blue", pygame.Rect(self.x, self.y, self.size, self.size))

    def eaten(self, player):
        if player[0] >= self.x-20 and player[0] <= self.x+20 and player[1] >= self.y-20 and player[1] <= self.y+20 :
            
            self.moveFood()
            return True
    
    def moveFood(self):
        self.x = random.randint(0, window_width-20)
        self.y = random.randint(0, window_height-20)
        self.color = random.choice(colors)
        


    

class Player:
    x, y = 0, 0
    height, width = 0, 0
    color = (0,0,0)
    speed = 0
    direction = ""
    score=0
    lost = False

    def drawPlayer(self):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def getPlayerPosition(self):
        return (self.x, self.y)
    def checkForlimits(self):
        if self.x + self.width/2 >= window_width or self.y + self.height/2 >= window_height or self.x + self.width/2 <= 0 or self.y + self.height/2 <= 0:
            self.lost = True
        return self.lost
    def movePlayer(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP] :
            self.direction = "UP"
        if keys[pygame.K_RIGHT] :
            self.direction = "RIGHT"
        if keys[pygame.K_LEFT] :
            self.direction = "LEFT"
        if keys[pygame.K_DOWN] :
            self.direction = "DOWN"


        if self.direction == "RIGHT":
            self.x += self.speed
        if self.direction == "UP":
            self.y -= self.speed
        if self.direction == "DOWN":
            self.y += self.speed
        if self.direction == "LEFT":
            self.x -= self.speed
    def game_over(self):
        pygame.quit()

snake = Player()
snake.x = 200
snake.y = 200
snake.height = 20
snake.width = 20
snake.color = (0,0,230)
snake.speed = 1
food = Food()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill("black")    
    food.createFood()
    if food.eaten(snake.getPlayerPosition()) :
        snake.score += 10
    
    snake.drawPlayer()
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"score : {snake.score}", True, "white")
    window.blit(score_text, (10, 10))
    snake.movePlayer()
    if snake.checkForlimits() :
        snake.game_over()   
    pygame.display.flip()

pygame.quit()