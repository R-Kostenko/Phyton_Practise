import re
a = input("Введіть Ваш рядок: ")
num_list = []
 
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
 
print("Список чисел: ", num_list)
print("Найбільше число: ", max(num_list))
words = re.sub("[0-9]", "", a)
print ("Рядок без чисел: ",words)