#Dylan Fox
#Doctor's Office Simulation

import random

class Physician:

    def __init__(self, name, minutes):

        self.name = name
        self.minutes = random.randint(15,20)

    def setMinutes(self, minutes):

        self.minutes = minutes

    def getMinutes(self):

        return self.minutes

    def setRandMins(self):

        self.setMinutes(random.randint(15,20))

class ExamRoom:
    
    def __init__(self, name, physicianName, isFull, Patient):

        self.name = name
        self.physicianName = physicianName
        self.isFull = isFull
        self.Patient = Patient

    def getIsFull(self):

        return self.isFull

    def setIsFull(self, isFull):

        self.isFull = isFull
##
##class Nurse:
##
##    def __init__(self):


class Patient:

    def __init__(self, triaged, triageLevel, waitingRoom, ExamRoom):

        self.traiged = triaged
        self.triageLevel = triageLevel
        self.waitingRoom = waitingRoom
        self.ExamRoom = ExamRoom


physician1 = Physician("Physician 1", None)
physician2 = Physician("Physician 2", None)
physician3 = Physician("Physician 3", None)
physician4 = Physician("Physician 4", None)
physicians = [physician1, physician2, physician3, physician4]

patient1 = Patient(False, None, False, None)

exam1 = ExamRoom("ExamRoom 1", "", False, None)
exam2 = ExamRoom("ExamRoom 2", "", False, None)
exam3 = ExamRoom("ExamRoom 3", "", False, None)
exam4 = ExamRoom("ExamRoom 4", "", False, None)
examrooms = [exam1, exam2, exam3, exam4]


def simulate():

    for physician in physicians:

        for examroom in examrooms:

            if examroom.physicianName is "":
                examroom.physicianName = physician.name
                break
        
    for examroom in examrooms:
       print(examroom.name, examroom.physicianName)

simulate()
