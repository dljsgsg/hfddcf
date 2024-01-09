
start = int(input("tell yor number:"))
end = int(input("tell diapozon:"))
for number in range(start, end + 1):
    if number % 7 == 0:
        print(number)
#2
start = int(input("tell yor number:"))

end = int(input("tell diapozon: "))
for i in range(start, end+1):
    print(i, end=' ')
print()
print(";Все числа диапазона в убывающем порядке;")
for i in range(end, start-1, -1):
    print(i, end= " ")
print()
print("Все числа, кратные 7")
for i in range(start, end+1):
    if i % 7 == 0:
        print()
print(i, end='')
count = 0
for i in range(start, end+1):
    if i % 5 == 0:
        count += 1
print('Количество чисел, кратных 5:', count)
#3
