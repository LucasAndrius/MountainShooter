#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg

from code.menu import Menu


class Game:
    def __init__(self):

        pg.init()
        self.window = pg.display.set_mode(size=(800, 480))

    def run(self, ):

        # Inicio Mantem janela aberta
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # check for all events
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit()  # Close window
            #         quit()  # end pymage
        # Fim Mantem janela aberta
