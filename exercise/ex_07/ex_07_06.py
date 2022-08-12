user_list = list()

while True:
    user_input = input('Enter a number: ')
    if user_input == 'done' : break
    value = float(user_input)
    user_list.append(value)

print('Max', max(user_list))
print('Min', min(user_list))
print('Average', sum(user_list)/len(user_list))