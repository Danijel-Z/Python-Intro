#True and False
# first = True
# beforeWasSpace = False

# namn = input()
# nyNamn = ""
# for i in namn:
#     if first or beforeWasSpace:
#         nynamn = i.upper()
#     else:
#         nyNamn = nyNamn + i
#     first = False
#     beforeWasSpace = i == ""

#String 1
# txt1= input("Mata in ett text: ")
# txt2= input("Mata in ett annat text: ")
# txt3= input("Och mata in ett till text: ")

# print(f"Du skrev: {txt1}, {txt2} och {txt3}.")

#String 2

# txt = "Hello, world"
# for i in txt:
#     if i == "w":
#         n= txt.find("w")
#         print(f"Du har en {i} i texten. Och den ligger på positionen {n}")

#annat exempel,fast lättare och bättre

# txt = input()
# n= txt.find("w")
# print(f"Du har en w i texten. Och den ligger på positionen {n}")

#String 3, Den här är sjuuuk True and False
#Förvandlar första bokstavet i namnet till ett stort bokstav
# namn = "danijel daki zdravkovic"
# nyttNamn = ""
# FirstLetter = True
# LetterAfterSpace = False

# for bokstav in namn:
#     if FirstLetter or LetterAfterSpace == True:
#         nyttNamn = nyttNamn + bokstav.upper()
#     else:
#         nyttNamn = nyttNamn + bokstav
#     FirstLetter = False
#     if bokstav == " ":
#         LetterAfterSpace = True
#     else:
#         LetterAfterSpace = False

# print(nyttNamn)


#String 4
# antalStars = 0

# text = "Detta är en string som du ska ändra."
# text = text.replace(" ", "*")

# for i in text:
#     if i == "*":
#         antalStars = antalStars + 1

# print(antalStars)

#String 5
mail = input("Skriv in ditt mail adress: ")
EfterPunkt = True
for bokstav in mail:
    if bokstav != "@":
        print("Titta igenom ditt mail adress. ")
    if EfterPunkt == True:
        bokstav = "."
        

