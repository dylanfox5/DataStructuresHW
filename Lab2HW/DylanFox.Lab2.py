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

def callNurse():
    triageRoom.append(waitingRoom.pop(0)) #move patient from waiting room to triage room
    triageRoom.sort(key=lambda Patient: Patient.triageNumber) #sorts based on triageNumber

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

    time.clock()

    minute = 1
    while minute != 10:
        print("Minute", minute)
        for i in range(6):
            waitingRoom.append(Patient(int(time.clock())))

        for i in range(len(waitingRoom)):
                    callNurse()

        if len(examRoom) < examRoomSize:
            for i in range(len(examRoom), examRoomSize):
                nextPatient = triageRoom.pop(0)
                examRoom.append(nextPatient)
                nextPatient.timeEnteredExamRoom = minute

        print("Patients in Exam Room:")
        for p in examRoom:
            print(p.name, "Treatment Time:", p.treatmentTime, p.timeEnteredExamRoom)

        print("\nPatients in Triage Room:")
        for p in triageRoom:
            print(p.name, "Triage Number:", p.triageNumber)

        print("\nPatients in Waiting Room:")
        for p in waitingRoom:
              print(p.name)

        for p in examRoom:
            if (minute - p.timeEnteredExamRoom) >= p.treatmentTime:
                examRoom.remove(p)
                
        print("\n")
        #time.sleep(10)
        
        minute += 1


simulate()
