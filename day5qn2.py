def area_of_circle(radius):
    return 3.14 * radius * radius
def area_of_triangle(base, height):
    return 0.5 * base * height
r = int(input("Enter the radius value: "))
area_circle = area_of_circle(r)
print("Area of circle:", area_circle)
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_triangle = area_of_triangle(base, height)
print("Area of triangle:", area_triangle)
