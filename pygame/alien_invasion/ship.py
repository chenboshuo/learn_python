import pygame

class Ship():

    def __init__(self, ai_settings,screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船并获取其外界矩形
        self.imag = pygame.image.load('images/ship.bmp') # 函数返回一个表示飞船外形的surface
        self.rect = self.imag.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船属性中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center(小数) 更新rect 对象(整数部分)
        self.rect.centerx = self.center

    def biltme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.imag, self.rect)