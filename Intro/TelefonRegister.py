
#key = namn
#value = telefonnummer
telReg = {}

while True:
    namn = input("Ange namnet du vill lägga till: ")
    namn = namn.lower()
    if namn in telReg:
        print("Ops! Namnet finns redan.")
    else:
        telnr = input("Ange telefonnummret till denna personen: ")
        telReg[namn] = telnr
    if len(telReg) == 2:
        break

while True:
    namn = input("Ange ett namn du vill söka telefonnummret till: ")
    #om namnet inte finns så ska ett meddelande komma
    if namn in telReg:
        telnr = telReg[namn]
        print(f"{namn}s telefonnummer är: {telnr}")
        if len(telReg) == 2:
            break
    else:
        print("Namnet finns inte. Försök igen")
        




