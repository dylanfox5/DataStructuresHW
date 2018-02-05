#Dylan Fox
#Doctor's Office Simulation
#https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects

import random
import time

waitingRoom = []
triageRoom = []
triageRoomSize = 15
names = ["joey", "bobby", "susann", "loretta", "grant",\
         "jenny", "billy", "tucker", "cletus", "hunter",\
         "gunner", "rose", "amy", "charlette", "duke", \
         "ricky", "bo", "luke", "jesse"]

examRoom = []
examRoomSize = 6

def callNurse():
    triageRoom.append(waitingRoom.pop(0)) #move patient from waiting room to triage room
    triageRoom.sort(key=lambda Patient: Patient.triageNumber) #sorts based on triageNumber (See url above for lambda function)

class Patient:

    def __init__(self, time):
        
        self.triageNumber = random.randint(1,100)
        self.name = names[random.randint(0,len(names)-1)]\
                    + " " + names[random.randint(0,len(names)-1)]
        self.arrivalTime = time
        self.treatmentTime = random.randint(1, 5) 
        self.timeEnteredExamRoom = 0
        
    def exit(self, patient): #remove patient from simulation
        examRoom.remove(patient)

def simulate():

    """Simulation adds 6 patients every minute,
        one minute is equal to one loop through the while statement,
        patients are added to the waitingRoom, then sorted based on
        triageNumber in the triageRoom, based on any open examRooms
        the patients from the triageRoom are added to an examRoom,
        once patient's treatmentTime has expired they are removed."""

    numberOfPatients = eval(input("How many patients?"))
    examRoomSize = eval(input("How many doctors?"))
    
    patientsTreated = 0
    minute = 0 #used to simulate real minutes without having to wait
    while numberOfPatients != 0: #number of minutes to simulate
        print("Minute", minute+1)
        
        for i in range(numberOfPatients): 
            waitingRoom.append(Patient(minute+1))

        #if len(triageRoom) < triageRoomSize: #max of 15 patients in triageRoom

        callNurse()
##            if len(waitingRoom) < triageRoomSize:
##                for i in range(len(triageRoom), len(waitingRoom)): #moves to triageRoom + triages patients
##                    callNurse()
##            elif len(waitingRoom) > triageRoomSize:
##                for i in range(len(triageRoom), triageRoomSize): #moves to triageRoom + triages patients
##                    callNurse()

            
        if len(examRoom) < examRoomSize: #check any examRoom openings
            for i in range(len(examRoom), examRoomSize):
                nextPatient = triageRoom.pop(0)
                examRoom.append(nextPatient) #adds patient to examRoom
                nextPatient.timeEnteredExamRoom = minute+1

        for p in examRoom: #checks if treatmentTime has expired
            if (minute - p.timeEnteredExamRoom) >= p.treatmentTime-1:
                examRoom.remove(p) #removes patient from examRoom
                patientsTreated += 1
                numberOfPatients -= 1
        
        print("Patients in Exam Room:")
        for p in examRoom:
            print(p.name, "Treatment Time:", p.treatmentTime,"Time entered Exam Room:", p.timeEnteredExamRoom)

        print("\nPatients in Triage Room:")
        for p in triageRoom:
            print(p.name, "Triage Number:", p.triageNumber)

        print("\nPatients in Waiting Room:")
        for p in waitingRoom:
              print(p.name)
                
        print("Patients Treated:", patientsTreated)
        print("\n")

        minute += 1

simulate()
