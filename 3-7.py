# // Spurning 7: GOLF SCORES
holeNum = 1

while holeNum <= 18:
    par = int(input("Par of hole " + str(holeNum) + ": "))
    score = int(input("Score on hole " + str(holeNum) + ": "))

    calc = score - par
    # print("calculation: ", calc)
    if calc < -3:
        print("invalid score")
    elif calc == -3:
        print("albatross")
    elif calc == -2:
        print("eagle")
    elif calc == -1:
        print("birdie")
    elif calc == 0:
        print("par")
    elif calc == 1:
        print("bogey")
    elif calc == 2:
        print("double bogey")
    elif calc == 3:
        print("triple bogey")
    else:
        print("bad hole")

    holeNum += 1
