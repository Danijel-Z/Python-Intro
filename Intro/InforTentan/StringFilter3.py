def filterContains(inList, filter): 
    outList=[]
    for i in filter:
        for n in inList:
            if i in n:
                outList.append(n)
            else:
                pass
    return outList

kontrollLista=["Herro", "234", "Namn", "hej på dig", "frukt"]
filterLista=["rr","1"," "]


print(filterContains(kontrollLista, filterLista))

listamedtal=[3,6,2,8,0]
listamedtal.sort(reversed=True)
print(*listamedtal)