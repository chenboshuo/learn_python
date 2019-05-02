import sys

import pygame

def check_events():
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    '''更新屏幕上的图像,并切换到新屏幕'''
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)  # 这个方法只接受一种实参: 一种颜色
    ship.biltme()

    # 让最近的屏幕可见
    pygame.display.flip()