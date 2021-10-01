import os
import pygame
import sys
import time
import path
import random


def draw_robot():
    robot = pygame.image.load(GAME_PATH + "/images/chatbot.png")
    robotX = 601
    robotY = 300
    screen.blit(robot, (robotX, robotY))
    pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((1800, 1202), pygame.RESIZABLE)
GAME_PATH = path.Path(__file__).parent
screen.fill((0, 0, 130))
draw_robot()
pygame.display.update()


os.system("mpg123 " + GAME_PATH + "/sounds/greeting.mp3")


def get_guess():
    pygame.event.clear()

    while 1:
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            os.system("mpg123 " + GAME_PATH + "/sounds/escape.mp3")
            time.sleep(10)
            sys.exit()

        if event.type == pygame.KEYDOWN:
            return event.key
        else:
            pass


class GameRound:
    def __init__(self):
        # TODO: Add non character buttons to say what Moni hit
        self.key_sounds = {
            pygame.K_a: "a.mp3",
            pygame.K_b: "b.mp3",
            pygame.K_c: "c.mp3",
            pygame.K_d: "d.mp3",
            pygame.K_e: "e.mp3",
            pygame.K_f: "f.mp3",
            pygame.K_g: "g.mp3",
            pygame.K_h: "h.mp3",
            pygame.K_i: "i.mp3",
            pygame.K_j: "j.mp3",
            pygame.K_k: "k.mp3",
            pygame.K_l: "l.mp3",
            pygame.K_m: "m.mp3",
            pygame.K_n: "n.mp3",
            pygame.K_o: "o.mp3",
            pygame.K_p: "p.mp3",
            pygame.K_q: "q.mp3",
            pygame.K_r: "r.mp3",
            pygame.K_s: "s.mp3",
            pygame.K_t: "t.mp3",
            pygame.K_u: "u.mp3",
            pygame.K_v: "v.mp3",
            pygame.K_w: "w.mp3",
            pygame.K_x: "x.mp3",
            pygame.K_y: "y.mp3",
            pygame.K_0: "0.mp3",
            pygame.K_1: "1.mp3",
            pygame.K_2: "2.mp3",
            pygame.K_3: "3.mp3",
            pygame.K_4: "4.mp3",
            pygame.K_5: "5.mp3",
            pygame.K_6: "6.mp3",
            pygame.K_7: "7.mp3",
            pygame.K_8: "8.mp3",
            pygame.K_9: "9.mp3",
            pygame.K_BACKSPACE: "backspace.mp3",
            pygame.K_TAB: "tab.mp3",
            pygame.K_RETURN: "return.mp3",
            pygame.K_SPACE: "space.mp3",
            pygame.K_CAPSLOCK: "capslock.mp3",
            pygame.K_LSHIFT: "left_shift.mp3",
            pygame.K_RSHIFT: "right_shift.mp3",
            pygame.K_LCTRL: "left_control.mp3",
            pygame.K_RCTRL: "right_control.mp3",
            pygame.K_RALT: "right_alt.mp3",
            pygame.K_LALT: "left_alt.mp3",
            pygame.K_BACKQUOTE: "grave.mp3",
            pygame.K_BACKSLASH: "backslash.mp3",
            pygame.K_SLASH: "forward_slash.mp3",
            pygame.K_COMMA: "comma.mp3",
            pygame.K_PERIOD: "period.mp3",
            pygame.K_DELETE: "delete.mp3",
            pygame.K_UP: "up_arrow.mp3",
            pygame.K_DOWN: "down_arrow.mp3",
            pygame.K_RIGHT: "right_arrow.mp3",
            pygame.K_LEFT: "left_arrow.mp3",
            pygame.K_HOME: "home.mp3",
            pygame.K_PAGEUP: "page_up.mp3",
            pygame.K_PAGEDOWN: "page_down.mp3",
            pygame.K_END: "end.mp3",
            pygame.K_F1: "F1.mp3",
            pygame.K_F2: "F2.mp3",
            pygame.K_F3: "F3.mp3",
            pygame.K_F4: "F4.mp3",
            pygame.K_F5: "F5.mp3",
            pygame.K_F6: "F6.mp3",
            pygame.K_F7: "F7.mp3",
            pygame.K_F8: "F8.mp3",
            pygame.K_F9: "F9.mp3",
            pygame.K_F10: "F10.mp3",
            pygame.K_F11: "F11.mp3",
            pygame.K_F12: "F12.mp3",
            pygame.K_SEMICOLON: "semicolon.mp3",
            pygame.K_MINUS: "minus.mp3",
            pygame.K_EQUALS: "equalS.mp3",
            pygame.K_LEFTBRACKET: "left_bracket.mp3",
            pygame.K_RIGHTBRACKET: "right_bracket.mp3",
            pygame.K_LSUPER: "left_windows_key.mp3",
            pygame.K_RSUPER: "right_windows_key.mp3",
            pygame.K_PRINT: "print_screen.mp3"
        }
        self.search_key_index = random.randint(0, 35)

        self.search_key = list(self.key_sounds.keys())[self.search_key_index ]

        if self.search_key_index < 26:
            os.system("mpg123 " + GAME_PATH + "/sounds/can_you_find_letter.mp3")
        else:
            os.system("mpg123 " + GAME_PATH + "/sounds/can_you_find_number.mp3")
        os.system("mpg123 " + GAME_PATH + "/sounds/" + self.key_sounds[self.search_key])

    def say_guess(self, p_pygame_key):
        print('Playing')
        os.system("mpg123 " + GAME_PATH + "/sounds/" + self.key_sounds[p_pygame_key])

    def listen(self):
        stop = False

        while not stop:
            guess_key = get_guess()

            if guess_key == self.search_key:
                os.system("mpg123 " + GAME_PATH + "/sounds/correct_guess.mp3")
                stop = True
            else:
                os.system("mpg123 " + GAME_PATH + "/sounds/incorrect_guess.mp3")
                os.system("mpg123 " + GAME_PATH + "/sounds/" + self.key_sounds[guess_key])
                os.system("mpg123 " + GAME_PATH + "/sounds/looking_for.mp3")
                os.system("mpg123 " + GAME_PATH + "/sounds/" + self.key_sounds[self.search_key])


def main_game():
    for x in range(3):
        game_round = GameRound()
        game_round.listen()


main_game()
