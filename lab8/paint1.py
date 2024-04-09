import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5
CURRENT_COLOR = colorRED

currX = 0
currY = 0

prevX = 0
prevY = 0

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_rectangle(x1, y1, x2, y2, color):
    pygame.draw.rect(screen, color, calculate_rect(x1, y1, x2, y2), THICKNESS)

def draw_square(x1, y1, x2, y2, color):
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    size = min(width, height)
    pygame.draw.rect(screen, color, pygame.Rect(min(x1, x2), min(y1, y2), size, size), THICKNESS)

def draw_right_triangle(x1, y1, x2, y2, color):
    pygame.draw.polygon(screen, color, [(x1, y1), (x2, y1), (x1, y2)], THICKNESS)

def draw_equilateral_triangle(x1, y1, x2, y2, color):
    height = abs(y1 - y2)
    half_base = abs(x1 - x2) // 2
    pygame.draw.polygon(screen, color, [(x1, y2), (x2, y2), (x1 + half_base, y1)], THICKNESS)

def draw_rhombus(x1, y1, x2, y2, color):
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    pygame.draw.polygon(screen, color, [(x1 + width // 2, y1), (x2, y1 + height // 2), (x1 + width // 2, y2), (x1, y1 + height // 2)], THICKNESS)

done = False

current_shape = "rectangle"

while not done:

    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            
        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                if current_shape == "rectangle":
                    draw_rectangle(prevX, prevY, currX, currY, CURRENT_COLOR)
                elif current_shape == "square":
                    draw_square(prevX, prevY, currX, currY, CURRENT_COLOR)
                elif current_shape == "right_triangle":
                    draw_right_triangle(prevX, prevY, currX, currY, CURRENT_COLOR)
                elif current_shape == "equilateral_triangle":
                    draw_equilateral_triangle(prevX, prevY, currX, currY, CURRENT_COLOR)
                elif current_shape == "rhombus":
                    draw_rhombus(prevX, prevY, currX, currY, CURRENT_COLOR)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            base_layer.blit(screen, (0, 0))  # Переносим отрисованные фигуры на базовый слой

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r:
                print("Drawing rectangle")
                current_shape = "rectangle"
                CURRENT_COLOR = colorRED
            elif event.key == pygame.K_s:
                print("Drawing square")
                current_shape = "square"
                CURRENT_COLOR = colorGREEN
            elif event.key == pygame.K_t:
                print("Drawing right triangle")
                current_shape = "right_triangle"
                CURRENT_COLOR = colorBLUE
            elif event.key == pygame.K_e:
                print("Drawing equilateral triangle")
                current_shape = "equilateral_triangle"
                CURRENT_COLOR = colorWHITE
            elif event.key == pygame.K_h:
                print("Drawing rhombus")
                current_shape = "rhombus"
                CURRENT_COLOR = colorBLACK

            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1

    pygame.display.flip()
    clock.tick(60)
