score = input("What score is yours? ")
fscore = float(score)

if fscore > 1.0:
    print('Error, Out of range')
    quit()

if fscore >= 0.9:
    print('A')
elif fscore >= 0.8:
    print('B')
elif fscore >= 0.7:
    print('C')
elif fscore >= 0.6:
    print('D')
else:
    print('F')