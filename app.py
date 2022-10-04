n = input("enter number of students: ")
x=1;sum=0
while(not n.isdigit() or int(n)<=0):
    n = input("enter number di ai sus: ")

n = int(n)
for i in range(1,n+1):
    sum+=int(input(f"enter score student {i} di sus: "))
print(sum)