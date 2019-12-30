# import the pygame module, so you can use it
import pygame


# define a main function
def main():
    clock = pygame.time.Clock()
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.mixer.init()
    pygame.mixer.music.load('./bwc/5.mp3')
    logo = pygame.image.load("./bwc/3.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("联机黑白棋")
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((900, 580))
    jiemian = pygame.image.load("./bwc/2.png")
    jiemian.convert()
    beijing = pygame.image.load("./bwc/6.png")
    beijing.convert()
    screen1 = pygame.Surface(screen.get_size())
    screen2 = pygame.Surface(screen.get_size())
    screen1 = screen1.convert()
    screen2 = screen2.convert()
    danren = pygame.image.load("./bwc/danren.png")
    danren.convert()
    danren1 = pygame.image.load("./bwc/danren1.png")
    danren1.convert()
    duoren = pygame.image.load("./bwc/duoren.png")
    duoren.convert()
    duoren1 = pygame.image.load("./bwc/duoren1.png")
    duoren1.convert()
    tuichu = pygame.image.load("./bwc/tuichu.png")
    tuichu.convert()
    tuichu1 = pygame.image.load("./bwc/tuichu1.png")
    tuichu1.convert()
    screen1.blit(beijing, (-200, -100))
    screen1.blit(jiemian, (10, 10))
    pygame.mixer.music.play(loops=-1)
    n1 = True
    while n1:

        clock.tick(30)
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        if 630 <= x1 <= 840 and 80 <= y1 <= 110:
            screen1.blit(danren1, (600, 30))
            if buttons[0]:
                n1 = False
        elif 630 <= x1 <= 840 and 250 <= y1 <= 280:
            screen1.blit(duoren1, (600, 200))
        elif 630 <= x1 <= 840 and 420 <= y1 <= 450:
            screen1.blit(tuichu1, (600, 370))
            if buttons[0]:
                pygame.quit()
                exit()
        else:
            screen1.blit(danren, (600, 30))
            screen1.blit(duoren, (600, 200))
            screen1.blit(tuichu, (600, 370))

        screen.blit(screen1, (0, 0))
        pygame.display.update()
        # define a variable to control the main loop
        for event in pygame.event.get():
            # 判断事件类型是否是退出事件
            if event.type == pygame.QUIT:
                print("游戏退出...")
                # quit 卸载所有的模块
                pygame.quit()
                # exit() 直接终止当前正在执行的程序
                exit()
    screen.blit(screen2, (0, 0))
    pygame.display.flip()
    n2 = True
    while n2:
        clock.tick(30)
        screen.blit(screen2, (0, 0))
        screen2.blit(jiemian, (10, 10))
        pygame.display.update()
        for event in pygame.event.get():
            # 判断事件类型是否是退出事件
            if event.type == pygame.QUIT:
                print("游戏退出...")
                # quit 卸载所有的模块
                pygame.quit()
                # exit() 直接终止当前正在执行的程序
                exit()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)


if __name__ == "__main__":
    # call the main function
    main()
