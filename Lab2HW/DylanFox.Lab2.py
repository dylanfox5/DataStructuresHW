#Dylan Fox
#Doctor's Office Simulation

import random

waitingRoom = []
traigeRoom = []
names = ["joey", "bobby", "susann", "loretta", "grant",\
         "jenny", "billy", "tucker", "cletus", "hunter",\
         "gunner", "rose", "amy", "charlette", "duke", \
         "ricky", "bo", "luke", "jesse"]

examRoom = []
examRoomSize = 6
doctors = 6

class Physician:

    def __init__(self, name):

        self.name = name #Physician 1-6

    def examination(): #sets random minutes 15-20
        minutes = random.randint(15,20)

def callNurse():
    #move patient from waiting room to triage room
    triageRoom.append(waitingRoom.pop(0))
    sort(triageRoom, key=patient.traigeNumber)

class Nurse: #function

    def __init__(self, name):

        self.name = name #nurse

    def getPatient(): #get patient to triage

        
    def sendPatient(): #send patient to waiting room for physician
        pass

class Patient:

    def __init__(self, time):
        self.triageNumber = random.randint(100)
        self.name = names[random.randint(len(names)-1)]\
                    + " " + names[random.randint(len(names)-1)]
        self.arrivalTime = time
        self.treatmentTime = random.randint(15, 20)

        
    def exit(self):
        #remove patient from simulation

class ExamRoom:
    
    def __init__(self, Physician):

        self.Physician = Physician #which physician is at each examroom
        self.runTime = 0
        self.Patient = None #current patient in examroom

    def addPatient(self, WaitingRoom): #add patient to examroom

        self.waitingList2.pop(0)
        
    def removePatient(self): #remove patient from examroom

        
    def timeRemaining():
        
        return self.runTime


    
class WaitingRoom:

    def __init__(self):

        self.waitingList1 = []
        self.waitingList2 = []

    def addPatients(self, patient): #keep track of patients before nurse

        self.waitingList1.append(patient)

    def removePatients(self): #remove patiens waiting for nurse

        return self.waitingList1.pop(0)
        
    def addPatientsTwo(self, patient): #add patients waiting for physician

        self.waitingList2.append(patient)

    def removePatientsTwo(self): #remove patients waiting for physician

        return self.waitingList2.pop(0)
