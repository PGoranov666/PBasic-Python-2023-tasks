from math import pi
type_of_figure = input()

#Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
if type_of_figure == "square":
    side = float(input())
    area = side * side
    print(f"{area:.3f}")

#Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
elif type_of_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")

#Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
elif type_of_figure == "circle":
    radius = float(input())
    area = pi * (radius ** 2)
    print(f"{area:.3f}")

#Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
elif type_of_figure == "triangle":
    lenght = float(input())
    height = float(input())
    area = lenght * height / 2
    print(f"{area:.3f}")
