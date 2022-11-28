#Estudo Dirigido 03 - Interpolação de Lagrange - Piter Martins Rocha

x = [-1, 0, 2]
y = [4, 1, -1]

def lagrange(x,y,z):
    n = len(x)

    sum = 0
    k = 0
    while k < n:
        sum += y[k]*L(k,x,z)
        k += 1

    return sum    


def L(k, x, z):
    n = len(x)
    
    a = 1
    b = 1

    j = 0
    while j < n:
        if j != k:
            a *= (z-x[j])
            b *= (x[k] - x[j])
        
        j+=1

    return a/b


print('%1.5f' %lagrange(x,y,1))