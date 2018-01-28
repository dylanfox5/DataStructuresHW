#Dylan Fox
#Doctor's Office Simulation

import random

class Physician:

    def __init__(self, name):

        self.name = name #Physician 1-6

class Nurse:

    def __init__(self, name):

        self.name = name #nurse

class Patient:

    def __init__(self, name, triaged, triageLevel, waitingRoom, ExamRoom, minutes):

        self.name = name
        self.triaged = triaged #boolean: True=yes; False=no
        self.triageLevel = triageLevel #scale of 1-10? based on urgency
        self.waitingRoom = waitingRoom #1 or 2; 1=1st waiting room, 2=2nd waiting room
        self.ExamRoom = ExamRoom #Examroom patient is currently in
        self.minutes = random.randint(15,20) #random num of mins 

class ExamRoom:
    
    def __init__(self, name, physicianName, isFull, Patient):

        self.name = name #ExamRoom 1-6
        self.physicianName = physicianName #which physician is at each examroom
        self.isFull = isFull #boolean: true=yes; false=no
        self.Patient = Patient #current patient in examroom

class WaitingRoomOne:

class WaitingRoomTwo:


physician1 = Physician("Physician 1")
physician2 = Physician("Physician 2")
physician3 = Physician("Physician 3")
physician4 = Physician("Physician 4")
physicians = [physician1, physician2, physician3, physician4]

patient1 = Patient("Paitent 1", False, 5, 1, None, 0)
patient2 = Patient("Patient 2", False, 9, 1, None, 0)
patients = [patient1, patient2]

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
            
    urgency = 0
    for x in range(len(patients)):
        if patients[x].triageLevel > urgency:
            urgency = patients[x].triageLevel

            for examroom in examrooms:
                if examroom.Patient is None:
                    examroom.Patient = patients[x]
                    break
    
    print(patient1.minutes)    
    for examroom in examrooms:
       if examroom.Patient is not None:
           print(examroom.name, examroom.physicianName, examroom.Patient.name)
       else:
           print(examroom.name, examroom.physicianName)
    

simulate()
