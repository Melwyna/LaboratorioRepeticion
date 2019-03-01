contpa=0
for a in range (1, 1000000000000):
 a=int(input("Ingrese un numero:"))
 if (a%2==0):
  contpa+=1
 else:
  if (a%2!=0):
    break
print ("hubieron", contpa, "pares")