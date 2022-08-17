import pygame


class FrogPlayer(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # This variable is to keep track of everytime we animate our frog
        # so that it animates only while its function is called
        # it will be set to True in the animation method will go back to False at the end of it
        self.is_animating = False
        self.sprites = []
        # This is bringing in our images and appending them to our above list variable
        for image in range(1, 11):
            self.sprites.append(pygame.transform.scale(pygame.image.load(f'frog_pics/attack_{image}.png').convert_alpha(), (66 * 7, 22 * 7)))
        # This is like our place of the current sprite so that we know which frame is being displayed
        self.current_sprite = 0
        # This keeps track of which image is being displayed based off of the current_sprite
        # current_sprite will be incremented by +1 later on to iterate through the images *
        self.image = self.sprites[self.current_sprite]

        # The next 2 lines draw a rectangle around our sprite so we can move it and position it later
        self.rect = self.image.get_rect()
        # This controls the place on the sprite from where we want to position it
        # (bottomleft, bottomleft, topright, bottomright)
        self.rect.bottomleft = [pos_x, pos_y]

    # This function will animate our frog by looping through its provided images
    def animate(self):
        self.is_animating = True

    '''
        To animate our frog we need the update function for our FrogPlayer class
        The update method is predefined in the Sprite class in pygame module
        There is no need to use this built in method it is used as a "hook" that you can override -> pygame docs
        For our case we are using this function to reset our frog's frame everytime we are done animating it
        This will also be looping in main to constantly check when to update our sprite
    '''

    def get_keys(self):
        # So that we constantly get a mouse pos
        mx, my = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
        elif keys[pygame.K_d]:
            self.rect.x += 5    

    def update(self, speed=0.2):
        self.get_keys()
        if self.is_animating:
            # This increments the current_sprite image by one to produce an animation *
            # We can use the int() function to increment over the images slowly so that we can get a smoother animation
            # BUT we will call the int() func at the end bc we need image to be updates and not current sprite
            # (also it won't work)
            # We can also set the parameter manually in our main code when we call the function
            self.current_sprite += speed
            # We need this to go back to the first INDEX of the image after the last one in the list has been reached
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                # We need to stop the animation by setting is_animating_right to False
                # We do it under this if statement because first we want to loop through every image then
                # We will set the variable to False
                self.is_animating = False
            # We also need to update the current image being displayed onto the screen
            self.image = self.sprites[int(self.current_sprite)]
