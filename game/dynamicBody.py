from vec2D import Vec2D

class DynamicBody():
    """ A dynamic body is used to represent an object that
    is affected by forces in the world. They have no gravity of their own
    but are effected by the mass of LockedBodies """
    
    def __init__(self, position=Vec2D(0,0), velocity=Vec2D(0, 0), radius=3):
        self.gConstant = 10
        self.position  = position
        self.velocity  = velocity
        self.radius    = radius
    
    def update(self, lockedBodies, dt):
        """ Updates velocity and applies to position based on all
        the locked bodies in the system """
        for body in lockedBodies:
            rawDisplace = body.getWorldPosition() - self.position
            direction = Vec2D.normalize(rawDisplace)
            displacementSquared = Vec2D.magnitudeSquared(rawDisplace)
            acceleration = dt*self.gConstant*body.mass/max(1, displacementSquared)
            self.velocity = self.velocity + Vec2D.scale(direction, acceleration)
            self.position = self.position + self.velocity

        