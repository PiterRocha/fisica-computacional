#Estudo Dirigido 07 - Piter Martins Rocha

import numpy

A = numpy.array([[1,0,0], [2,3,0],[3,4,2]])
x_1 = numpy.array([[1], [1],[1]])
lambda_ = 15

def metodo_potencias(A, x_1, lambda_):
   
    print('| k  |        x^(k)       | λ^(k)| ')
    print('| %02d | (%.2f, %.2f, %.2f) | %.1f |' %(1, x_1[0][0], x_1[1][0], x_1[2][0], lambda_)) 

    k = 2
    x_k = x_1

    while k < lambda_:
        x = calcula_x(A, x_k)
        l = numpy.dot(x.T, numpy.dot(A,x))

        print('| %02d | (%.2f, %.2f, %.2f) | %.2f |' %(k, x[0][0], x[1][0], x[2][0], l[0][0]))

        x_k = x
        k += 1


def calcula_x(A,x_k):
    a = numpy.dot(A,x_k)
    b = normaliza(a)

    return a/b

def normaliza(x):
    sum = 0

    for i in x:
        for j in i:
            sum += j**2

    return sum**(1/2)
    

metodo_potencias(A, x_1, lambda_)

