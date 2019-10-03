import datetime
import pygame
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def update(world):
    start = datetime.datetime.now()
    for s in world._entities:
        if s.has("Playable"):
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
                obj = world.get_entity((coords[0], coords[1] + 32))
                print(coords)
                for s in obj:
                    if s and s.has("Menu"):
                        s.get("Menu").show()
                if not world.get_solid((coords[0], coords[1]+32)):
                    player.get("Coordinates").add(0,32)



            if event.key == pygame.K_KP_ENTER:
                print(player.get("Inventory").get())
                player.get("Inventory").use()

            if event.key == pygame.K_F5:
                world.save()

            if event.key == pygame.K_F6:
                world.load()
                for s in world._entities:
                    if s.has("Playable"):
                        player = s
                        break

    world.update()
    world.timer.update(world._entities)
    # print(len(world._entities), len(world._systems))

    clock.tick(10) # FPS

    world.draw(screen)
    pygame.display.flip()

    #print(datetime.datetime.now() - start)


