#6 odd or even(array)(total)
n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the elements:")))
odd=0
even=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("The number of odd numbers is",odd)
print("The number of even numbers is",even)
