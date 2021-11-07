import time
seconds = time.time()
print(f"Seconds since epoch:{seconds} ")
time.sleep(1)
print(f"Ett ögonblick")
time.sleep(1.5)

localtime = time.ctime(seconds)
print(f"Localtime: {localtime}")



import time
# pause1 = time.sleep(2)
# pause0_5 = time.sleep(0.5)

allaKonton = ["23"]
transaktionLista = []
saldo = 200
seconds = time.time()
localtime = time.ctime(seconds)

def menuA():
    menuA = ["", "****Huvudmeny****", "1. Skapa konto", "2. Administrera konto", "3. Avsluta", ""]
    for i in menuA:
        print(i)

def menuB(minKonto):
    menuB = ["", f"****Kontomeny**** - konto: {str(minKonto)}", "1. Ta ut pengar", "2. Sätt in pengar", "3. Visa Saldo", "4. Avsluta", ""]
    for i in menuB:
        print(i)
        time.sleep(0.25)

#Kallar fram menuA, och sedan matar användaren in ett val mellan 1 och 3
menuA()
val = int(input("Ange menyval: "))
#Så länge användaren inte avslutar programmet genom att trycka "3", så loopas det som finns i while loopen
while val != 3:
    
    if val == 1:
        NyKonto = (input("Ange kontonummer: "))

        if NyKonto not in allaKonton:
            allaKonton.append(NyKonto)
            print("Din konto har skapats. ")
            time.sleep(1)
        else:
            print("Denna kontonummer finns redan.")
            time.sleep(1)
    
    elif val == 2:
        minKonto = (input("Ange ditt kontonummer: "))

        if minKonto not in allaKonton:
            print("Denna kontonummer finns inte.")
            time.sleep(1)

        else:
            print("OK.")
            time.sleep(1)
            menuB(minKonto)
            val2 = int(input("Ange kontomenyval: "))
            break
    menuA()
    val = int(input("Ange menyval: "))

if val == 2:
    while val2 != 4:
        if val2 == 1:
            taUtBelopp = int(input("Ange belopp: "))
            if taUtBelopp > saldo or taUtBelopp <= 0:
                print("Du har inte så mycket pengar.")
                time.sleep(1)
            elif taUtBelopp <= saldo and taUtBelopp > 0:
                saldo = saldo - taUtBelopp
                print("Ok.")
                time.sleep(1)
                f = open("transaktion.txt", "w")
                f.write(f"Tar ut pengar: {taUtBelopp} Datum: {localtime} \n ")
                f.close()
            
        if val2 == 2:
            sattInBelopp = int(input("Ange belopp: "))
            if sattInBelopp > 0:
                saldo = saldo + sattInBelopp
                print("Ok")
                time.sleep(1)
        if val2 == 3:
            print(f"Ditt saldo är: {saldo}")
            time.sleep(1)
        
        menuB(minKonto)
        val2 = int(input("Ange kontomenyval: "))
    
    if val2 == 4:
        print("Du har avslutat programmet.")

elif val == 3:
    print("Du har avslutat programmet.")



