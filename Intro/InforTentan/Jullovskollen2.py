from datetime import date

datum= input("Skriv in datum: <YYYY><MM><DD>")
datum=datum.split(" ")

år=int(datum[0])

månad=int(datum[1])

dag=int(datum[2])


d0 = date(år, månad, dag)
d1 = date(år, 12, 20)


if dag > 20 and månad==12:
    d1=date(år+1, 12, 20)
    delta = d1-d0
    print(delta.days)

else:
    delta = d1 - d0
    print(delta.days)

