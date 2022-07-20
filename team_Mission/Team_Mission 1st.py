니안코치님 06팀 리드부스터 노가리입니다
금주 1차미션 제출합니다



Q1

- 할 수 있는 일
    - 시스템 유틸리티 제작
    - GUI 프로그래밍
    - C/C++와의 결합
    - 웹 프로그래밍
    - 수치 연산 프로그래밍
    - 데이터베이스 프로그래밍
    - 데이터 분석, 사물 인터넷
- 하고 싶은 일
    세상은 복잡해지고 인간이 수용할 수 없는 많은 정보가 넘처 흐르고 있습니다.
    그 정보들 중에서 필요하고 효율적인 데이터를 선별하여 세상에 도움이 되는 프로그램을 개발하고 싶습니다



Q2)

- CPU
    CPU는 ‘Central Processing Unit’의 약자로서,직역 하면 중앙처리장치이다. 단어 그대로, 컴퓨터의 정중앙에서 모든 데이터를 처리하는 장치라는 뜻이다.
    CPU는 컴퓨터의 두뇌에 해당하는 것으로서, 사용자로부터 입력 받은 명령어를 해석, 연산한 후 그 결과를 출력하는 역할을 한다.

- Main memory
    컴퓨터의 주요 구조는 크게 중앙처리장치(CPU), 주기억장치, 보조기억장치 및 입출력장치로 구분할 수 있다.
    주기억장치는 프로그램을 기억하는 프로그램 영역과 입력자료를 기억하는 영역, 출력자료를 기억하는 영역, 작업을 실행하여 중간계산결과를 기억하는 작업영역으로 구성된다.
    주기억장치에는 롬(ROM)과 램(RAM)이 있다.

    롬은 읽기만 하는 기억장치로서 전원이 끊어져도 기억된 내용이 지워지지 않으며, 종류로는 마스크롬, 피롬, 이피롬 등이 있다.
    마스크롬은 제작할 때 내용을 기억하기 때문에 사용자가 임의로 바꿀 수가 없다.

    램은 기억된 내용을 사용자가 임의로 변경할 수 있으며 프로그램이나 자료를 저장할 수 있으나 전원이 꺼지면 기억된 내용이 모두 지워진다.
    따라서 휘발성메모리라고도 한다. 램에는 에스램(static RAM)과 디램(dynamic RAM)이 있다. 에스램은 전원이 공급되는 동안은 기억된 내용이 유지되고,
    디램은 전원이 공급되어도 주기적으로 충전(refresh)을 하여 주어야 기억된 자료가 유지된다. 디램은 주로 대용량 기억장치에 사용된다.

- Secondary memory
    컴퓨터의 중앙처리장치가 아닌 외부에 존재하여 주기억장치의 한정된 기억용량을 보조하기 위해 사용하는 것으로 전원이 차단되어도 기억된 내용이 상실되지 않는다.

    반도체로 만들어진 주기억장치는 처리속도가 빠르기는 하지만, 대부분 전원이 끊어지면 저장된 자료가 소멸되고 가격이 비싸 다량의 자료를 영구적으로 보관할 수가 없다.
    그러나 보조기억장치는 속도가 상대적으로 느리기는 하지만, 다량의 자료를 영구적으로 저장할 수 있는 특징이 있다.



Q3)

###################### SyntaxError ######################

# Syntax Error
for i in range(5)
print(i)

# Modified Error
for i in range(5):
    print(i)


# Syntax Error
len('Hello') = 1

# Modified Error
len('Hello') == 1

###################### ValueError ######################

#Value Error
int('this is a cat')

#Modified Error
int(12.1234)


#Value Error
print(int('7.23'))

#Modified Error
print(int('7'))

###################### TypeError ######################

#Type Error
a = 15
b = 'Hello'
c = a + b

#Modified Error
a = '15'
b = 'Hello'
c = a + b


#Type Error
number = '123'
result = number >> 2
print('The given number is :', number)
print('Result is :', result)

#Modified Error
number = 123
result = number >> 2
print('The given number is :', number)
print('Result is :', result)

###################### OverflowError ######################

#Overflow Error
pow(2.0, 1_000_000)


#Modified Error
pow(2.0, 10) #Modified Error

###################### AttributeError ######################

#Attribute Error
import time

time.sleep(1)
time.wake(1)


#Modified Error
import time

time.sleep(1)

###################### KeyError ######################

#KeyError
dic = {'a':'apple', 'b':'banana'}
print(dic['c'])

#Modified Error
dic = {'a':'apple', 'b':'banana'}
print(dic['b'])

###################### IndexError ######################

#Index Error
a = [1, 2, 3, 4, 5]
print(a[5])

#Modified Error
a = [1, 2, 3, 4, 5]
print(a[4])

###################### NameError ######################

#Name Error
prin("Hello")

#Modified Error
print("Hello")



Q4)

k_age = int(input('나이가 몇 살인가요? '))

# 한국나이 1살인 경우는 0살 처리
if k_age == 1:
    print('0')
    quit()

birth = int(input('생일이 지났습니까? 맞으면 0, 아니면 -1: '))

