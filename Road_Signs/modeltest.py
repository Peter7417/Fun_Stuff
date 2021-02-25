import tensorflow as tf
import pygame
import sys
import cv2
import os
import numpy as np

# Global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HEIGHT = 400
WIDTH = 600
IMG_WIDTH = 30
IMG_HEIGHT = 30

# Initialize pygame
pygame.init()
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)

# Initialize font sizes
OPEN_SANS = "assets/fonts/OpenSans-Regular.ttf"
smallFont = pygame.font.Font(OPEN_SANS, 20)
largeFont = pygame.font.Font(OPEN_SANS, 40)

# Load production model
model = tf.keras.models.load_model('road_sign_model')

# Set pygame to an initialization mode
prediction = None
Initialization = True

# Preliminaries to create a text input box
input_box = pygame.Rect(250, 350, 40, 32)
text = ''
color_inactive = pygame.Color('aquamarine3')
color_active = pygame.Color('darkcyan')
color = color_inactive
active = False


# Function to get the path of the desired file
def get_location(location):
    folder_path = os.getcwd()
    picture = os.path.join('testing_data',location)
    return os.path.join(folder_path, picture)


# Function to process the test image before comparing it against the production model
def get_image(info):
    pic = cv2.imread(get_location(info), cv2.IMREAD_COLOR)
    res = cv2.resize(pic, (IMG_HEIGHT, IMG_WIDTH), interpolation=cv2.INTER_AREA)

    return np.array(res).reshape(1, 30, 30, 3)


def get_sign(value):
    road_sign = {
        0: '20 Zone Sign',
        1: '30 Zone Sign',
        2: '50 Zone Sign',
        3: '60 Zone Sign',
        4: '70 Zone Sign',
        5: '80 Zone Sign',
        6: 'End of 80 Zone Sign',
        7: '100 Zone Sign',
        8: '120 Zone Sign',
        9: 'No Passing (overtaking) for any vehicle type except one line (track) transport Sign',
        10: 'No passing for vehicles with a total weight of over 3.5 t Sign',
        11: 'Indicates priority, only at the upcoming intersection or crossing Sign',
        12: 'Priority Road starts Sign',
        13: 'Yield Sign',
        14: 'Stop Sign',
        15: 'No entry for any type of Vehicle Sign',
        16: 'No entry for motor vehicles with a maximum authorized mass of more than 3.5 t Sign',
        17: 'Do not enter Sign',
        18: 'This is a general danger or warning Sign',
        19: 'A single curve is approaching in the left direction Sign',
        20: 'A single curve is approaching in the right direction Sign',
        21: 'Indicates an approaching double curve - first to the left Sign',
        22: 'Warning of a rough road ahead Sign',
        23: 'The danger of skidding or slipping Sign',
        24: 'The road narrows from the right side Sign',
        25: 'Man at work Sign',
        26: 'Traffic lights ahead Sign',
        27: 'PPedestrians may cross the road Sign',
        28: 'Pay attention to children Sign',
        29: 'Be aware of cyclists Sign',
        30: 'Beware of an icy road ahead Sign',
        31: 'Indicates wild animals may cross the road Sign',
        32: 'End of all previously set passing and speed restrictions Sign',
        33: 'Indicates that traffic must turn right Sign',
        34: 'Indicates that traffic must turn left Sign',
        35: 'The mandatory direction of travel is straight ahead Sign',
        36: 'Mandatory directions of travel, straight ahead or right Sign',
        37: 'Mandatory directions of travel, straight ahead or left Sign',
        38: 'Drive from the right of the obstacle Sign',
        39: ' Drive from the left of the obstacle Sign',
        40: 'Indicates entrance to a traffic circle Sign',
        41: 'End of the no-passing zone for vehicles under 3.5 t Sign',
        42: 'End of all passing restrictions Sign',
    }
    return road_sign[value]

while True:

    for event in pygame.event.get():
        # Handle the instance when the user closes the pygame application
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
                    Initialization = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Set the pygame background color
    screen.fill(BLACK)

    # Check if the mouse button is clicked
    click, _, _ = pygame.mouse.get_pressed()
    if click == 1:
        # If true, return the position of the click
        mouse = pygame.mouse.get_pos()
    else:
        mouse = None

    # Create and draw the reset button
    resetButton = pygame.Rect(50, 300, 100, 30)
    resetText = smallFont.render("Reset", True, BLACK)
    resetTextRect = resetText.get_rect()
    resetTextRect.center = resetButton.center
    pygame.draw.rect(screen, WHITE, resetButton)
    screen.blit(resetText, resetTextRect)

    # Create and draw the predict button
    predictButton = pygame.Rect(250,300,100,30)
    predictText = smallFont.render("Predict", True, BLACK)
    predictTextRect = predictText.get_rect()
    predictTextRect.center = predictButton.center
    pygame.draw.rect(screen, WHITE,predictButton)
    screen.blit(predictText,predictTextRect)

    # Create the text information box
    infoBox = pygame.Rect(50,350,200,32)
    infoBoxText = smallFont.render("Type in file name", True, BLACK)
    infoBoxTextRect = infoBoxText.get_rect()
    infoBoxTextRect.center = infoBox.center

    # Create the input text box
    surface_txt = smallFont.render(text, True, WHITE)
    # Resize the box if the text is too long.
    width = max(200, surface_txt.get_width()+10)
    input_box.w = width
    # Blit the text.
    screen.blit(surface_txt, (input_box.x+5, input_box.y+5))

    if Initialization is True:
        # If the state of the program is Initialization of if the reset button is pressed
        # set the test image space to BLACK and draw the text information box and input text box
        image_space = pygame.Rect(50,50,300,230)
        # Setting image space to BLACK
        pygame.draw.rect(screen,BLACK,image_space)
        # Drawing the text information box
        pygame.draw.rect(screen, WHITE,infoBox)
        # Showing the text inside the information box
        screen.blit(infoBoxText,infoBoxTextRect)
        # Drawing the text input box
        pygame.draw.rect(screen, color, input_box,2)
    else:
        # If program state is all but the above, show the test image scaled down
        img = pygame.image.load(get_location(data))
        screen.blit(pygame.transform.scale(img, (300, 230)), (50,50))

    if mouse and resetButton.collidepoint(mouse):
        # Set the program state to reset when pressed
        prediction = None
        Initialization = True

    if mouse and predictButton.collidepoint(mouse):
        # Begin image prediction
        image = get_image(data)
        prediction = model.predict(image).argmax()

    if prediction is not None:
        # resultText = smallFont.render("I think it is " + str(prediction), True, WHITE)
        resultText = smallFont.render(get_sign(prediction), True, WHITE)
        resultTextRect = resultText.get_rect()
        # height = max(200, resultText.get_width()+10)
        # resultTextRect.h = height
        offset = 320
        resultTextRect.center = (offset + ((WIDTH-offset)/2), 100)
        screen.blit(resultText, resultTextRect)

    pygame.display.flip()
