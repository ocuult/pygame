import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16);
font_height = font.get_linesize()
# event_text = []

while True:

    event = pygame.event.wait()
    event_text=str(event)
    # event_text.append(str(event))
    #获得时间的名称
    # event_text = event_text[-SCREEN_SIZE[1]//font_height:]
    #这个切片操作保证了event_text里面只保留一个屏幕的文字
    #由于除法/自动产生的类型是浮点型，因此出现上述错误，修正方法为，将/更改为//
    if event.type == QUIT:
        exit()

    screen.fill((255, 255, 255))

    y = SCREEN_SIZE[1]-font_height
    #找一个合适的起笔位置，最下面开始但是要留一行的空
    # for text in reversed(event_text):
    screen.blit( font.render(event_text, True, (0, 0, 0)), (30, y) )
        #以后会讲
    y-=font_height
        #把笔提一行

    pygame.display.update()