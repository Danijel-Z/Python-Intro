text = "ni talar bra latin"
text = text.replace(" ", "")
textReversad = text[::-1]

if text == textReversad:
    print("Palidrom")
else:
    print("Ej palidrom")

text = "text@hotmail.com"
#text = text[::-1] #Reversar strängen
hittadSnabbelA = text.find("@")
punktPosition = text.rfind(".")

if hittadSnabbelA != -1 and punktPosition != -1:
    textInnanPunkt, textEfterPunkt = text.split(text[punktPosition],1)
    if len(textEfterPunkt) >= 2 and len(textEfterPunkt) <=3:
        print("Det är en korrekt mail.")
else:
    print("Det är en felaktig mail.")

class Team:

    def __init__(self,namn,antal_vunna,antal_förlorade,avgojrda_match):
        self._namn = namn

        self._antalvunna = int(antal_vunna)

        self._antalförlorade = int(antal_förlorade)

        self._avgjorda_match = int(avgojrda_match)


    def Poäng(self):
        resultat = self._antalvunna * 3 + self._avgjorda_match
        return resultat

    def skriv_ut (self):
        poäng= self.Poäng()

        utskrifta = f'{self._namn},{self._antalvunna},{self._avgjorda_match},{self._antalförlorade},{poäng}'
        utskrifta=utskrifta.split(',')

        return utskrifta


lista_team= []

while True:

    namn= input("Skriv in <Namn> <Antal vunna> <Antal förlorade> <Oavgjorda matcher>: ")

    if namn == "N" or namn == "n":

        for team in lista_team:
            team = ",".join(team)
            print(team)
        break

    namn_1 , antal_vunna,antal_förlorade,avgjorde_match = namn.split()

    Fösta_team =Team(namn_1 , antal_vunna,antal_förlorade,avgjorde_match)

    lista_team.append(Fösta_team.skriv_ut())
