import os
import pygame
import sys
import time
import path
import random

GAME_PATH = os.path.dirname(os.path.abspath(__file__))

def draw_robot():
    robot = pygame.image.load(GAME_PATH + "/images/chatbot.png")
    robotX = 601
    robotY = 300
    screen.blit(robot, (robotX, robotY))
    pygame.display.update()

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1800, 1202), pygame.RESIZABLE)
screen.fill((0, 0, 130))
draw_robot()
pygame.display.update()

#os.system("mpg123 " + GAME_PATH + "/sounds/hello.mp3")
#os.system("mpg123 " + GAME_PATH + "/sounds/" + name + ".mp3")

greeting_sound = pygame.mixer.Sound(GAME_PATH + "/sounds/hello.mp3")
name_sound = pygame.mixer.Sound(GAME_PATH + "/sounds/moni.mp3")
greeting_sound.play()
name_sound.play()
game_running = True
while game_running:
	
	pygame.event.clear()
	event = pygame.event.poll()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_running = False


