from random import choice 

class RandomWalk:
    """A class to generate random walks"""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""

        self.num_points=num_points

        # All walks start at (0,0)
        self.x_val= [0] #default empty list
        self.y_val= [0] #default empty list 

    """ To make random decisions, we'll store possible moves in a list and use the choice() method 
    from the random module, to decide which move to make each time a step is taken"""

    # CHOSING DIRECTIONS 
    #fill_walk() will fill the walk with points and determine the direction of each step
    def fill_walk(self):
        """Calculate all points in the walk"""

        #keep taking steps until the walk reaches the desired length which is num_points value 
        while len(self.x_val) < self.num_points:
            #decide which direction to go and how far to go in that direction
            x_direction= choice([1,-1]) # choice is a x value number between 1 and -1 for direction [1 -> right] and [-1 -> left]
            x_distance= choice([0,1,2,3,4]) 
            x_step= x_direction * x_distance #length of each step

            y_direction= choice([1,-1])
            y_distance= choice([0,1,2,3,4])
            y_step= y_direction * y_distance # length of each step

            # reject moves that go nowhere
            if x_step==0 and y_step==0:
                continue

            #calculate the new position 
            x= self.x_val[-1] + x_step
            y= self.y_val[-1] + y_step


            self.x_val.append(x)
            self.y_val.append(y)

