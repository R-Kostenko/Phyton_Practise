import random
value=[]
for i in range(30):
    k=random.randint(-100,100)
    value.append(k)
print (value)
print("\nМаксимальне число:",max(value))
print("Індекс максимального числа:",value.index(max(value)))
value_change=[i for i in value if not i%2]
value_change.sort(reverse=True) 
print("Відсортований список:", value_change)