
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

def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((0, 0, 0))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        # clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()

