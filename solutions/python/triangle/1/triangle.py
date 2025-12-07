def triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    return (a + b >= c) and (b + c >= a) and (a + c >= b) and (a + b + c > 0)

def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    return triangle(sides) and (a==b==c)
    
def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    return triangle(sides) and (a==b or a==c or b==c)

def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    return triangle(sides) and a!=b and a!=c and b!=c
