def check_string_overlapped(king_list):
	''' 고려 또는 조성 왕들 중 같은 이름이 있으면 고려와 조선과 비교하기
	전에 미리 제거'''

	i = 0
	for king in king_list:
		if king in king_list[i+1: ]:
			del king_list[i]
		i += 1
	return king_list

def check_duplicate(korea_king, chosun_king):
	# 같은 시대(고려 또는 조선) 왕이름 중에 중복되는 이름이 있으면 미리 중복이름 제거
	korea_king = check_string_overlapped(korea_king.split(','))
	chosun_king = check_string_overlapped(chosun_king.split(','))

	# histogram 만들기
	king_dict = dict()
	for king in korea_king + chosun_king:
		king_dict[king] = king_dict.get(king, 0) + 1
	print(king_dict)
	
	count = 0
	for king, repetition in king_dict.items():
		if repetition > 1:
			count += 1
			print(f"고려와 조선에 모두 있는 왕: {king}")

	print(f"고려와 조선에 있는 왕 이름은 총 {count}개 입니다")


korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

check_duplicate(korea_king, chosun_king)
