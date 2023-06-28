import os
import pygame
import sys
import time
import path
import random
import PIL

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) < 2:
    name = 'moni'
else:
    name = sys.argv[1]

if len(sys.argv) < 3:
    number_of_rounds = 3
else:
    number_of_rounds = sys.argv[2]

print("name: " + name)


def draw_robot():
    # screen.fill((0, 0, 130))
    robot = pygame.image.load(GAME_PATH + "/images/chatbot.png")
    robot_x = (screen.get_width() / 2) - (robot.get_width() / 2)
    robot_y = screen.get_height() / 2 - (robot.get_height() / 2)
    screen.blit(robot, (robot_x, robot_y))
    pygame.display.update()


def wait_for_sound_end(timeout_length):
    timeout = time.time() + timeout_length
    while pygame.mixer.get_busy() and time.time() < timeout:
        pass


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1800, 1202), pygame.RESIZABLE)
draw_robot()
pygame.display.update()

# os.system("mpg123 " + GAME_PATH + "/sounds/hello.mp3")
# os.system("mpg123 " + GAME_PATH + "/sounds/" + "peter" + ".mp3")

time.sleep(1)

greeting_sound = pygame.mixer.Sound(GAME_PATH + "/sounds/hello.mp3")
name_sound = pygame.mixer.Sound(GAME_PATH + "/sounds/moni.mp3")
greeting_sound.play()
wait_for_sound_end(60)
name_sound.play()
game_running = True

while game_running:
    pygame.event.clear()
    event = pygame.event.poll()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.VIDEORESIZE:
            pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            time.sleep(1)
            draw_robot()
            pygame.display.update()

pygame.quit()
