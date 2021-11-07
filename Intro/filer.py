#Printa alla namn som finns i main.txt filen, "read mode(r)"
with open("main.txt", "w") as f:
    for line in range(5):
        f.write("Hej \n")

with open("HundLista.txt", "r") as f:
    for line in f:
        x = line.find("Hej")
        if x == True:
            halsa = x
            print("Daki" + halsa)

    


l = ["Hej","Tjo", 15]
n = []
#Skapa ny fil och lägga till text i den med hjälp av "append mode(a)"
with open("newfile.txt", "a") as f:
    for index in l:
        f.write(f"{index}\n")
    f.write("Klart!\n")
with open("newfile.txt", "r") as f:
    for line in f:
        n.append(line)
    n[4] = int(n[4])

#Ändrar texten i newfile.txt med hjälp av "write mode(w)". Den tar bort allt gammal text och skriver till nytt
with open("newfile.txt", "w") as f:
    f.write("Hej hej!\n")
    f.write("Nu skapar vi nytt fil\n")
    f.write("Nu skapar vi nytt fil\n")
    f.write("Nu skapar vi nytt fil\n")
    f.write("Nu skapar vi nytt fil\n")
    f.write("Nu skapar vi nytt fil\n")


#Tar bort en fil med import os och os.path
import os 
if os.path.exists("main.txt"):
    os.remove("main.txt")

#Skriver ut varannan text, börjar med den första meningen
udda = True
with open("produkt.txt", "r") as f:
    for line in f:
        if udda == True:
            print(line)
            udda = False
        else:
            udda = True




