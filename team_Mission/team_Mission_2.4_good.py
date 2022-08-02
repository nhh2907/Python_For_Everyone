# 다음 코드는 if문 없이 list comprehension으로 구현함

def bus_fare(types, ages):
	fare = {'card':[0, 450, 720, 1200, 0], 'cash':[0, 450, 1000, 1300, 0]}
	age_table = {
		range(0, 8):0,
		range(8, 14):1,
		range(14, 20):2,
		range(20, 75):3,
		range(75, 200):4
	}

	# List comprehension
	bus_fare = [fare[types][index] for age_set, index in age_table.items() if ages in age_set ][0] 

	print(f'나이 = {ages}', f'종류 = {types}', f'요금은 {bus_fare}원입니다', sep='\n')

age_ = int(input('Your age? '))
type_ = input('card or cash? ').lower()
bus_fare(type_, age_)
