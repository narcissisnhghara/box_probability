import random

class Box:
    def __init__(self, textures = {'smooth':0.35, 'not smooth': 0.65}, colors = {'red':0.5, 'green':0.3, 'blue':0.2}):
        """
        Initializes a Box instance with specified texture and color settings
        
        Args:
            textures (dict): dictionary of possible ball textures with corresponding probability weights
            colors (dict): dictionary of possible ball colors with corresponding probability weights
        """

        # Extract textures and colors values from dictionaries
        self.textures_val = list(textures.keys())
        self.colors_val = list(colors.keys())

        # Extract textures and colors weights from dictionaries
        self.textures_wts = list(textures.values())
        self.colors_wts = list(colors.values())

        # Initialize a dictionary to track ball frequencies
        self.ball_freq = {(texture, color): 0 for texture in self.textures_val for color in self.colors_val}

    def get_ball(self):
             
        texture = random.choices(self.textures_val, weights=self.textures_wts)[0]
        color = random.choices(self.colors_val, weights=self.colors_wts)[0]
        return texture, color

    def print_results(self, iters):

        for _ in range(iters):
            ball = self.get_ball()
            self.ball_freq[ball] += 1

        # Calculates the probabilities of each ball combination
        for ball_index, ball in enumerate(self.ball_freq.keys()):
            texture, color = ball
            count = self.ball_freq[ball]
            probability = (count / iters) * 100
            print(f"Probability of Ball-{ball_index} with {texture} texure and {color} color: {probability:.2f}%")
