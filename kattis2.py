while True:
       ligne1=input()
       if not ligne1:
              break
       n1,n2=map(int, ligne1.split())
       if not ligne2:
              break
       ligne2=input()
       if not ligne3:
              break
       ligne3=input()
       n3,n4=map(int, ligne2.split())
       n5,n6=map(int, ligne3.split())
       if(n1,n2,n3,n4,n5,n6 > 0):
              if(n1>0 and n1<10**15):
                     if(n2>0 and n2<10**15):
                            if(n3>0 and n3<10**15):
                                   if(n4>0 and n4<10**15):
                                          if(n5>0 and n5<10**15):
                                                 if(n6>0 and n6<10**15):
                                                        print(abs(n1-n2))
                                                        print(abs(n3-n4))
                                                        print(abs(n5-n6))


