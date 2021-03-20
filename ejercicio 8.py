nI=int(input("Año inicial:")) 

nF=int(input("Año final:")) 

for n in range(nI, nF+1): 

   if not n%10==0: 

       continue 

   if not n%4==0: 

       continue 

   if n%100!=0 or n%400==0: 

       print(n) 
