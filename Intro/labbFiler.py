# with open('filA.txt') as f:
#     data = f.read()
  
# # Reading data from file2
# with open('filB.txt') as f:
#     data2 = f.read()
  
# # Merging 2 files
# # To add the data of file2
# # from next line
# data += "\n"
# data += data2
  
# with open ('file3.txt', 'w') as fp:
#     fp.write(data)

# import os
# filnamn = ["filA.txt", "filB.txt"]
# fil = ""
# for namn in filnamn:
#     with open(namn, "r") as infile:
#         fil = fil + infile.readline()
# filensNamn = input("Skriv filens namn (+ .txt): ")
# with open(filensNamn, "w") as f:
#     while True:
#         if os.path.exists(filensNamn):
#             print("Denna fil finns redan. Vänligen välj en annan.")
#             filensNamn = input()
#         else:
#             f.write(fil)
#             break
    

#Labb 3

tal = 1

with open("filA.txt", "w") as f:
   
    f.write(f" {tal}  Hej hej!\n")
    tal = tal + 1
    f.write(f" {tal}  Nu skapar vi nytt fil\n")
    tal = tal + 1
    f.write(f" {tal}  Nu skapar vi nytt fil\n")
    tal = tal + 1

lines = []
with open('49.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print(f'line {count}: {line}') 
