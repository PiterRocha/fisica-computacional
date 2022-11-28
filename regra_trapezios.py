# Estudo Dirigido 06 - Piter Martins Rocha

import math

x = [-1,0,1,2,3]
y = [1,1,0,-1,2]

# Exercício 2
def metodo_dos_trapezios(x,y):
    h = (x[1]-x[0])
    n = len(x)

    sum = 0

    i = 1
    while i < n-1:
        sum += y[i]

        i+=1

    sum = 2*sum + y[0] + y[n-1]

    return h/2 * sum

print('--------------------------------------')
print('Exercício 2:')
print()
print('I =',metodo_dos_trapezios(x,y))
print()

# Exercício 3
def funcao(x):
    return 1/x

def metodo_dos_trapezios_2(a,b,m):
    h = (b-a)/m
    
    x = conj_x(a,b,h)
    y = f(x)

    sum = 0

    i = 1
    while i <= m-1:
        sum += y[i]

        i+=1

    sum = 2*sum + y[0] + y[m]
 
    return h/2 * sum


def conj_x(a,b,h):
    x = []
    i = a
    while i < b:
        x.append(i)
        i+=h
    
    x.append(b)

    return x

def f(x):
    y = []
    for i in x:
        y.append(funcao(i))

    return y

print('--------------------------------------')
print('Exercício 3:')
print()
print('I = %.4f' %metodo_dos_trapezios_2(1,3,4))
print()

#Exercício 4
def funcao(x):
    return math.exp(x)

print('--------------------------------------')
print('Exercício 4:')
print()
# m = 10
print('m = 10    | I = %.6f' %metodo_dos_trapezios_2(0,1,10))
# h = 0,01
print('h = 0,01  | I = %.6f' %metodo_dos_trapezios_2(0,1,100))
# h = 0,001
print('h = 0,001 | I = %.6f' %metodo_dos_trapezios_2(0,1,1000))
print()

#Exercício 5
def metodo_simpson(a,b,m):
    h = (b-a)/m
    
    x = conj_x(a,b,h)
    y = f(x)

    sum_i = 0
    sum_p = 0

    i = 1
    while i <= m-1:
        if i % 2 == 0:
            sum_p += y[i]
        else:
            sum_i += y[i]

        i+=1

    sum = 4*sum_i+ 2*sum_p + y[0] + y[m]
 
    return h/3 * sum

def funcao(x):
    return 1/(1+x)

print('--------------------------------------')
print('Exercício 5:')
print()
print('I = %.4f'%metodo_simpson(0,3,6))
print()

#Exercício 6
def funcao(x):
    return math.exp(x)

print('--------------------------------------')
print('Exercício 6:')
print()
# m = 10
print('m = 10    | I = %.12f'%metodo_simpson(0,1,10))
# h = 0,01
print('h = 0,01  | I = %.12f'%metodo_simpson(0,1,100))
# h = 0,001
print('h = 0,001 | I = %.12f'%metodo_simpson(0,1,1000))
print()

print('--------------------------------------')

