import sys, pygame, random, math, os

def adjSize(object, changeX, changeY):
    center = object.center
    object.inflate_ip(changeX, changeY)
    object.center = center
    return object

difficulty = 5 - int(input("Choose a difficulty 1, 2, 3: "))
pygame.init()
size = width, height = 1120, 720
screen = pygame.display.set_mode(size)
fps = pygame.time.Clock()
frameNum = 0


font = pygame.font.Font(None, 36)

objSize = objW, objH = 100, 100
object = pygame.Rect(width / 2 - objW / 2, height / 2 - objH / 2, objW, objH)
food = pygame.Rect(random.randint(0, 110), random.randint(0, 700), 20, 20)
poison = pygame.Rect(random.randint(0, 110), random.randint(0, 700), 20, 20)
flag = True
while True:
    screen.fill("black")
    if frameNum >= fps.get_fps():
        frameNum = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_l:
                print(object.x, object.y)
    pygame.draw.rect(screen, "blue", object)
    pygame.draw.rect(screen, "green", food)
    pygame.draw.rect(screen, "red", poison)
    score = font.render("score: " + str(object.width), True, (255, 255, 255))
    screen.blit(score, (10, 10))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        object.move_ip(0, -5)
    if keys[pygame.K_a]:
        object.move_ip(-5, 0)
    if keys[pygame.K_s]:
        object.move_ip(0, 5)
    if keys[pygame.K_d]:
        object.move_ip(5, 0)
    if keys[pygame.K_EQUALS]:
        object = adjSize(object, 5, 5)
    if(flag):
        if object.colliderect(food):
            object = adjSize(object, 50, 50)
            food.topleft = (random.randint(0, 1100), random.randint(0, 700))
            poison.topleft = (random.randint(0, 1100), random.randint(0, 700))
        elif object.colliderect(poison):
            object = adjSize(object, -50, -50)
            poison.topleft = (9999, 9999)
        if object.width < 1120 and object.width > 0 and frameNum % difficulty == 0:
            object = adjSize(object, -1, -1)
        elif object.width <= 0:
            text = font.render("Game Over!", True, (255, 255, 255))
            screen.blit(text, (490, 350))
            flag = False
            score = font.render("score: " + str(object.width), True, (255, 255, 255))
            screen.blit(score, (10, 10))
            pygame.display.flip()
        elif object.width >= 1120:
            text = font.render("You Win!", True, (255, 255, 255))
            screen.blit(text, (490, 350))
            flag = False
            score = font.render("score: " + str(object.width), True, (255, 255, 255))
            screen.blit(score, (10, 10))
            pygame.display.flip()

    if flag: pygame.display.flip()
    frameNum += 1
    fps.tick(60)
