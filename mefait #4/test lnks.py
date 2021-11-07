import math
dist=lambda x,y:math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return '({},{})'.format(self.x,self.y)
    def __repr__(self):
        return 'Point({},{})'.format(self.x,self.y)
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __ne__(self,other):
        return not self==other
    def __lt__(self,other):
        return self.x<other.x or (self.x==other.x and self.y<other.y)
    def __le__(self,other):
        return self<other or self==other
    def __gt__(self,other):
        return not self<=other
    def __ge__(self,other):
        return not self<other
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        return Point(self.x*other,self.y*other)
    def __rmul__(self,other):
        return Point(self.x*other,self.y*other)
    def __truediv__(self,other):
        return Point(self.x/other,self.y/other)
    def __floordiv__(self,other):
        return Point(self.x//other,self.y//other)
    def __mod__(self,other):
        return Point(self.x%other,self.y%other)
    def __divmod__(self,other):
        return (Point(self.x//other,self.y//other),Point(self.x%other,self.y%other))
    def __pow__(self,other):
        return Point(self.x**other,self.y**other)
    def __rpow__(self,other):
        return Point(other**self.x,other**self.y)
    def __neg__(self):
        return Point(-self.x,-self.y)
    def __pos__(self):
        return Point(+self.x,+self.y)
    def __abs__(self):
        return Point(abs(self.x),abs(self.y))
    def __invert__(self):
        return Point(1/self.x,1/self.y)
    def __round__(self,n=0):
        return Point(round(self.x,n),round(self.y,n))
    def __floor__(self):
        return Point(math.floor(self.x),math.floor(self.y))
    def __ceil__(self):
        return Point(math.ceil(self.x),math.ceil(self.y))
    def __trunc__(self):
        return Point(math.trunc(self.x),math.trunc(self.y))
    def __iadd__(self,other):
        self.x+=other.x
        self.y+=other.y
        return self
    def __isub__(self,other):
        self.x-=other.x
        self.y-=other.y
        return self
    def __imul__(self,other):
        self.x*=other
        self.y*=other
        return self
    def __itruediv__(self,other):
        self.x/=other
        self.y/=other
        return self
    def __ifloordiv__(self,other):
        self.x//=other
        self.y//=other
        return self
    def __imod__(self,other):
        self.x%=other
        self.y%=other
        return self
    def __ipow__(self,other):
        self.x**=other
        self.y**=other
        return self
    def __iabs__(self):
        self.x=abs(self.x)
        self.y=abs(self.y)
        return self

class linkedNode():

    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)
    def __eq__(self,other):
        return self.data==other.data
    def __ne__(self,other):
        return not self==other
    def __lt__(self,other):
        return self.data<other.data
    def __le__(self,other):
        return self<other or self==other
    def __gt__(self,other):
        return not self<=other
    def __ge__(self,other):
        return not self<other
    def __add__(self,other):
        return linkedNode(self.data+other.data,self.next+other.next)
    def __sub__(self,other):
        return linkedNode(self.data-other.data,self.next-other.next)
    def __mul__(self,other):
        return linkedNode(self.data*other,self.next*other)
    def __rmul__(self,other):
        return linkedNode(self.data*other,self.next*other)
    def __truediv__(self,other):
        return linkedNode(self.data/other,self.next/other)
    def __floordiv__(self,other):
        return linkedNode(self.data//other,self.next//other)
    def __mod__(self,other):
        return linkedNode(self.data%other,self.next%other)



    

# all the following functions are not defined in the Point class
# but in the module math
def acos(x):
    return math.acos(x)
def asin(x):
    return math.asin(x)
def atan(x):
    return math.atan(x)

# i'm not sure if this is the best way to do it
# but it works

# i love this function
def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

# it's not a prime number if it's divisible by 2 or 3
def is_prime2(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    if n%3==0:
        return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0:
            return False
        if n%(i+2)==0:
            return False
    return True

#the main life of the program
def main():
    print("Welcome to the prime number generator!")
    print("This program will generate prime numbers")
    print("between two numbers you choose.")
    print("")
    print("Please enter the first number:")
    a=int(input())
    print("Please enter the second number:")
    b=int(input())
    print("")
    print("The prime numbers between",a,"and",b,"are:")
    for i in range(a,b+1):
        if is_prime2(i):
            print(i)
    print("")
    print("Thank you for using the prime number generator!")
# robots are not welcome
#the meaning of life is 42
#did you know that the square root of 42 is 6?
#i'm not sure if this is the best way to do it
# but it works
#stop asking me to explain this
# i love this function
# github is the best thing ever
# i love github
# i love github
# i love ArithmeticError(division by zero)

# i make love to the people who use this program
# i love you
# i love you
# the people who use this program are the best
# i love you
# but me too
# i love you
# purple is the best color
# i love you
# the best color is purple
# mdrs are the best
# python is the best
# olivia is the best
# damn it
# people from the internet are the best
# people from france are the worst
# i love you
# 2b2t is the best
# 2b or not 2b is the best
# debuggers are the best
if __name__=='__main__':
    p1=Point(1,2)
    p2=Point(3,4)
    a=linkedNode(data=p1,next=linkedNode(data=p2))
    print(a)
    print(p1)
    print(p2)
    print(p1==p2)

