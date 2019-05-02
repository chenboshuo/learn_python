import pygame

class Ship():

    def __init__(self, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen

        # 加载飞船并获取其外界矩形
        self.imag = pygame.image.load('images/ship.bmp') # 函数返回一个表示飞船外形的surface
        self.rect = self.imag.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False

    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right:
            self.rect.centerx += 1

    def biltme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.imag, self.rect)