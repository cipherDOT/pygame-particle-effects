
import pygame
from pygame.display import update
from pygame.locals import *
import random


pygame.init()

width = 500
height = 500

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Particle Physics')
font = pygame.font.Font("./custom_fonts/ARCADECLASSIC.ttf", 24)


class ParticlePrinciple(object):
    def __init__(self):
        self.particles = []

    def emit(self):
        if self.particles:
            self.delete()
            for particle in self.particles:
                particle[0][0] += particle[2][0]
                particle[0][1] += particle[2][1]
                particle[1] -= 0.2
                pygame.draw.circle(display, (200, 200, 200),
                                   particle[0], int(particle[1]))

    def add(self):
        x_pos, y_pos = pygame.mouse.get_pos()
        radius = 10
        direction = [random.uniform(-1, 1), random.uniform(-1, 1)]
        particle_circle = [[x_pos, y_pos], radius, direction]
        self.particles.append(particle_circle)

    def delete(self):
        particle_copy = [
            particle for particle in self.particles if particle[1] > 1]
        self.particles = particle_copy


def update_fps(clock):
    fps = str(int(clock.get_fps())) + 'fps'
    fps_text = font.render(fps, 1, pygame.Color("Cyan"))
    return fps_text


def main():
    run = True
    particles = ParticlePrinciple()
    PARTICLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICLE_EVENT, 40)
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

            if event.type == PARTICLE_EVENT:
                particles.add()

        display.fill((30, 30, 30))
        display.blit(update_fps(clock), (10, 10))
        particles.emit()
        pygame.display.flip()
        clock.tick(120)


if __name__ == "__main__":
    main()
