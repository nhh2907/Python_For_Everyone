def computepay(h, r):
	if h > 40:
		xp = (h * r) + (h - 40.0) * (r * 0.5)
	else:
		xp = h * r
	return xp

while True:
	try :
		fhour = float(input('How many hours did you work? '))
		frate = float(input('What rate is yours? '))
	except:
		print('Input must be in numeric letters. Enter a \'number\'')
		continue
	break


# 입력값을 숫자 문자로 받아야 하므로 숫자가 아닌 글자이면 재입력 요구. 다음 코드의  한 가지 단점은 소수점 숫자를 입력하면 인식을 못함
'''
while True:
	hour = input('How many hours did you work? ')
	if not hour.isdecimal():
		print('Input must be in numeric letters. Enter a \'number\'')
		continue
	fhour = float(hour)
	while True:
		rate = input('What rate is yours? ')
		if not rate.isdecimal():
			print('Input must be in numeric letters. Enter a \'number\'')
			continue
		frate = float(rate)
		break
	break
'''

pay = computepay(fhour, frate)
print('Pay', pay)
