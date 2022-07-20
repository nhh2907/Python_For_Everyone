hour = input("How many time did you work? ")
rate = input("What rate is yours? ")

try:
    fhour = float(hour)
    frate = float(rate)
except:
    print("Error, Please enter numeric input")
    quit()

if fhour > 40.0:
    pay = (frate * 40.0) + (fhour - 40.0) * frate * 1.5
    print(pay)
else:
    pay = fhour * frate
    print(pay)