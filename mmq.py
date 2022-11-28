# Estudo Dirigido 05 - Piter Martins Rocha

import numpy

x = [1,2,3,4,5]
y = [1.3,3.5,4.2,5.0,7.0]

def g_1(i):
    return x[i]

def g_2():
    return 1

def a_11(x):
    m = len(x)
    a = 0
    
    for i in range(m):
        a += g_1(i) * g_1(i)

    return a

def a_12(x):
    m = len(x)
    a = 0

    for i in range(m):
        a += g_1(i) * g_2()

    return a

def a_22(x):
    m = len(x)
    a = 0

    for i in range(m):
        a += g_2() * g_2()

    return a

def b_1(x,y):
    m = len(x)
    b = 0

    for i in range(m):
        b += g_1(i) * y[i]

    return b


def b_2(x,y):
    m = len(x)
    b = 0

    for i in range(m):
        b += g_2() * y[i]

    return b

alpha_1 = (b_1(x,y)*a_22(x)-b_2(x,y)*a_12(x))/(a_11(x)*a_22(x)-a_12(x)*a_12(x))
alpha_2 = (b_2(x,y)*a_11(x)-b_1(x,y)*a_12(x))/(a_22(x)*a_11(x)-a_12(x)*a_12(x))

print('--------------------------------------')
print('Exercício 2:')
print('α1 =', alpha_1)
print('α2 =', alpha_2)
print('Φ(x)=',alpha_1 ,'x +', alpha_2)
print()

x = [0.2,1,2,3,4]
y = [4,1.8,0.7,0.25,0.1]

h = []
for i in y:
    h.append(numpy.log(i))


alpha_0 = (b_2(x,h)*a_11(x)-b_1(x,h)*a_12(x))/(a_22(x)*a_11(x)-a_12(x)*a_12(x))
alpha_1 = (b_1(x,h)*a_22(x)-b_2(x,h)*a_12(x))/(a_11(x)*a_22(x)-a_12(x)*a_12(x))

print('--------------------------------------')
print('Exercício 3:')
print('α0 =', alpha_0)
print('α1 =', alpha_1)

print('ln(Φ(t)) = %1.2f %1.2f t' %(alpha_0, alpha_1))
print()