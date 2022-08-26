def calculate_ROE(stocks, sells):
	new_list = list()
	stocks = stocks.split(',')

	# 여기서도 enumerate를 사용
	for i, stock in enumerate(stocks): 
		stock = stock.split('/')
		# 인덱스를 하드코딩하는 것 대신 언패킹으로 간단히 할 수 있음
		name, num, average = stock
		ROE = ((sells[i]-int(average)) / int(average)) * 100
		new_list.append((ROE, name))

	new_list.sort(reverse=True)

	for ROE, stock in new_list:
		print(f"{stock}의 수익률: {ROE:.2f}")
		print(f"{stock}의 수익률: {ROE:.3}")  # 또 다른 소수 둘째 표현
	
stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

calculate_ROE(stocks, sells)
