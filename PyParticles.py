import math
import random
import Menu

def addVectors(vector1,vector2):
    angle1,length1=vector1
    angle2,length2= vector2
    
    x=math.sin(angle1)*length1+math.sin(angle2)*length2
    y=math.cos(angle1)*length1+math.cos(angle2)*length2
    
    angle  = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return (angle, length)

def collide(p1, p2):
    """ Tests whether two particles overlap
        If they do, make them bounce
        i.e. update their angle, speed and position """
    
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    dist = math.hypot(dx, dy)
    if dist < p1.size + p2.size:
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        total_mass = p1.mass + p2.mass

        (p1.angle, p1.speed) = addVectors((p1.angle, p1.speed*(p1.mass-p2.mass)/total_mass), (angle, 2*p2.speed*p2.mass/total_mass))
        (p2.angle, p2.speed) = addVectors((p2.angle, p2.speed*(p2.mass-p1.mass)/total_mass), (angle+math.pi, 2*p1.speed*p1.mass/total_mass))
        elasticity = p1.elasticity * p2.elasticity
        p1.speed *= elasticity
        p2.speed *= elasticity

        overlap = 0.5*(p1.size + p2.size - dist+1)
        p1.x += math.sin(angle)*overlap
        p1.y -= math.cos(angle)*overlap
        p2.x -= math.sin(angle)*overlap
        p2.y += math.cos(angle)*overlap

class Particle:
    """ A circular object with a velocity, size and mass """
    
    def __init__(self,position, size, mass=1):
        self.x,self.y=position
        self.size = size
        self.colour = (Menu.color('Happy'))
        self.thickness = 0
        self.speed = 0
        self.angle = 0
        self.mass = mass
        self.drag = 1
        self.elasticity = 0.9

    def move(self):
        """ Update position based on speed, angle
            Update speed based on drag """

        #(self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= self.drag
        
    def mouseMove(self, x, y):
        """ Change angle and speed to move towards a given point """

        dx = x - self.x
        dy = y - self.y
        self.angle = 0.5*math.pi + math.atan2(dy, dx)
        self.speed = math.hypot(dx, dy) * 0.1

class Environment:
    """ Defines the boundary of a simulation and its properties """
    
    def __init__(self,positionTwo):
        self.width, self.height= positionTwo
        self.particles = []
        
        self.colour = (255,255,255)
        self.mass_of_air = 0.2
        self.elasticity = 0.75
        self.acceleration = None
        
    def addParticles(self, n=1, **kargs):
        """ Add n particles with properties given by keyword arguments """
        
        for i in range(n):
            size = kargs.get('size', random.randint(10, 80))
            mass = kargs.get('mass', random.randint(100, 10000))
            x = kargs.get('x', random.uniform(size, self.width - size))
            y = kargs.get('y', random.uniform(size, self.height - size))

            particle = Particle((x, y), size, mass)
            particle.speed = kargs.get('speed', random.random())
            particle.angle = kargs.get('angle', random.uniform(0, math.pi*2))
            particle.colour = kargs.get('colour', (Menu.color('Happy')))
            particle.drag = (particle.mass/(particle.mass + self.mass_of_air)) ** particle.size

            self.particles.append(particle)

    def update(self):
        """  Moves particles and tests for collisions with the walls and each other """
        
        for i, particle in enumerate(self.particles):
            particle.move()
            if self.acceleration:
                particle.accelerate(self.acceleration)
            self.bounce(particle)
            for particle2 in self.particles[i+1:]:
                collide(particle, particle2)

    def bounce(self, particle):
        """ Tests whether a particle has hit the boundary of the environment """
        
        if particle.x > self.width - particle.size:
            particle.x = 2*(self.width - particle.size) - particle.x
            particle.angle = - particle.angle
            particle.speed *= self.elasticity

        elif particle.x < particle.size:
            particle.x = 2*particle.size - particle.x
            particle.angle = - particle.angle
            particle.speed *= self.elasticity

        if particle.y > self.height - particle.size:
            particle.y = 2*(self.height - particle.size) - particle.y
            particle.angle = math.pi - particle.angle
            particle.speed *= self.elasticity

        elif particle.y < particle.size:
            particle.y = 2*particle.size - particle.y
            particle.angle = math.pi - particle.angle
            particle.speed *= self.elasticity

    def findParticle(self, x, y):
        """ Returns any particle that occupies position x, y """
        
        for particle in self.particles:
            if math.hypot(particle.x - x, particle.y - y) <= particle.size:
                return particle
        return None