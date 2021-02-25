import tensorflow as tf
import pygame
import sys
import cv2
import os
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HEIGHT = 400
WIDTH = 600
IMG_WIDTH = 30
IMG_HEIGHT = 30

pygame.init()
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)

OPEN_SANS = "assets/fonts/OpenSans-Regular.ttf"
smallFont = pygame.font.Font(OPEN_SANS, 20)
largeFont = pygame.font.Font(OPEN_SANS, 40)



model = tf.keras.models.load_model('Traffic_model')
prediction = None
count = None

input_box = pygame.Rect(250, 350, 40, 32)
text = ''
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False


def get_location(data):
    folder_path = os.getcwd()
    picture = os.path.join('testing_data',data)
    return os.path.join(folder_path, picture)


def get_image(info):
    pic = cv2.imread(get_location(info), cv2.IMREAD_COLOR)
    res = cv2.resize(pic, (IMG_HEIGHT, IMG_WIDTH), interpolation=cv2.INTER_AREA)

    return np.array(res).reshape(1, 30, 30, 3)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
            # Change the current color of the input box.
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    data = text
                    text = ''
                    count = 0
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.fill(BLACK)

    click, _, _ = pygame.mouse.get_pressed()
    if click == 1:
        mouse = pygame.mouse.get_pos()
    else:
        mouse = None

    resetButton = pygame.Rect(50, 300, 100, 30)
    resetText = smallFont.render("Reset", True, BLACK)
    resetTextRect = resetText.get_rect()
    resetTextRect.center = resetButton.center
    pygame.draw.rect(screen, WHITE, resetButton)
    screen.blit(resetText, resetTextRect)

    predictButton = pygame.Rect(250,300,100,30)
    predictText = smallFont.render("Predict", True, BLACK)
    predictTextRect = predictText.get_rect()
    predictTextRect.center = predictButton.center
    pygame.draw.rect(screen, WHITE,predictButton)
    screen.blit(predictText,predictTextRect)

    infoBox = pygame.Rect(50,350,200,32)
    infoBoxText = smallFont.render("Type in file name", True, BLACK)
    infoBoxTextRect = infoBoxText.get_rect()
    infoBoxTextRect.center = infoBox.center

    # input text box

    surface_txt = smallFont.render(text, True, WHITE)
    # Resize the box if the text is too long.
    width = max(200, surface_txt.get_width()+10)
    input_box.w = width
    # Blit the text.
    screen.blit(surface_txt, (input_box.x+5, input_box.y+5))

    if count is None:
        image_space = pygame.Rect(50,50,300,230)
        pygame.draw.rect(screen,BLACK,image_space)
        pygame.draw.rect(screen, WHITE,infoBox)
        screen.blit(infoBoxText,infoBoxTextRect)
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box,2)
    else:
        img = pygame.image.load(get_location(data))
        screen.blit(pygame.transform.scale(img, (300, 230)), (50,50))

    if mouse and resetButton.collidepoint(mouse):
        prediction = None
        count = None

    if mouse and predictButton.collidepoint(mouse):
        image = get_image(data)
        prediction = model.predict(image).argmax()

    if prediction is not None:
        # print(prediction)
        resultText = smallFont.render("I think it is " + str(prediction), True, WHITE)
        resultTextRect = resultText.get_rect()
        offset = 320
        resultTextRect.center = (offset + ((WIDTH-offset)/2), 100)
        screen.blit(resultText, resultTextRect)

    pygame.display.flip()
