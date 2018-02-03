
#Dylan Fox
#Doctor's Office Simulation

import random
import time

waitingRoom = []
triageRoom = []
names = ["joey", "bobby", "susann", "loretta", "grant",\
         "jenny", "billy", "tucker", "cletus", "hunter",\
         "gunner", "rose", "amy", "charlette", "duke", \
         "ricky", "bo", "luke", "jesse"]

examRoom = []
examRoomSize = 6
doctors = 6

def callNurse():
    #move patient from waiting room to triage room
    triageRoom.append(waitingRoom.pop(0))
    sorted(triageRoom, key=patient.triageNumber)

class Patient:

    def __init__(self, time):
        
        self.triageNumber = random.randint(1,100)
        self.name = names[random.randint(0,len(names)-1)]\
                    + " " + names[random.randint(0,len(names)-1)]
        self.arrivalTime = time
        self.treatmentTime = random.randint(15, 20)
        self.timeInExamRoom = 0
        
    def exit(self):
        pass
        #remove patient from simulation

def simulate():

    simulationTime = time.clock()
    for x in range(6):
                waitingRoom.append(Patient(time.clock()))

    for x in range(len(waitingRoom)):
        callNurse()

    for p in triageRoom:
        print(p.name)

##    while simulationTime < 600:
##        print(simulationTime)
##    
##        if simulationTime % 60 == 0:
##            for x in range(5):
##                waitingRoom.append(Patient(time.clock()))
##
##        if len(examRoom) != examRoomSize:
##            while len(examRoom) != examRoomSize:
##                callNurse()
##                nextPatient = triageRoom.pop(0)
##                examRoom.append(nextPatient)
##                nextPatient.timeInExamRoom = time.clock()
##
##        else:
##            for p in examRoom:
##               if p.timeInExamRoom >= p.treatmentTime:
##                    p = patientTreated
##                    examRoom.remove(patientTreated)

simulate()
