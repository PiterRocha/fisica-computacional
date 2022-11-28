#Projeto Final - Piter Martins Rocha

import matplotlib.pyplot as plt
import numpy as np
import csv

#Extrai as colunas do arquivo .csv e as converte em listas x e y
def csv_to_list():
    x = []
    y = []

    c = open('tabela.csv', 'r')
    tabela = csv.DictReader(c)

    for col in tabela:
        x.append(float(col['x']))
        y.append(float(col['y']))

    return x,y

#Extrai os valores do total da soma de x, y, x*y e x**2
def valores(x,y):
    n = len(x)
    
    sum_x = 0
    sum_x2 = 0
    for i in x:
        sum_x += i
        sum_x2 += i**2

    sum_y = 0
    for i in y:
        sum_y += i

    sum_xy = 0
    for i in range(n):
        sum_xy += x[i]*y[i]
        i+=1

    val = [sum_x, sum_y, sum_xy, sum_x2]

    return val

#Calcula os coeficientes a e b
def calcula_coeficientes(x,y):
    val = valores(x,y)

    n = len(x)
    sum_x = val[0]
    sum_y = val[1]
    sum_xy = val[2]
    sum_x2 = val[3]

    a = (n*sum_xy - sum_x*sum_y)/(n*sum_x2 - sum_x**2)
    b = (sum_x*sum_xy - sum_y*sum_x2)/(sum_x**2-n*sum_x2)

    return a,b

#Imprime a tabela de dados
def imprime_tabela(x,y):
    print('Tabela')
    print()
    eixo_x = x.copy()
    eixo_y = y.copy()
    eixo_x.insert(0,'X')
    eixo_y.insert(0,'Y')
    tabela = [eixo_x,eixo_y]
    f = '{:>8} ' * len(tabela)
    for i in zip(*tabela):
        print(f.format(*i))

#Plota o gráfico e imprime a equação da reta
def plot_graf(x,y,a,b):
    
    eq = '%.5fx%+.5f' %(a,b)
    print('Equação da Reta:', eq )
    
    print()

    print('Gráfico:')
    titulo = 'Gráfico de '+ eq
    plt.title(titulo)    
    x = np.array(x)
    y = np.array(y)
    plt.plot(x, y, 'o')
    plt.plot(x, a*x+b, color='red')
    plt.show()

x,y = csv_to_list()

a,b = calcula_coeficientes(x,y)

imprime_tabela(x,y)
print()
plot_graf(x, y, a, b)





