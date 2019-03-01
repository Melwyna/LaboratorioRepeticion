contmay=0
contmen=0
contcer=0
for n in range (1, 11):
 n=int(input("ingrese los numeros"))
 if (n>0):
  contmay+=1
 if (n<0):
  contmen+=1
 if (n==0):
  contcer+=1
print ("hubieron", contmay, "numeros mayores que cero", "y hubieron", contmen, "numeros menores que cero", "y", contcer, "numeros iguales a cero")