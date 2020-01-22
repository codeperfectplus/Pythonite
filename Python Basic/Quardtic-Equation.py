""" ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0 """
import cmath
def quardtic(a,b,c):                 #ax2 + bx + c = 0
    d = (b**2) -(4*a*c)
    sol1 = (-b -cmath.sqrt(d))/(2*a)
    sol2 = (-b +cmath.sqrt(d))/(2*a)
    return sol1,sol2

a, b, c=1, 5, 6
answer = quardtic(a,b,c)
print(answer)