def palindrom(ord):
    ord = ord.replace(" ", "")
    ordReversed= ""
    ordlength = len(ord) + 1
    for bokstav in range(-1,-ordlength,-1):
        ordReversed += ord[bokstav]
    if ord == ordReversed:
        return "Det är en palidrom"
    
    return "Det är inte en palidrom"

a=input("Mata in ett ord")
print(palindrom(a))

temp=input("Skriv din mening här: ")

temp=temp.split()
temp="".join(temp)
temp=list(temp)

omvänt= temp[::-1]
kontroll=True

for i in range(len(temp)):

    if temp[i] == omvänt[i]:
        test=True

    elif temp[i] != omvänt[i]:
        test=False
        print("Denna mening är inte palymdrom")
        break

if test==True:
    print("Denna mening är palymdrom")


with open('produkt.txt') as file:

    lista = file.readlines()
    lista = [x.split(',') for x in lista]

    # for i in range (0,len(lista)):
    #     lista[i] = lista[i].replace("\n", "")
    #     lista[i] = lista[i].split(",")

    for produkt in lista:
        idprodukt = produkt[0]
        pris = produkt[1]
        perAntal = produkt[2]
        namn = produkt[3]



while True:
    forNamn = input("Förnamn: ")
    if len(forNamn) < 10:
        break
    print("Namnet är för långt")

age = 50

# f-string
print(f"Hej {forNamn}. Du är {age} år gammal")


#String to lower
forNamnInLowerCase = forNamn.lower()

if forNamnInLowerCase == "stefan":
    print("Hej")

#String find
# namn = "Stefan"
# index = namn.find("St")
# if index == -1:
#     print("Fanns inte")
# else:
#     print(f"Hittades på position {index}")  

#String replace + find
while True:
    txt = input("Skriv text: ")
    index = txt.find("moron")
    if index != -1:
        print("Du är utkickat ur gruppen")
        break

    txt = txt.replace("idiot", "?#*#*")
    txt = txt.replace("dumskalle", "*********")
    print(txt)
 

