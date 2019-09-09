import datetime
import pygame
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def update(world):
    start = datetime.datetime.now()
    for s in world._entities:
        if s.has("Playable") and s.has("Coordinates"):
            player = s
            break

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Выясняем какая именно кнопка была нажата
            if event.key == pygame.K_LEFT:
                coords = player.get("Coordinates").get()
                if not world.get_solid((coords[0]-32,coords[1])):
                    player.get("Coordinates").add(-32,0)
            if event.key == pygame.K_RIGHT:
                coords = player.get("Coordinates").get()
                if not world.get_solid((coords[0] + 32, coords[1])):
                    player.get("Coordinates").add(32,0)
            if event.key == pygame.K_UP:
                coords = player.get("Coordinates").get()
                if not world.get_solid((coords[0], coords[1]-32)):
                    player.get("Coordinates").add(0,-32)
            if event.key == pygame.K_DOWN:
                coords = player.get("Coordinates").get()
                if not world.get_solid((coords[0], coords[1]+32)):
                    player.get("Coordinates").add(0,32)

    world.update()
    # print(len(world._entities), len(world._systems))

    clock.tick(100) # FPS

    world.draw(screen)
    pygame.display.flip()

    print(datetime.datetime.now() - start)


