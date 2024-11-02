import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Platformer Game")

#these are the different poses for now, i'll include the sounds and poses in a file
idle_image = pygame.image.load("idle.png").convert_alpha()  # Idle pose
run_image = pygame.image.load("run.png").convert_alpha()    # Running pose
jump_image = pygame.image.load("jump.png").convert_alpha()  # Jumping pose

scale_factor = 0.5  #this is just to determine how large we want to dino to be
idle_image = pygame.transform.scale(idle_image, (int(idle_image.get_width() * scale_factor), int(idle_image.get_height() * scale_factor)))
run_image = pygame.transform.scale(run_image, (int(run_image.get_width() * scale_factor), int(run_image.get_height() * scale_factor)))
jump_image = pygame.transform.scale(jump_image, (int(jump_image.get_width() * scale_factor), int(jump_image.get_height() * scale_factor)))

run_sound = pygame.mixer.Sound("running2.wav")
jump_sound = pygame.mixer.Sound("jumping.mp3")

#these are the dif states for dino
character_state = "idle"
character_x, character_y = 100, 500
character_speed = 5
is_jumping = False
jump_velocity = 15
gravity = 1

is_running_sound_playing = False

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                character_state = "jumping"
                is_jumping = True
                jump_velocity = 15
                jump_sound.play()  # jump sound

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_state = "running"
        character_x -= character_speed
        if not is_running_sound_playing:
            run_sound.play()
            is_running_sound_playing = True
    elif keys[pygame.K_RIGHT]:
        character_state = "running"
        character_x += character_speed
        if not is_running_sound_playing:
            run_sound.play()
            is_running_sound_playing = True
    else:
        if not is_jumping:
            character_state = "idle"
        is_running_sound_playing = False

#had a hard time with this one, but it is just a boundary to make sure the dino does not run off the screen
    if character_x < 0:
        character_x = 0
    elif character_x > 1000 - run_image.get_width():
        character_x = 1000 - run_image.get_width()
#if the height for the jumping isn't that great, lmk and i can fix it
    if is_jumping:
        character_y -= jump_velocity
        jump_velocity -= gravity
        if character_y >= 500:
            character_y = 500
            is_jumping = False
            character_state = "idle"

    if character_state == "idle":
        screen.blit(idle_image, (character_x, character_y))
    elif character_state == "running":
        screen.blit(run_image, (character_x, character_y))
    elif character_state == "jumping":
        screen.blit(jump_image, (character_x, character_y))

    pygame.display.flip()

pygame.quit()
