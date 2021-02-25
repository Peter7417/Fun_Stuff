
# import tensorflow as tf
import pygame as pg
import sys
import cv2
import os
import numpy as np

# input_shape = (4, 28, 28, 3)
# x = tf.random.normal(input_shape)
# y = tf.keras.layers.Conv2D(
#     2, 3, activation='relu', input_shape=input_shape[1:])(x)
# z = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(y)
# a = tf.keras.layers.Conv2D(
#     4, 3, activation='relu'
# )(z)
# b = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(a)
# c = tf.keras.layers.Flatten()(b)
# print('x:', x.shape)
# print('y:', y.shape)
# print('z:', z.shape)
# print('a:', a.shape)
# print('b:', b.shape)
# print('c:', c.shape)

# print(os.listdir())
# print(os.path.join('testing_data','no_entry.jpg'))

# def main():
#     screen = pg.display.set_mode((640, 480))
#     font = pg.font.Font(None, 32)
#     clock = pg.time.Clock()
#     input_box = pg.Rect(100, 100, 140, 32)
#     color_inactive = pg.Color('lightskyblue3')
#     color_active = pg.Color('dodgerblue2')
#     color = color_inactive
#     active = False
#     text = ''
#     done = False
#
#     while not done:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 done = True
#             if event.type == pg.MOUSEBUTTONDOWN:
#                 # If the user clicked on the input_box rect.
#                 if input_box.collidepoint(event.pos):
#                     # Toggle the active variable.
#                     active = not active
#                 else:
#                     active = False
#                 # Change the current color of the input box.
#                 color = color_active if active else color_inactive
#             if event.type == pg.KEYDOWN:
#                 if active:
#                     if event.key == pg.K_RETURN:
#                         print(text)
#                         text = ''
#                     elif event.key == pg.K_BACKSPACE:
#                         text = text[:-1]
#                     else:
#                         text += event.unicode
#
#         screen.fill((0, 0, 0))
#         # Render the current text.
#         txt_surface = font.render(text, True, color)
#         # Resize the box if the text is too long.
#         width = max(200, txt_surface.get_width()+10)
#         input_box.w = width
#         # Blit the text.
#         screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
#         # Blit the input_box rect.
#         pg.draw.rect(screen, color, input_box, 2)
#
#         pg.display.flip()
#         # clock.tick(30)
#
#
# if __name__ == '__main__':
#     pg.init()
#     main()
#     pg.quit()

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


print(get_sign(0))