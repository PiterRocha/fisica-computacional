# ESTUDO DIRIGIDO 04 - Piter Martins Rocha

def metodo_newton(x,y):
    i = y
    d = [i[0]]

    while len(i) > 2: 
        j = []

        k = 0
        while k < len(i)-1:
            
            j.append((i[k+1]-i[k])/(x[k+1]-x[k]))
            k += 1

        
        d.append(j[0])
        i = j

    d.append((i[1]-i[0])/(x[-1]-x[0]))
    

    return d

def interpolacao(x,y,z):
    d = metodo_newton(x,y)

    m = len(x)

    p = d[0]

    i = 1
    while i < m:
        k = d[i]
        j = 0
        while j < i:
            k *= (z - x[j])
            j+=1
        i+=1

        p += k

    return p

#exercício 2
x = [-1,0,2]
y = [4,1,-1]

m = len(x)
d = metodo_newton(x,y)
print('+------------------------------------------+')
i=0
while i < len(d):
    print('d%d = %f' %(i, d[i]))
    i += 1

z = 1
p = interpolacao(x,y,z)
print('P_%d(%d) = %f' %(m-1, z, p))

#exercício 3
x = [20,25,30,35,40,45,50]
y = [0.99907,0.99852,0.99826,0.99818,0.99828,0.99849,0.99878]

print('+------------------------------------------+')
z = 32.5
p = interpolacao(x,y,z)
print("Calor específico da água a 32.5°C: %.5f" %p)
z = 0.99837
p = interpolacao(y,x,z)
print("A temperatura do calor específico %.5f é de %.2f °C" %(z,p))
print('+------------------------------------------+')