#Loop 1, skriver ut tal från 0 till 10 med for- och while loop
# for tal in range(11):
    # print(tal)

# tal = 0
# while tal <11:
#     print(tal)
#     tal = tal + 1

#Loop 2, Matar in 2 tal som sedan printas ut de tal emellan dessa två. Man gör det först med for och sedan while loop
# tal1 = int(input("Mata in ett tal: "))
# tal2 = int(input("Mata in en till tal: "))

# for tal in range(tal1, tal2 + 1):
#     print(tal)

#Loop 3, Användare matar in 2 tal som sedan adderas och skrivs ut. 
#Efteråt kommer while loop som ställer en fråga om användaren vill fortsätta. 
#Om den trycker på J upprepas/itereras processen, och om den trycker på N avslutas programmet

# tal1 = int(input("Mata in ett tal: "))
# tal2 = int(input("Mata in ett annat tal: "))
# summa = tal1 + tal2
# print(summa)

# while True:
#     svar = input("Vill du fortsätta? Tryck J eller N ")
#     if svar == "J":
#         tal1 = int(input("Mata in ett tal: "))
#         tal2 = int(input("Mata in ett annat tal: "))
#         summa = tal1 + tal2
#         print(summa)
#     elif svar == "N":
#         print("Programmet avslutat.")
#         break

#Loop 4, börjar med att skapa en variabel som heter summa och har värde 0
#I for-loopen sätter jag range till 10
#Loopen sparar talet som användare matar in i variabel som heter tal
#Sedan uppdateras summan, genom att man tilldelar summan med att addera det nya talet (tal) med det gamla talet i summan, d.v.s. (summa)
# summa = 0
# for i in range(10):
#     tal = int(input("Mata in ett tal: "))
#     summa = tal + summa

# print("Summan av talen är: ", summa)

#Loop 5, Skapar ett tal som har värde 0
#Sparar i variabeln "tal1" det tal användare matar in
#Sedan i for-loopen skapar vi range till talet som användare har matat in
#Och så länge tal1 är större än tal2 ska den skriva ut talet och sedan minusera med 1
# tal2 = 0
# tal1 = int(input("Mata in ett heltal: "))

# for i in range(tal1):
#     if tal1 > tal2:
#         print(tal1)
#         tal1 = tal1 - 1
# print("Klar!")

#Loop 6

#Loop 7
#Slumpa två tal
import random

while True:
    print("Rolling the dice")
    print("The values are: ")
    randomNumber1 = random.randint(1, 6)
    randomNumber2 = random.randint(1, 6)
    print(randomNumber1)
    print(randomNumber2)

    c = input("Roll the dice again? ")
    if c == "y" or c == "yes":
        continue
    #det här är två andra kod för samma sak
    # if not (c== "y" or c == "yes"):
    #     break
    # if c != "y" or c != "yes":
    #     break

    

