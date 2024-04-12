while True:
    n,cpt,som=int(input("entier positif:")),0,0
    if (n>0 and n<21):
        while(cpt<n):
            cpt+=1
            som+=cpt
        break
    print("saisie incorrecte")
print("somme= ",som)

 








