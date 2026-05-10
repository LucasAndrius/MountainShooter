import pygame as pg

pg.init()

window = pg.display.set_mode(size=(800, 480))
print('setup end')

print('loop start')

# Inicio Mantem janela aberta
while True:
    # check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("Quitting...")
            pg.quit()  # Close window
            quit()  # end pymage
# Fim Mantem janela aberta
