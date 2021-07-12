import re
a = input("Введіть Ваш рядок: ")
num_list = []
max_num=0
 
num = ''
for char in a:
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            num_list.append(int(num))
            num = ''
if num != '':
    num_list.append(int(num))
if len(num_list)>0:
    max_num=max(num_list)
else:
    print("В рядку відсутні числа!!!")
print("Список чисел: ", num_list)
print("Найбільше число: ", max_num)
words = re.sub("[0-9]", "", a)
print ("Рядок без чисел: ",words)