# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите число X '))
y = int(input('Введите число Y '))
z = int(input('Введите число Z '))

leftPart = not (x or y or z)
rightPart = not x and not y and not z
result = leftPart == rightPart

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')


