#Dylan Fox
#Doctor's Office Simulation
#https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects

import random

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
        self.treatmentTime = random.randint(15, 20) 
        self.timeEnteredExamRoom = 0

def simulate():

    """Simulation asks for number of patients and doctors (examRooms) based
       on user input. The simulation runs until all patients have been treated.
       All patients enter the waitingRoom and the nurse transfers one patient
       at a time to the triageRoom. If there are any examRoom openings, the
       patient is moved to an examRoom. The patiens is removed once their
       treatment time has expired. AverageWaitTime is printed at the end."""

    numberOfPatients = eval(input("How many patients?"))
    examRoomSize = eval(input("How many doctors?"))
    
    patients = numberOfPatients
    patientsTreated = 0
    minute = 0
    averageWaitTime = 0
    for i in range(numberOfPatients): 
            waitingRoom.append(Patient(minute+1))
            
    while numberOfPatients != 0: #loops until 0 patients 
        print("Minute", minute+1)

        if len(waitingRoom) > 0:           
            for i in range(len(waitingRoom)):
                callNurse()
                break
        else:
            pass
           
        if examRoomSize > 0 and len(triageRoom) > 0: #check any examRoom openings
            nextPatient = triageRoom.pop(0)
            examRoom.append(nextPatient) #adds patient to examRoom
            nextPatient.timeEnteredExamRoom = minute+1
            examRoomSize -= 1
            averageWaitTime += (minute+1)

        for p in examRoom: #checks if treatmentTime has expired
            if (minute - p.timeEnteredExamRoom) >= p.treatmentTime-1:
                examRoom.remove(p)
                patientsTreated += 1
                numberOfPatients -= 1
                examRoomSize += 1
        
        print("Patients in Exam Room:")
        for p in examRoom:
            print(p.name, "Treatment Time:", p.treatmentTime,"Time entered Exam Room:", p.timeEnteredExamRoom)

        print("\nPatients in Triage Room:")
        for p in triageRoom:
            print(p.name, "Triage Number:", p.triageNumber)

        print("\nPatients in Waiting Room:")
        for p in waitingRoom:
              print(p.name)
        print("\n")

        minute += 1
        
    print("Patients Treated:", patientsTreated)
    print("Average Wait Time:", averageWaitTime/patients)

simulate()

