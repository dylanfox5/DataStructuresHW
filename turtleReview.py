##Dylan Fox

import turtle
import time

##dfox = Turtle()

##dfox.forward(100)
##dfox.left(30)
##dfox.forward(100)


#Create a simulation that predicts what turtle will win a race
#Racerone -  average joe
#Eugene - runs 15% faster than an average turtle, but must wait .5 second
#to turn
#Blaze - retired, but runs at 40% increased speed

class RacingTurtle:

    def __init__(self, speed, turnDelay, name):

        self.name = name
        self.turt = turtle.Turtle()
        self.speed = 20 * (1 + (speed/100))
        self.turnDelay = 0 + turnDelay

    def getX(self):

        return self.turt.xcor()

    def getY(self):

        return self.turt.ycor()

    def forward(self, distance):
        """Moves the turtle forward speed * distance"""

        self.turt.forward(distance * self.speed)

    def turnRight(self, degrees):

        self.turt.right(degrees)
        time.sleep(self.turnDelay)

    def turnLeft(self, degrees):

        self.turt.left(degrees)
        sleep(self.turnDelay)

racerone = RacingTurtle(0, 0, "Racer One")
eugene = RacingTurtle(15, 0.5, "Eugene 'The Machine' Topps")

eugene.turt.penup()
eugene.turt.sety(150)
eugene.turt.pendown()

time.clock()
eugeneStartTime = time.clock()

#leg 1
while (eugene.getX() < 100):
       eugene.forward(1)


#turn
eugene.turnRight(90)

#leg 2
while (eugene.getY() > 50):
       eugene.forward(1)

eugeneEndTime = time.clock()

racerStartTime = time.clock()
#leg 1
while (racerone.getX() < 100):
       racerone.forward(1)

#turn
racerone.turnRight(90)

#leg 2
while (racerone.getY() > -100):
       racerone.forward(1)

racerEndTime = time.clock()

print(eugeneEndTime - eugeneStartTime)
print(racerEndTime - racerStartTime)
