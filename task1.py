
first=int(input("Введите первое число: "))
difference=int(input("Введите разность: "))
count=int(input("Введите колчиество элементов: "))
array=[]
for i in range(first, count+1):
    array.append(first+(i-1)*difference)
print(array)