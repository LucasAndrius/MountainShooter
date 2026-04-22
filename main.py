import pygame as pg

pg.init()

window = pg.display.set_mode(size = (600, 480) )
print('setup end')

print('loop start')
while True:
    # check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()            # Close window
            quit()               # end pymage