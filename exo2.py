s=0
for i in range (1,4):
     n2=float(input(f"taille numero {i}: "))
     if n2 < 170 :
        s+=1   
        i+=1
        continue
print("le nombre de taille inférieur à 170cm est ",s)