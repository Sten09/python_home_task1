#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/

#in
# - 3
# - 6
# - 2
# - 1

#out
#5.099

x1 = float(input("Введите координату точки А по х: "))
y1 = float(input("Введите координату точки A по y: "))
x2 = float(input("Введите координату точки B по х: "))
y2 = float(input("Введите координату точки B по y: "))

S = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(round(S, 2))