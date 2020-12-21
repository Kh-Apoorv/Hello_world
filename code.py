

import math


def greet():
    name = input('whats ur name')
    print('hello',name)
def add(h):
    ak=sum(h)
    return ak
def mul(o):
    c = 1
    for j in o:
        c=c*j
    return c

def fact(h):
    if h==0:
        return 1
    n= h*fact(h-1)
    return n

greet()
w=int(input('what uh want'
            '\n   1-addition' 
            '\n  2-multiplication'
            '\n  3-division of 2 numbers'
            '\n  4-factorial'
            '\n  5-area of 2-d objects'
            '\n  6- trignometric values of certain number'))
if w==1:
    n=int(input('the count of number that is wanted to be added '))
    lst=[]
    for i in range(n):
            f=int(input('enter the number'))
            lst.append(f)
            i+=1
    print(lst)
    ak=add(lst)
    print(ak)
    print('thanks and bye')

elif w==2:
    r=[]
    y=int(input('enter the count'))
    for i in range(y):
        t=int(input('the numnbers'))
        r.append(t)
        i+=1
    print(r)
    g=r
    c=mul(g)
    print(c)
    print('thanks and bye')
elif w==3:
    r= int(input('first value rather than zero'))
    t= int(input('second value rather than zero'))
    f= r/t
    print(f)
    print('thanks and bye')
elif w==4:
    u=int(input('enter the number uh want factorial of'))
    n=fact(u)
    print(n)
    print('thanks and bye')
elif w==5:
    l=int(input('what area uh want'
                '\n  1-triangle'
                '\n  2-circle'
                '\n  3-rectangle'
                '\n  4-square'))
    if l==1:
        aa=int(input('base of triangle'))
        ab = int(input('altitude of triangle'))
        g=.5*aa*ab
        print('the area of triangle is' ,g)
        print('thanks and bye')
    elif l==2:
        cc=int(input('radius of circle'))
        ac= 3.14*cc*cc
        print('the area of circle is',ac )
        print('thanks and bye')
    elif l==3:
        rl=int(input('the lenght of rectamngle is'))
        rw = int(input('the witdh of rectamngle is'))
        ra= rl*rw
        print('the area of rectangle is ',ra)
        print('thanks and bye')
    elif l==4:
        ss = int(input('the side of square is'))
        sa= ss*ss
        print('the area of square is ',sa)
        print('thanks and bye')
    else:
        print('inalid option')
        print('bye')
elif w==6:
    trig=int(input('enter the number,uh want trignometric values in radians'))
    print('sin',math.sin(trig))
    print('cos',math.cos(trig))
    print('tan',math.tan(trig))
    print('thanks and bye')
else:
    print('invaid option')
    print('ok bye')








