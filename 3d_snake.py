import pygame, random

def bounds():
    if snake_body[0].x >= width:
        snake_body[0].x = 0

    if snake_body[0].x < 0:
        snake_body[0].x = width

    if snake_body[0].y >= height:
        snake_body[0].y = 0

    if snake_body[0].y < 0:
        snake_body[0].y = height

    return snake_body[0]
def redirect():
    if keys[pygame.K_LEFT] and direction != 'r':
        return 'l'
    if keys[pygame.K_RIGHT] and direction != 'l':
        return 'r'
    if keys[pygame.K_DOWN] and direction != 'u':
        return 'd'
    if keys[pygame.K_UP] and direction != 'd':
        return 'u'
    
    return direction
def draw_polygon(color, r, d, eye_level):
        ps, p = snake_size, pygame
        #right includes left, and down includes up using negitive numbers
        color = ((color[0])/2, (color[1])/2, (color[2])/2)
        r_a = (eye_level[0] - r)
        d_a = (eye_level[1] - d)
        
        top_left = (r*ps, d*ps)
        top_right = ((r + 1)*ps, d*ps)
        bottom_left = ((r)*ps, (d + 1)*ps)
        bottom_right = ((r + 1)*ps, (d + 1)*ps)
        
        top_left_corner = (top_left[0] + r_a, top_left[1] + d_a)
        top_right_corner = (top_right[0] + r_a, top_right[1] + d_a)
        bottom_left_corner = (bottom_left[0] + r_a, bottom_left[1] + d_a)
        bottom_right_corner = (bottom_right[0] + r_a, bottom_right[1] + d_a)

        p.draw.polygon(window, color, (top_left, top_left_corner, top_right_corner, top_right))
        p.draw.polygon(window, color, (top_left, top_left_corner, bottom_left_corner, bottom_left))
        p.draw.polygon(window, color, (top_right, top_right_corner, bottom_right_corner, bottom_right))
        p.draw.polygon(window, color, (bottom_left, bottom_left_corner, bottom_right_corner, bottom_right))

        p.draw.line(window, (0,0,0), top_right, top_right_corner, 1)
        p.draw.line(window, (0,0,0), top_left, top_left_corner, 1)
        p.draw.line(window, (0,0,0), top_right, top_right_corner, 1)
        p.draw.line(window, (0,0,0), bottom_left, bottom_left_corner, 1)


pygame.init()
snake_size = 10
width, height = snake_size*20, snake_size*20
window = pygame.display.set_mode((1000, 1000))
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
snake_body = [pygame.Rect(random.randint(0, width), random.randint(0, height), snake_size, snake_size) for i in range(3)]
apple = pygame.Rect(random.randint(0, width), random.randint(0, height), snake_size, snake_size)
direction = 'r'
time = 0

while True:
    time += 1
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    for i in range(len(snake_body)-1, 0, -1):
        snake_body[i].x = snake_body[i-1].x
        snake_body[i].y = snake_body[i-1].y
    keys = pygame.key.get_pressed()

    direction = redirect()

    if direction == 'l':
        snake_body[0].x -= snake_size
    if direction == 'r':
        snake_body[0].x += snake_size
    if direction == 'u':
        snake_body[0].y -= snake_size
    if direction == 'd':
        snake_body[0].y += snake_size

    snake_body[0] = bounds()

    if snake_body[0].colliderect(apple):
        apple = pygame.Rect(random.randint(0, width), random.randint(0, height), snake_size, snake_size)
        snake_body.append(pygame.Rect(random.randint(0, width), random.randint(0, height), snake_size, snake_size))
        snake_size += 1
        for i in snake_body:
            i[-1] += 1
            i[-2] += 1
        width, height = snake_size*20, snake_size*20
        window = pygame.display.set_mode((width, height))
    window.fill('black')
    color_size = (time%120)/10
    for i in range(20):
        for j in range(20):
            pygame.draw.rect(window, (i*color_size, max(0, (i-j)*color_size), j*color_size), pygame.Rect(i*snake_size, j*snake_size, snake_size, snake_size))
    for i in snake_body:
         draw_polygon((0, 255, (255/len(snake_body)*(snake_body.index(i)+1))), i[0]/snake_size, i[1]/snake_size, (10, 10))
    for i in snake_body:
        pygame.draw.rect(window, (0, 255, 255/len(snake_body)*(snake_body.index(i)+1)), i)
    pygame.draw.rect(window, (255, 0, time%50), apple)
    pygame.display.update()
 

 