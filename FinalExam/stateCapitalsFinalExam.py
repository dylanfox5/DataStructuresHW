#Dylan Fox
#State Capitals Dictionary


stateCapitals = {"Des Moines":"", "Jefferson City":"", "Albany":"", "Sacramento":"", "Ausitn":"", "Lincoln":""}

def addStates(num):

    for entry in stateCapitals:
        if stateCapitals[entry] == "":
            stateCapitals[entry] = num
            break

addStates("Iowa")
addStates("Missouri")
addStates("New York")
addStates("California")
addStates("Texas")
addStates("Nebraska")

for entry in stateCapitals:
    if stateCapitals[entry] == "California":
        print(entry)
