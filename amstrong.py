 
s=int(input("Enter any number: "))
x=list(map(int,str(s)))
y=list(map(lambda x:x**3,x))
if(sum(y)==s):
    print("yes")
else:
    print("no ")
