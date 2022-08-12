str = 'X-DSPAM-Confidence: 0.8475'
index = str.find(':')
print(index)

print(str[index:])

# 아직은 문자열임
number = str[index+1:]
print(number)

# 숫자, not 문자열. 그래서 float 형변환 함수가 앞의 화이트스페이스를 없앴음
float_number = float(number)
print(float_number)
