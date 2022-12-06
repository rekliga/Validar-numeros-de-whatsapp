numero = 10
numero1 = 2
n=3
numero3 = 0
base = int(numero1)
#resta
# for i in range(numero):
#     if numero1 <= numero:
#         if numero == numero1:
#             break
        
#         numero1 +=1
#         numero3 +=1

def resta(n1,n2):
    valor = 0
    while n1>n2:
        n2+=1
        valor+=1
    return valor


#print(resta(5,1))
# print(numero3)

def multiplicar(n1,n2):
    valor = 0
    for i in range(n2):
       valor +=n1 
    return valor
#print(multiplicar(5,8))

def multi(n1,n2):
    value = 0
    while(n1>0): #significa mientras n1 sea mayor que 0
        print(n1)
        n1-=1
        value+=n2
        
    return value

print(multi(5, 3))
#suma
# for i in range(numero+numero1):
#     numero3+=1

#division
def div(n1,n2):
    value = 0
    while n2<=n1:
        n1 -= n2
        value+=1
    return value,n1

print(div(15, 3))




#elevar
# for i in range(n-1):
#     #print(i)
#     numero1 = numero1*base
#     #print(numero1)
#     #print(base)

# print(numero1)


#elevar while
print("elevar")
def elevar(n1,n2):
    value = 1
    while (n2):
        #print(n2)
        n2-=1
        value = value*n1
        
    return value


print(elevar(3, 3))


print("factorial")

def factorial(n2):
    value = 1
    while(n2>0):
        
        value = value*n2
        #print(value)
        n2-=1
    return value

print(factorial(5))



print("Es primo")

def numprimo(n1):
    value = True
    for i in range(2,round(n1/2)):
        if (n1%i==0):
            #print(n1)
            value = False
    return value

print(numprimo(9))


def perfnum(n1):
    value =0
    base = n1
    for i in range(1,n1):
        if n1%i == 0:
            value +=i
    if value == n1:
        print("es un numero perfecto")
        return(value)


print(perfnum(14))