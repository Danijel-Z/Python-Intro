#Hjälp funktionen, som beskriver själva funktionen och vad den gör. 
#Fast man måste skriva manuellt infon i funktionen!
def greet(name, greeting="Hello"):
    """Print a greeting to the user `name`
    Optional parameter `greeting` can change what they're greeted with."""

    print("{} {}".format(greeting, name))

help(greet)


def inputNamn(minLength, language, namn, name):
    if language == "Sv":
        print(f"Mata in {namn}: ")
    else:
        print(f"Enter {name}: ")
    while True:
        namn = input()
        if len(namn) > minLength:
            break
    return namn #Stoppar in resultatet i namn

lang = input("Välj Sv eller En för språk: ")
forNamn = inputNamn(3, lang, "förnamn", "forname")
efterNamn = inputNamn(6, lang, "efternamn", "lastname")


def inputNamn(minLength, language = "sv"):
    if language == "sv":
        print(f"Mata in namn: ")
    else:
        print(f"Enter name: ")
    while True:
        namn = input()
        if len(namn) > minLength:
            break
    return namn

lang = input("Välj Sv eller En för språk: ")
forNamn = inputNamn(3, lang)
efterNamn = inputNamn(6, lang)
