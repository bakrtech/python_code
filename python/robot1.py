#import stuff
import pygame
import os


class Entity():
    X = 150
    Y = 160
    change_X = 0
    change_Y = 0


p1 = Entity()


pygame.init()

screen = pygame.display.set_mode((800, 600))


def player1():
   # p1.Y +=0.1
    screen.blit(player, (p1.X, p1.Y))


# loader
icon = pygame.image.load("robotic-arm.png")
player = pygame.image.load("robot.png")

pygame.display.set_caption("robot1")
pygame.display.set_icon(icon)

working = True

while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print(p1.X)
                p1.change_X -= 0.1
            if event.key == pygame.K_d:
                print(p1.X)
                p1.change_X += 0.1
            if event.key == pygame.K_s:
                print(p1.Y)
                p1.change_Y += 0.1
            if event.key == pygame.K_w:
                print(p1.Y)
                p1.change_Y -= 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                p1.change_X = 0
            if event.key == pygame.K_s or event.key == pygame.K_w:
                p1.change_Y = 0
    screen.fill((220, 220, 205))
    player1()
    p1.X += p1.change_X
    p1.Y += p1.change_Y

    if p1.X <= 0:
        p1.X = 1
    if p1.X >= 736:
        p1.X = 735
    if p1.Y <= 0:
        p1.Y = 0
    if p1.Y >= 530:
        p1.Y = 530
    pygame.display.update()
