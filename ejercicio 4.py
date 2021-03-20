r=2
n = int(input("Número: "))
f = n*r
print("el resultado de la operacion",f)
print("los numeros que cuenta antes del resultado: ")
for x in range(n,f):
    print(x)
