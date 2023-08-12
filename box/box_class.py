import random
from collections import Counter

class Box:

    def __init__(self, textures = {'smooth':0.35, 'not smooth': 0.65}, colors = {'red':0.5, 'green':0.3, 'blue':0.2}, num_balls = 1000):
        """
        Initializes a Box instance with specified texture and color settings
        
        Args:
            textures (dict): dictionary of possible ball textures with corresponding probability weights
            colors (dict): dictionary of possible ball colors with corresponding probability weights
            num_balls (int): total number of balls in Box
        """
        self.balls = []

        # Extract textures and colors values from dictionaries
        self.textures_val = list(textures.keys())
        self.colors_val = list(colors.keys())

        # Extract textures and colors weights from dictionaries
        self.textures_wts = list(textures.values())
        self.colors_wts = list(colors.values())
        
        # Initialize a dictionary to track frequencies and total number of all types of balls 
        self.ball_freq = {(texture, color): [0,0] for texture in self.textures_val for color in self.colors_val}

        for i in range(num_balls):
            texture = random.choices(self.textures_val, weights=self.textures_wts)[0]
            color = random.choices(self.colors_val, weights=self.colors_wts)[0]
            self.balls.append((texture, color))
            self.ball_freq[(texture, color)][1] += 1


        

    def get_ball(self):
        return random.choice(self.balls)

    def print_results(self, iters):

        for _ in range(iters):
            ball = self.get_ball()
            self.ball_freq[ball][0] += 1

        # Calculates the probabilities of each ball combination
        for ball in self.ball_freq.keys():
            texture, color = ball
            count = self.ball_freq[ball][0]
            number = self.ball_freq[ball][1]
            probability = (count / iters) * 100

            print(f"there are {number} balls with {texture} texure and {color} color")
            print(f"Probability of balls with {texture} texure and {color} color: {probability:.2f}%")
