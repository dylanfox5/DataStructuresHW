##Dylan Fox

import turtle
import time
print(turtle.screensize())
##dfox = Turtle()

##dfox.forward(100)
##dfox.left(30)
##dfox.forward(100)


#Create a simulation that predicts what turtle will win a race
#Racerone -  average joe
#Eugene - runs 15% faster than an average turtle, but must wait .5 second
#to turn
#Blaze - retired, but runs at 40% increased speed
#Zeus the Lightning Racer - 50% faster turns, default speed

class RacingTurtle:

    def __init__(self, speed, turnDelay, name):

        self.name = name
        self.turt = turtle.Turtle()
        self.speed = speed
        self.turnDelay = 0.3 + turnDelay

    def getX(self):

        return self.turt.xcor()

    def getY(self):

        return self.turt.ycor()

    def forward(self):
        """Moves the turtle forward speed * distance"""

        self.turt.forward(1)

    def turnRight(self, degrees):

        self.turt.right(degrees)
        time.sleep(self.turnDelay)

    def turnLeft(self, degrees):

        self.turt.left(degrees)
        time.sleep(self.turnDelay)



racerone = RacingTurtle(0, 0, "Racer One")
eugene = RacingTurtle(15, 0.5, "Eugene 'The Machine' Topps")
blaze = RacingTurtle(40, 1, "Blaze")
zeus = RacingTurtle(0, -.15, "Zeus the Lightning Turtle")

racers = [eugene, racerone, blaze, zeus]

##eugene.turt.penup()
##eugene.turt.sety(150)
##eugene.turt.pendown()

##blaze.turt.penup()
##blaze.turt.sety(-150)
##blaze.turt.pendown()
##
##zeus.turt.penup()
##zeus.turt.sety(-300)
##zeus.turt.pendown()

raceTest = [100, 90, 100, -90, 100]
ovalRace = [100, -90, 100, -90, 200, -90, 100, -90, 100]


def runRace(rt, track):

    time.clock()
    startTime = time.clock()
    counter = 0

    for distance in track:
        if counter % 2 == 0:
            runForward(distance, rt)

        else:
                rt.turnRight(distance)

        counter += 1

    endTime = time.clock()

    return endTime - startTime

def runForward(dist, rt):
    distance = int(dist * (1 - rt.speed/100))
    for i in range(distance):
        rt.forward()

def reposRacers(racelist):

    currentRacer = 0
    startpos = (len(racers) * 250 - (len(racers)) * 125) * -1
    
    for racer in racelist:
        racer.turt.penup()
        racer.turt.setx(startpos + (125 * currentRacer) )
        racer.turt.pendown()
        currentRacer += 1
    

turtle.screensize(len(racers) * 250, 300)

reposRacers(racers)

for racer in racers:
    print(racer.name, runRace(racer, ovalRace))
