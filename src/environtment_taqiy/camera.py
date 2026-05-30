class CameraManager:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0
        self.speed = 5
        self.mode = "normal"  # "normal" atau "closeup"

    def set_target(self, x, y, mode):
        self.target_x = x
        self.target_y = y
        self.mode = mode

    def update(self):
        # Smooth transition
        if abs(self.x - self.target_x) > self.speed:
            if self.x < self.target_x:
                self.x += self.speed
            else:
                self.x -= self.speed

        if abs(self.y - self.target_y) > self.speed:
            if self.y < self.target_y:
                self.y += self.speed
            else:
                self.y -= self.speed

    def get_position(self):
        return (self.x, self.y)