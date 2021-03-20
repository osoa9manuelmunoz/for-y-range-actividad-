n = int(input("ingrese un numero: "))
factorial = 1
for i in range(n):
    print ( factorial, " * " ,n )
    factorial = factorial * n
    n -= 1
    print("el factorial es",factorial)