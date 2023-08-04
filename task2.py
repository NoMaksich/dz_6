print("Введите значения массива")
array=[]
for i in input().split():
    array.append(int(i))
down, up=map(int, input("Введите границы диапазона: ").split())
for i in range(0, len(array)):
    if array[i]>=down and array[i]<=up:
        print(i, end=" ")