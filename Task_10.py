# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

Ax = float(input('Введите координату точки А по X: '))
Ay = float(input('Введите координату точки А по Y: '))
Bx = float(input('Введите координату точки В по X: '))
By = float(input('Введите координату точки B по Y: '))
print(f'Расстояние между двумя точками составит {round(((Ax - Bx) ** 2 + (Ay - By) ** 2) **0.5, 2)}')