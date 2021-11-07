d = {}
d["new_dict"] = [1, 2, 3]
print(d)
d['new_dict'] = {'nested_dict': 1}
print(d)

#TelegonRegister

lista = []
lista.append("08-250123")
lista.append("10-350135")
#index
for index in range(len(lista)):
    talet = lista[index]

telReg= {}
telReg["stefan"] = "08- 250123"
telReg["renault"] = "120"
telReg["oliver"] = "10- 350135"

namn = input("Ange ett namn som du vill ha reda på telefonnummret till: ")
telnr = (input("Ange mobilnummer: "))
telReg[namn] = telnr

print(f"Ditt namn är {namn} och ditt telefonnummer:{telnr}")




#Uppgift 3
sample_s = 'w3resource'

listan=[]

for char in sample_s:
    listan.append(char)

print(listan)

ny_dic={}

x = 1

ny_lista = set(listan)

for i in ny_lista:
    ny_dic.update({i:x})
    x += 1

print(ny_dic)

dikt = {}
ord = "w3resource"
for bokstav in ord:
    countAntalBokstav = ord.count(bokstav)
    dikt[bokstav] = countAntalBokstav

print(*dikt)

