radius = 20
pi = 3.14
def area_of_circle(radius):
    area = pi * radius ** 2
    return area
def circumference_of_circle(radius):
    circumference = 2 * pi * radius
    return circumference
area = area_of_circle(radius)
circumference = circumference_of_circle(radius)
print("Area of the circle:", area)
print("Circumference of the circle:", circumference)
