import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    tmr = 0
    x = 0
    y = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img2, [-tmr + 1600, 0])
        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img, [-tmr+3200, 0])
        kk_rct = kk_img.get_rect()
        kk_rct.center = 300, 200
        k = pg.key.get_pressed()
        if k[pg.K_UP]:
            y -= 1
        elif k[pg.K_DOWN]:
            y += 1
        elif k[pg.K_RIGHT]:
            x += 2
        elif k[pg.K_LEFT]:
            x -= 1
        kk_rct.move_ip((x-tmr, y))
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1
        if tmr == 3199:
            tmr = 0
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()