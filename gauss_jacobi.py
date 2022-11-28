#Estudo Dirigido 07 - Piter Martins Rocha

x_zero = [0.7, -1.6, 0.6]
epsilon = 0.05

def gauss_jacobi(x_zero, epsilon):
    x_k_menos_um = x_zero

    d = epsilon

    while d >= epsilon:
        x_1 = (7 - 2 * x_k_menos_um[1] - x_k_menos_um[2])/10
        x_2 = (-8 - x_k_menos_um[0]-x_k_menos_um[2])/5
        x_3 = (6 - 2 * x_k_menos_um[0] - 3 * x_k_menos_um[1])/10

        x_k = [x_1, x_2, x_3]
        
        d = calcula_d(x_k_menos_um, x_k)

        x_k_menos_um = x_k

    return d


def calcula_d(x_k_menos_um, x_k):
    x = []

    for i in range(len(x_k)):
        x.append(x_k[i] - x_k_menos_um[i])

    a = abs(max(x,key=abs))
    b = abs(max(x_k,key=abs))

    return a/b


d = gauss_jacobi(x_zero, epsilon)
print('d = %.5f' %d)


