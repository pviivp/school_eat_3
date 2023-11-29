from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        label = Label(text='text')

        return label

if __name__ == '__main__':
    MyApp().run()

# import pygame as pg
#
# pg.init()
#
# root = pg.display.set_mode((0, 0), pg.FULLSCREEN)
# clock = pg.time.Clock()
#
# width, height = pg.display.get_window_size()
#
# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             exit()
#
#     root.fill((0, 255, 0))
#
#     pg.draw.rect(root, (255, 0, 0), (0, 0, width, height), 10)
#
#     clock.tick(60)
#     pg.display.flip()