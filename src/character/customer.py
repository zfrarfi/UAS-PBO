import pygame
from character.character import Character

class Customer(Character):
    def __init__(self, x_position, y_position):
        super().__init__(x_position, y_position, name = "Customer", bubble_chat = "", speed = 0.5)
        
        self.front_frames = [
            pygame.image.load("assets/image/character/customer/cust_front_frame1.png").convert_alpha(),
            pygame.image.load("assets/image/character/customer/cust_front_frame2.png").convert_alpha()
        ]

        self.back_frames = [
            pygame.image.load("assets/image/character/customer/cust_back_frame1.png").convert_alpha(),
            pygame.image.load("assets/image/character/customer/cust_back_frame2.png").convert_alpha()
        ]

        self.left_frames = [
            pygame.image.load("assets/image/character/customer/cust_left_frame1.png").convert_alpha(),
            pygame.image.load("assets/image/character/customer/cust_left_frame2.png").convert_alpha()
        ]

        self.right_frames = [
            pygame.image.load("assets/image/character/customer/cust_right_frame1.png").convert_alpha(),
            pygame.image.load("assets/image/character/customer/cust_right_frame2.png").convert_alpha()
        ]
        
        # Scale frames maintaining aspect ratio
        target_width = 80
        for frame_list in [
            self.front_frames,
            self.back_frames,
            self.left_frames,
            self.right_frames
        ]:
            for i in range(len(frame_list)):
                original_width = frame_list[i].get_width()
                original_height = frame_list[i].get_height()
                scale = target_width / original_width
                new_height = max(1, int(original_height * scale))
                frame_list[i] = pygame.transform.smoothscale(
                    frame_list[i],
                    (target_width, new_height)
        )
                
        self.direction = "front"
        self.animation_index = 0
        self.animation_timer = 0
        self.animation_delay = 10
        
        self.image = self.front_frames[0]

        self.rect = self.image.get_rect(
            center=(x_position, y_position)
        )
        self.state = "to_cashier"
        self.cashier_x = 950
        self.cashier_y = 270

        self.seat_x = 350
        self.seat_y = 500
        

        
    def animate(self):

        self.animation_timer += 1

        if self.animation_timer >= self.animation_delay:

            self.animation_index += 1

            if self.animation_index >= 2:
                self.animation_index = 0

            self.animation_timer = 0
            
    def get_current_image(self):

        if self.direction == "front":
            return self.front_frames[self.animation_index]

        elif self.direction == "back":
            return self.back_frames[self.animation_index]

        elif self.direction == "left":
            return self.left_frames[self.animation_index]

        else:
            return self.right_frames[self.animation_index]
        
    def update(self):

        if self.state == "to_cashier":

            arrived = self.move_to(
                self.cashier_x,
                self.cashier_y
            )

            if arrived:

                self.state = "ordering"

                self.wait_timer = 180

        elif self.state == "ordering":

            self.wait_timer -= 1

            if self.wait_timer <= 0:

                self.state = "to_seat"

        elif self.state == "to_seat":

            arrived = self.move_to(
                self.seat_x,
                self.seat_y
            )

            if arrived:

                self.state = "sitting"

        self.animate()

        self.image = self.get_current_image()

        self.rect.center = (
            self.x_position,
            self.y_position
        )
        
    def move_to(self,target_x,target_y):

        if abs(self.x_position - target_x) > self.speed:

            if self.x_position < target_x:
                self.x_position += self.speed
                self.direction = "right"

            else:
                self.x_position -= self.speed
                self.direction = "left"

        elif abs(self.y_position - target_y) > self.speed:

            if self.y_position < target_y:
                self.y_position += self.speed
                self.direction = "front"

            else:
                self.y_position -= self.speed
                self.direction = "back"

        else:
            return True

        return False

    def draw(self, screen, camera):

        screen.blit(
            self.image,
            (
                self.rect.x - camera[0],
                self.rect.y - camera[1]
            )
        )