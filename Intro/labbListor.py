#List 6
namnLista = ["Bannana", "Anakonda", "Daki", "Kik", "D"]
for namn in namnLista:
    namnLength = len(namn)
    if namnLength > 5:
        print(namn)

        
#List 5, Raderar duplikater från lista 
# med hjälp av funktionen "set"
namnLista = ["Anna", "Anna", "D", "Kik", "Kik", "D"]
namnLista = set(namnLista)
print(namnLista)

#List 4
namnLista = ["Anna", "Lukas", "D", "Kik"]

namnLength = len(namnLista)
for namn in namnLista:

    namnLowerCase = namn.lower()
    namncharacter = len(namn)
    lastCharacter = namn[namncharacter - 1]

    if namncharacter > 2 and (namnLowerCase[0] == lastCharacter):
        print(namn)


#List 3
nList= [1, 2, 4, 5]
nLargest = 0
for n in nList:
    if n > nLargest:
        nLargest = n
print(n)

#List 2
nList= [1, 2, 4, 5]
summa = 0
for n in nList:
    summa = n + summa
print(summa)

summa = 0
for index in range(len(nList)):
    talet = nList[index]
    summa = talet + summa
    
print(summa)

#List 1
tal1 = int(input("Mata in ett tal: "))
tal2 = int(input("Mata in ett tal: "))
tal3 = int(input("Mata in ett tal: "))
tal4 = int(input("Mata in ett tal: "))

talLista= [tal1, tal2, tal3, tal4]
longestTal = 0
for tal in talLista:
    if tal > longestTal:
        longestTal = tal

print(f"Det största talet är tal {tal}.")
