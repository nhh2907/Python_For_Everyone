def calculate_ROE(stocks, sells):
	new_list = list()
	stocks = stocks.split(',')

	i = 0
	for stock in stocks: 
		stock = stock.split('/')
		ROE = ((sells[i]-int(stock[2])) / int(stock[2])) * 100
		new_list.append((ROE, stock[0]))
		i += 1

	new_list.sort(reverse=True)

	for ROE, stock in new_list:
		print(f"{stock}의 수익률: {ROE:.2f}")
		print(f"{stock}의 수익률: {ROE:.3}")  # 또 다른 소수 둘째 표현
	
stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

calculate_ROE(stocks, sells)
