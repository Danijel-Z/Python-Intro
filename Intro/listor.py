allaSpelare = []
antal = len(allaSpelare)
while True:
    print("1.Skapa ny spelare")
    print("2.Lista alla spelare")
    print("3.Skriv ut den som är först i listan")
    print("4.Hur många spelare finns det? ")
    print("5.Avsluta")
    print(" ")
    
    sel = input("Vad vill du göra? ")
    if sel == 5:
        break
    if sel == 4:
        print(f"Nu är det {antal} spelare i listan")
    if sel == "3":
        print(allaSpelare[0])
    elif sel == "2":
        print("***Här är alla spelare***")
        for player in allaSpelare:
                print(player)
    elif sel == "1":
        print("***Ny spelare***")
        namn = input("Ange spelarens namn: ")
        allaSpelare.append(namn)

minaBarn = ["Sim", "Kaiqi", "Dimitris", "Daniel"]
for namn in minaBarn:
    print(namn)

#Med en for-loop
# ta fram det största talet i denna lista och skriv ut
#Först lägger vi till listan, skapar variabeln "largestSoFar" med värden 0. 
#Sedan lägger vi till for-loop och if-sats, på if-satsen frågar vi om talet är större än 0, och om det är det så sparas det i "largestSoFar"
listaMedTal= [3, 5504, 960, 45]

largestSoFar = 0
for tal in listaMedTal:
    if tal > largestSoFar:
        largestSoFar = tal 

print(tal)

