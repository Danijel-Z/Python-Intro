#Labb 4
def get_key(biggestValue):
    for key, value in SampleData.items():
        if biggestValue == value:
            return key
def print_items():
    for key,value in newData.items():
        print(f"{key} {value}")

SampleData = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
newData = {}
i = 0
while i < 3:
    biggestValue = 0
    for key in SampleData:
        value = SampleData.get(key)
        if value > biggestValue:
            biggestValue = value
    key = get_key(biggestValue)
    newData[key] = biggestValue
    del SampleData[key]
    i = i + 1

print_items()


val_list = list(SampleData.values())
valCopy_list = list(SampleData.values())
key_list = list(SampleData.keys())

count = 0
while True:
    biggestValue= 0
    for value in val_list:
        if value > biggestValue:
            biggestValue = value
    position = valCopy_list.index(biggestValue)
    print(f"{key_list[position]} {valCopy_list[position]}")
    val_list.remove(biggestValue)
    count = count + 1
    if count == 3:
        break


 
#Labb 3.
# from collections import defaultdict, Counter
# str1 = 'w3resource' 
# str1 = str1.replace(str1,'3sruwceo')
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter,0) + 1
# print(my_dict)

#Labb 2.
# SampleData = [{"V":"S001"}, {"V": "S002"},{"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},
# {"VIII":"S007"}]
# SampleList = []


# for val in SampleData:
#     # key_list = list(val.keys())
#     val_list = list(val.values())
#     if val_list not in SampleList:
#         SampleList.append(val_list)
#     else:
#         continue

# print(SampleList)

#Labb1. Write a Python script to check if a given key already exists in a dictionary

# telReg= {"danijel":"2001"}
# telReg["stefan"] = "08- 250123"
# telReg["renault"] = "120"
# telReg["oliver"] = "10- 350135"


# while True:
#     key = input("Skriv ett key. OBS! Tryck 'q' för att avsluta.  ")
#     if key in telReg.keys():
#         print(f"{key} exist")
#         print(f"value= {telReg[key]}")
#     elif key not in telReg.keys() and key != "q":
#         print(f"{key} does not exist")
#     else:
#         if key == "q":
#             print("Du har avslutat programmet.")
#             break

