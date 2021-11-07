#Labb8: Rövarspråk

#Kommentera flera linjer:
"""
This type of comment spans multiple lines.
These are mostly used for documentation of functions, classes and modules.
"""

#Extralabb: Är jämt?
def isEven(a):
    if a%2 ==0:
        return True
 #this next line should be even with the if
    return False

print(isEven(7))

#Labb7: Vokaler
def Vokal(text):
    vokalList = ["a", "e", "i", "o", "u", "y", "å", "ö", "ä"]
    for bokstav in text:
        if bokstav not in vokalList:
            print("False")
        else:
            print("True")


text = "tjenaöäå"
Vokal(text)


#TestLabb:
def Add(age):
    b = 123
    age = age +1
    return age

age = 18
print(age)
Add(age)
print(Add(age))

#Labb6: ToPercentage
def ToPercentage(decTal):
    procent = decTal * 100
    return f"{procent} %"

decTal = float(input("Mata in ett siffra mellan 0 och 1 (ex. 0.5) "))
# procent = ToPercentage(decTal)
print(f"{decTal} är {ToPercentage(decTal)}.")

#Labb5: Räkna skatt
def CalculateTaxesOnSalary(lon):
    if lon >= 30000:
        lon = lon * 0.33
    elif lon < 15000:
        lon = lon * 0.12
    elif lon < 30000:
        lon = lon * 0.28
    return round(lon)

lon = int(input("Hur mycket är din månadslön? "))
skatt = CalculateTaxesOnSalary(lon)
print(f"Ditt skatt är: {skatt} ")


#Labb4: Längsta ordet, man ska hitta det längsta ordet och skriva ut det
def HittaLangstaOrdet(Array):
    langstaOrdet = ""
    for i in Array:
        if len(i) > len(langstaOrdet):
            langstaOrdet = i
    return langstaOrdet

Array = ["Hej", "Tjenare"]
svar = HittaLangstaOrdet(Array)
print(svar)





#Labb3: Ålder, se om man är myndig eller inte. Men först ska den säga True eller False
def IfMyndig(alder):
    if alder >= 18:
        return True
    else:
        return False

alder = int(input("Mata in ditt ålder: "))
svar = IfMyndig(alder)
if svar == True:
    print("Du är myndig")
else:
    print("Du är inte myndig")

#Labb2: Räkna ut MOMS
def MOMS(kostnad):
    moms = kostnad * 0.25
    return moms

kostnad = 200
moms = MOMS(kostnad)
print(moms)

#Labb1: Plussa ihop 2 stringar med hjälp av funktionen

def AdderaStrings(string1, string2):
    resultat = string1 + string2
    return resultat
    #return string1 + string2

a = "kfksmf"
b = "mkfms"
resultat = AdderaStrings(a,b)
print(resultat)

