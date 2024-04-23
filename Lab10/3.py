import pygame 
import sys, random
import psycopg2
from color_palette import *

# PostgreSQL connection parameters
DB_NAME = "your_db_name"
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_HOST = "your_db_host"
DB_PORT = "your_db_port"

# Connect to PostgreSQL
conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
cursor = conn.cursor()

pygame.init()

WIDTH = 600
HEIGHT = 600

CELL = 30

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorBLACK, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((HEIGHT, WIDTH))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                print("Collision! Game Over!")
                pygame.quit()
                sys.exit()

        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))

class Food:
    def __init__(self):
        self.pos = self.random_position()

    def random_position(self):
        x = random.randint(0, (WIDTH // CELL) - 1)
        y = random.randint(0, (HEIGHT // CELL) - 1)
        return Point(x, y)

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


def create_user(username):
    try:
        cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
        conn.commit()
        print("User created successfully")
    except psycopg2.Error as e:
        print("Error creating user:", e)


def check_user(username):
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user:
            print("User exists. Current level:", user[2])
        else:
            print("User does not exist.")
    except psycopg2.Error as e:
        print("Error checking user:", e)


def save_score(username, score):
    try:
        cursor.execute("INSERT INTO user_scores (username, score) VALUES (%s, %s)", (username, score))
        conn.commit()
        print("Score saved successfully")
    except psycopg2.Error as e:
        print("Error saving score:", e)


def load_scores(username):
    try:
        cursor.execute("SELECT * FROM user_scores WHERE username = %s", (username,))
        scores = cursor.fetchall()
        if scores:
            print("Scores for user", username, ":")
            for row in scores:
                print("Score:", row[2])
        else:
            print("No scores found for user", username)
    except psycopg2.Error as e:
        print("Error loading scores:", e)


def play_game():
    FPS = 5
    clock = pygame.time.Clock()

    food = Food()
    snake = Snake()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                elif event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                elif event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
                elif event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1

        draw_grid_chess()

        snake.move()
        snake.check_collision(food)

        snake.draw()
        food.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


def main():
    username = input("Enter your username: ")
    check_user(username)

    create_user(username)
    play_game()

    conn.close()


if __name__ == "__main__":
    main()










"""import pygame 
import sys, random
from color_palette import *

pygame.init()

WIDTH = 600
HEIGHT = 600

CELL = 30

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorBLACK, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((HEIGHT, WIDTH))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    # def move(self):
    #     head = self.body[0]
    #     self.body.pop()

    #     new_x = head.x + self.dx
    #     new_y = head.y + self.dy

    #     new_head = Point(new_x, new_y)
    #     self.body.insert(0, new_head)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                print("Collision! Game Over!")
                pygame.quit()
                #sys.exit()

        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))

class Food:
    def __init__(self):
        self.pos = self.random_position()

    def random_position(self):
        x = random.randint(0, (WIDTH // CELL) - 1)
        y = random.randint(0, (HEIGHT // CELL) - 1)
        return Point(x, y)

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


FPS = 5
clock = pygame.time.Clock()

food = Food()
snake = Snake()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    draw_grid_chess()

    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()

    pygame.display.flip()
    clock.tick(FPS)
"""