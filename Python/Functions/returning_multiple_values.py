import math
def circle(r):
    area = math.pi*r*r
    circumference = 2*math.pi*r
    return "{:.2f}".format(area), "{:.2f}".format(circumference)

r = 5
a, c = circle(r)
print("Area of circle is", a)
print("Circumference of circle is", c)