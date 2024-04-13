N=int(input())
if(1<=N<=10**4):
        if(N%10**4!=0):  
                print((N//100)*100+99)
        if(N%10**4==0):
                print(N-1)
