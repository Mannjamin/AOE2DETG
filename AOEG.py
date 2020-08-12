import random

numTeams = '0'
boolMutators = 'N'
numMutators = '0'

civilisations = ["Aztecs", "Berbers", "Britons", "Bulgarians", "Celts", "Chinese", "Cumans", "Ethiopians", "Franks", "Goths", "Huns", "Incas", "Indians", "Italians", "Japanese", "Khmer",
                "Koreans", "Lithuanians", "Magyars", "Malay", "Malians", "Mayans", "Mongols", "Persians", "Portuguese", "Saracens", "Slavs", "Spanish", "Tatars", "Tuetons", "Turks", "Vietnamese", "Vikings"]
mutations = ["No Infrantry", "Focus Infantry", "No Archers (incl Cavalry)", "Focus Archers", "No Cavalry (incl Camels and Elephants)", "Focus Cavalry",
            "No Siege Weapons (inc bombard cannons)", "Focus Siege Weapons", "No Blacksmith Upgrades", "No Trade (incl carts/caravans)", "No Monastery", "No Castles", "No Monks"]

# Get Number of Teams
def setNumTeams():
    global numTeams
    try:
        numTeams = input("Enter number of teams: ")
        try:
            numTeams = int(numTeams)
        except ValueError:
            print("Input is not a number, try again.")
            setNumTeams()
    except SyntaxError:
        print("No input found, try again.")
        setNumTeams()

# Determine whether to use Mutators or not
def setMutators():
    global boolMutators
    boolMutators = input("Enter Y or N for Mutators: ")
    if boolMutators == 'Y':
        setNumMutators()
    elif boolMutators == 'N':
        print("No Mutators")
    else:
        print("Y or N, try again.")
        setMutators()


# Get Number of Mutators wanted.
def setNumMutators():
    global numMutators
    numMutators = input("Enter number of mutators: ")

# Print User Chosen Parametrs
def printParams():
    # Number of Teams:
    print("Number of Teams Selected: " + str(numTeams))
    # Mutators:
    print("Mutators: " + str(boolMutators))
    if boolMutators == 'Y':
        # Number of Mutators:
        print("Number of Mutators: " + str(numMutators))

# Generate User Chosen Parameters
def getParams():
    # Output chosen parameters
    for x in range(int(numTeams)):
        # Get Random Civilisation:
        chosenCiv = random.choice(civilisations)
        # Get Mutators
        if boolMutators == "Y" or "y":
            chosenMut = []
            for y in range(int(numMutators)):
                # Second Check In
                while chosenCiv == "Goths":
                    randMute = random.choice(mutations)
                    while randMute == "No Infantry":
                        randMute = random.choice(mutations)
                        if randMute != "No Infantry":
                            break
                    chosenMut.append(randMute)
                    break    
                while chosenCiv == "Incas" or "Aztecs" or "Mayans":
                    randMute = random.choice(mutations)
                    while randMute == "Focus Cavalry":
                        randMute = random.choice(mutations)
                        if randMute != "Focus Cavalry":
                            break
                    chosenMut.append(randMute)
                    break 
        if boolMutators == 'Y':
            print("Team " + str(x+1) + " [Civilisation: " + str(chosenCiv) + "] [Mutators: " + str(chosenMut) +"]")
        else:
            print("Team " + str(x+1) + " [Civilisation: " + str(chosenCiv) +"]")


# Execute Code
print("Mann's Age of Empires Civilisation Generator")

setNumTeams()
setMutators()
printParams()
getParams()

