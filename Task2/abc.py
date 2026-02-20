a= float(input("a"))
b= float(input("b"))
c= float(input("c"))

D = b**2 - 4*a*c

print(f"D{D}")

if (D > 0):
    x_1= (-b+ (D)**(0.5))/(2*a)
    x_2= (-b- (D)**(0.5))/(2*a)

    print(f"x1, {x_1} __ x2 {x_2}")
elif (D == 0):
    print(f"one suloso is x{(-b- (D)**(0.5))/(2*a)}")
    
else:
    print(f"you made a mistake")