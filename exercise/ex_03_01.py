hour = input("How many time did you work? ")
rate = input("What rate is yours? ")

fhour = float(hour)
frate = float(rate)

if fhour > 40.0:
    pay = (frate * 40.0) + (fhour - 40.0) * frate * 1.5
    print(pay)
else:
    pay = fhour * frate
    print(pay)