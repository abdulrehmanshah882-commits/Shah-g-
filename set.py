aa = "This is the peograme for all sets method \n  Sets are here : \n"
bb= aa.upper()
print(bb.center(90))
set1={1,3,5,5,7,7,5,8,4,8,}
set2={6,8,9,6,7,9,3,8,4,7,}
set3={"shah","rumaiz","ghani","shameer","adnan"}
set4={"awais","hamza","zaid","shah","shameer"}
print(set1,"\n" ,set2 ,"\n" ,set3 ,"\n" ,set4)
a ="There are set methods in down"
b=a.upper()
print("\n")
print(b.center(80))
c=input("What is your choice in numbers : \n1 union , 2 intersection ,  3 update , 4 synmeteic_difference  \n 5 difference , 6  isdisjoint , 7 issuperset , 8 issubset , 9 add\n 10 remove , 11 discard , 12 pop , 13 del , 14 clear   : ".upper().center(20))
if c == "1" :
    print( "union =", set1.union(set2))  
    print(set3.union(set4)) 
elif c  == "2":
    print( "intersection =" ,set1.intersection(set2), "\n" ,set3.intersection(set4))
    
elif c=="3":
    set1.update(set2)
    print( "update set1 =", set1 )
    set3.update(set4)
    print( "update set3 =", set3)
    
elif c == "4" :
    print( "symmatric_difference of set1 ="  ,set1.symmetric_difference(set2) ,"\n", "symmetric_difference of set3 =", set3.symmetric_difference(set4) )   
elif c=="5":
    print( "difference =" , set1.difference(set2) ,"\n" ,"difference =" ,set3.difference(set4))
elif c== "6" :
    print(set1.isdisjoint(set2), "\n"  ,set3.isdisjoint(set4))
elif c == "7":
    print(set1.issuperset(set2), "\n" ,set3.issuperset(set4))
    
elif c =="8" :
    print(set1.issubset(set2), "\n", set3.issubset(set4))
elif c == "9":
         f=input("what is the set number : ")
         e =input("Enter any number that you want to add  : ")
         if f == "1":
                set1.add(e)
                print(set1)
                
         elif f =="2":
                set2.add(e)
                print(set2)
         elif f== "3":
            
                 set3.add(e)
                 print(set3)
         elif f =="4":
                set4.add(e)
                print(set4)
elif c == "10" :
         ff=input("what is the set number : ")
         ee=input("Enter any number that you want to remove : ")
         if ff== "1":
                set1.remove(ee)
                print(set1)
                
         elif ff=="2":
                set2.remove(ee)
                print(set2)
         elif ff== "3":
            
                 set3.remove(ee)
                 print(set3)
         elif ff=="4":
                set4.remove(ee)
                print(set4)
elif c == "11"  :
          fff=input("what is the set number : ")
          eee=input("Enter any number that you want to discard : ")
          if fff== "1":
                set1.discard(eee)
                print(set1)
                
          elif fff=="2":
                set2.discard(eee)
                print(set2)
          elif fff== "3":
            
                 set3.discard(eee)
                 print(set3)
          elif fff=="4":
                set4.discard(eee)
                print(set4)

elif c == "12" :
                 fef=input("what is the set number : ")
                 if fef== "1":
                        mm=set1.pop()
                        print(set1)
                        print( "poped item =", mm)
                 elif fef == "2":
                        nn=set2.pop()
                        print(set2)
                        print( "poped item =", nn)
                 elif fef == "3":
                        mn=set3.pop()
                        print(set3)
                        print( "poped item =", mn)      
                 elif fef == "4":
                        nm=set4.pop()
                        print(set4)
                        print( "poped item =", nm)     
elif c == "13" :
                         fee=input("what is the set number that you want to del : ")
                         if fee == "1":
                                del set1
                                print("set 1 is deleted")
                         elif fee == "2":
                                del set2
                                print("set 2 is deleted")         
                         elif fee == "3":
                                del set3
                                print("set 3 is deleted")       
                         elif fee == "4":
                                del set4
                                print("set 4 is deleted")
                                
elif c == "14" :
                              feee=input("what is the set number that you want to del : ")
                              
                              if feee == "1":
                                set1.clear()
                                print("set 1 is cleared")
                              elif feee == "2":
                                set2.clear()
                                print("set 2 is cleared")         
                              elif feee == "3":
                                set3.clear()
                                print("set 3 is cleared")       
                              elif feee == "4":
                                set4.clear
                                print("set 4 is cleared")
                                
else :
                              print("Invalid choice please enter from given numbers")                              
                              
         
  
