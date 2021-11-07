#Labb1 Nutid. Skriver ut aktuellt datum&tid

from datetime import datetime, timedelta

# dt = datetime.today() 
# print(dt)

# dt = datetime.today().replace(microsecond= 0)
# print(dt)

# dt = datetime.today().strftime("%Y-%m-%d")
# print(dt)

#Det här är ett annat sätt att replace sekunder till 0
# import datetime
# dt = datetime.datetime.today().replace(microsecond=0)
# print(dt)


#Labb2 Datumdelar
# dt = datetime.now()
# print(f"År= {dt.year}")
# print(f"Månad= {dt.month}")
# print(f"Dag= {dt.day}")
# print(f"Timmar= {dt.hour}")
# print(f"Minuter= {dt.minute}")
# print(f"Sekunder= {dt.second}")
# print(f"Millisekunder= {dt.microsecond}")

#Labb3 Dagens Veckodag, först på engelska

# veckodagLista= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# valdDatum= input("Skriv ett datum - ex.(2001-10-04): ")
# veckoDag = datetime.strptime(valdDatum, "%Y-%m-%d")
# print(f"Your weekday is: {veckodagLista[veckoDag.weekday()]} ")

#Nu på svenska:
# veckodagLista= ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
# print(f"Din veckodag är: {veckodagLista[veckoDag.weekday()]} ")

#Labb4 
# from datetime import datetime, timedelta
# till_40dagar= datetime.now()
# org_tid= till_40dagar.strftime("%Y-%m-%d-%X %p")
# weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# dag_efter40= till_40dagar+timedelta(days=40)
# print(f"idag {org_tid}")
# print(weekDays[dag_efter40.weekday()])

#Labb5


def KampanjPris():
    startDatum = datetime(2021,10,27)
    
    slutDatum = startDatum + timedelta(days = 30) 

    dagensDatum= datetime.now()
    
    if startDatum <= dagensDatum and dagensDatum <= slutDatum:
        pass
  
        
KampanjPris()
#Labb6
dateFromUser = input("Skriv ett datum här: (ex- 2021-10-04) ")
selected_Date = datetime.strptime(dateFromUser,"%Y-%m-%d")
selected_Date = datetime.replace(selected_Date, day = 28).date()

dateAfterOneMonth = selected_Date + timedelta(days = 5)
dateAfterOneMonth = datetime.strftime(dateAfterOneMonth, "%Y-%m-%d")

new_Date = datetime.strptime(dateAfterOneMonth, "%Y-%m-%d")
new_Date = datetime.replace(new_Date, day = 1).date()

# selected_Date = selected_Date.date()
# new_Date = new_Date.date()

whatMonthInSelected= selected_Date.strftime('%B')

NumberOfDaysInSelectedMonth = new_Date - timedelta(days = 1)

print(f"Antal dagar i {whatMonthInSelected} är {NumberOfDaysInSelectedMonth.day}")

