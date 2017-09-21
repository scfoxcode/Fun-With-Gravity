class DynamicBody():
    """ A dynamic body is used to represent an object that
    is affected by forces in the world. They have no gravity of their own
    but are effected by the mass of LockedBodies """
    
    def __init__(self, position=(0,0), velocity=(0, 0), radius=2):
        self.position = position
        self.velocity = velocity
        self.radius   = radius