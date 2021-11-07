import random

def randomFrånLista(lista):

    resultat=random.choice(lista)

    return resultat



while True:
    SkrivDingrej=input()
    
    inmatninglista=["Jag mår bra","Lämna mig ifred","Vad sa du?","whatever","Kanske det","Ingen aning", "Ja vad bra"]

    print(randomFrånLista(inmatninglista))