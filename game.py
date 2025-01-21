import arcade

SCREEN_WIDHT = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong Game'

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', scale = 0.1)
        self.change_x = 3
        self.change_y = 3
        
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDHT:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y
class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', scale = 1)
    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDHT:
            self.right = SCREEN_WIDHT
        if self.left <= 0:
            self.left = SCREEN_WIDHT
class Game(arcade.Window):
    def __init__(self, widht, height, title):
        super().__init__(widht, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()
        
    def setup(self):
        self.bar.center_x = SCREEN_WIDHT / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDHT / 2
        self.ball.center_y = SCREEN_HEIGHT / 3
    
    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()
        
    def update(self, delta_time):
        self.ball.update()
        self.bar.update()
        
    def on_mouse_motion(self, x, y, dx, dy):
        if x < 0:
            self.bar.change_x = 5
        
        
            
if __name__ == "__main__":
    window = Game(SCREEN_WIDHT, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()