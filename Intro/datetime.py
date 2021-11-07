from datetime import datetime, timedelta

#Julafton, räknar hur många dagar det är kvar tills julafton
julAfton = datetime(2021,12,24)
idag =  datetime.now()
timespan = julAfton - idag
print(f"Det är {timespan.days} dagar")

#Skriver ut vilken veckodag datumet är, i det här fallet är det nummer 3, som är en torsdag. Måndag == 0 och söndag == 6
jagArFoddDettaDatum = datetime(2001,10,4)
print(jagArFoddDettaDatum.weekday())
datum = datetime.now()

#Ett mer utförlig exempel på veckodagar
weekDay = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(weekDay[3])
print(weekDay[jagArFoddDettaDatum.weekday()])

#skriver ut nuvarande datum lite mer komplex, d.v.s. med nollor: 2021-04-10, istället för 2021-4-10
nuvarandeDatum = datetime.strftime(datum,"%d-%m-%Y")
print(nuvarandeDatum)

while True:
    print("Skriv in ditt födelsedag- ex 2001-10-04")
    date = input()
    dat = datetime.strptime(date, "%Y-%m-%d")
    print(f"Du är född på vecka {dat.weekday()} ")
    break

#Skapar två variablar, en är "dagens datum" och en är "datum om 30 dagar"
invoiceDate = datetime.now()
forFalloDag = invoiceDate + timedelta(days = 30)

print(forFalloDag.weekday())
if forFalloDag.weekday() == 5:
    forFalloDag = forFalloDag - timedelta(days=1)
if forFalloDag.weekday() == 6:
    forFalloDag = forFalloDag + timedelta(days=1)

#Formaterar datumet till finskrivet datum: ex. 2021-04-10
formattedInvoiceDate = invoiceDate.strftime("%Y-%m-%d")
print(f"Fakturadatum: {formattedInvoiceDate} ")
formatedForFalloDag = forFalloDag.strftime("%Y-%m-%d")
print(f"Fakturadatum: {formatedForFalloDag}")

#skapar ny variabel med namnet "idag" 
idag = datetime.now()

#Hoppar över varje första dag i månaden
if idag.day != 1:
    print("Kör batch")

#Skriver ut år, månad och dag för sig själva
print(idag.year)
print(idag.month)
print(idag.day)