if birth == 0:
    print(k_age - 1)
else:
    print(k_age - 2)





''' 다른 팀의 답변 '''



Q3

####################### SyntaxError #######################

# 잘못된 구문
for i in range(5)
    print(i)

# 올바른 구문
for i in range(5):
    print(i)


# 잘못된 구문
print "Yellow"

# 올바른 구문
print("Yellow")

####################### ValueError #######################

# 잘못된 구문
z = int('abc')

# 올바른 구문
z = str('abc')


# 잘못된 구문
num = int("red")

#올바른 구문
num = int("1")


# 잘못된 구문
z = ['a', 'b']
z.index('x')

#올바른 구문
z = ['a', 'b']
z.index('a')


####################### TypeError #######################

# 잘못된 구문
a=15
b='칠'
c=a+b

#올바른 구문
a=15
b=7
c=a+b


# 잘못된 구문
print(4 + "Green")

# 올바른 구문
print(str(4) + "Green")


####################### IndexError #######################

# 잘못된 구문
a=[1, 2, 3, 4, 5]
print(a[6])

# 올바른 구문
# 마지막 원소를 출력하는 것이 의도였다면
a=[1, 2, 3, 4, 5]
print(a[len(a)-1])


####################### IndentationError #######################

# 잘못된 구문
for i in range (5):
print(i)

# 올바른 구문
for i in range (5):
    print(i)


####################### KeyError #######################

# 잘못된 구문
a={'사과': 'apple'}
print(a['딸기'])

# 올바른 구문
a={'사과': 'apple'}
print(a['사과'])

# 잘못된 구문
d = {"x": 10, "y": 20}
result = d["z"]

# 올바른 구문
d = {"x": 10, "y": 20, "z": 30}
result =d["z"]


####################### NameError #######################

#잘못된 구문
typ(x)

#올바른 구문
type(x)


#잘못된 구문
x = 1
y = 2
print(z)

#올바른 구문
x = 1
y = 2
print(x)


####################### ZeroDivisionError #######################

#잘못된 구문
a = 55 / 0
print(a)

#올바른 구문
a = 55 / 1
print(a)


####################### AttributeError #######################

import math

#잘못된 구문
a = math.ceil2(1.2)
print(a)

#올바른 구문
a = math.ceil(1.2)
print(a)


Q4

####################### 방법 1. 한 큐에 끝낸다. #######################
K_age = int(input('당신은 몇 살인가요? '))
print()
print('생일이 아직 안지났다면 미국나이로', K_age - 2, '살 이고, ')
print('오늘이 생일이거나 생일이 지났다면 당신은', K_age - 1, '살 입니다!')


####################### 방법 2. 나는야 숫자의 달인 #######################
from datetime import datetime #datetime 모듈 사용

#잘못된 값이 들어오면 프로그램 다시 실행
while True :
  birth_yyyymmdd = input('생년월일을 적어주세요. ex)20220101  : ')
  if not birth_yyyymmdd.isnumeric():
    print("숫자가 아닌 값이 들어왔습니다. 다시 입력하세요.")
    continue
  if len(str(birth_yyyymmdd)) != 8:
    print("8가리 수가 아닌 값이 들어왔습니다. 다시 입력하세요.")
    continue
  break

format = '%Y%m%d'
datetime.strptime(birth_yyyymmdd, format)

now_date = datetime.now()
now_date = now_date.date()
now_date = now_date.strftime('%Y%m%d')

#생년월일이 지났는지 확인하기 위해 월일 데이터 자르기
birth_mmdd = birth_yyyymmdd[4:8]
now_date_mmdd = now_date[4:8]

#나이 계산을 위한 년 데이터 자르기
birth_yyyy = int(birth_yyyymmdd[0:4])
now_date_yyyy = int(now_date[0:4])

#생년월일이 현재월일보다 크면 -1
#생년월일이 현재월일보다 작으면 그대로
if birth_mmdd >= now_date_mmdd :
  age = now_date_yyyy - birth_yyyy -1
else :
  age = now_date_yyyy - birth_yyyy

#나이 계산에서 -값이 나오면 0세로 나오게 출력
if age < 0 :
  age = 0

print('현재 미국나이(만 나이)는', str(age) +'세 입니다.')


####################### 방법 3. 주어진 조건에 맞춰봅시다. #######################
korean_age = int(input("당신의 나이를 입력해주세요."))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
if(birth == 0):
  american_age = korean_age - 1
elif(birth == -1):
  american_age = korean_age - 2
print(american_age)


##################### 4. 꼭 시키는 대로 안 하는 사람이 있지요 #####################
def convert_age(korean_age, birth):
    if birth == 'Y' or birth == 'y':
        return korean_age - 1
    elif birth == 'N' or birth == 'n':
        return korean_age - 2
    else:
        return '잘못 입력했습니다.'

age = int(input("한국 나이로 몇 살입니까? : "))
yn = input("생일이 지났습니까?(맞으면 Y 아니면 N) : ")

print('미국나이:', str(convert_age(age, yn)), '세')
