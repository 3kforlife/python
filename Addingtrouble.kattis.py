nombres=input()
nbres3=nombres.split()
try:
     A=int(nbres3[0])
     B=int(nbres3[1])
     C=int(nbres3[2])
     if(A>=-10**9 and A<=10**9):
            if(B>=-10**9 and B<=10**9):
                if(C>=-10**9 and C<=10**9):
         
                     if(A+B==C):
                            print("correct!")
                     if(A+B!=C):
                            print("wrong!")

except ValueError:
     print("entrer des nombres séparer par des espaces")


    


