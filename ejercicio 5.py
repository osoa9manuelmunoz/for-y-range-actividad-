global t 
t = (input("ingrese su frase: "))

con=0
for i in t:
   if(i.isalpha()):
      con+=1
print("la cantidad de letras son: ",con)