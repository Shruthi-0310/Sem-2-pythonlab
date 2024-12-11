#7 uppercase and lowercase count
"""
n=input("Enter a jumbled sentence = ")
uppercase_count=0
lowercase_count=0

for char in n:
    if char.isupper():
        uppercase_count +=1
    elif char.islower():
        lowercase_count +=1

print(f"Number of uppercase letters : {uppercase_count}")
print(f"Number of lowercase letters : {lowercase_count}")
"""

#use this
def count_let(string):
    ucase=0
    lcase=0
    for char in string:
        if char.isupper():
            ucase+=1
        elif char.islower():
            lcase+=1
    return ucase,lcase
string=input()
u,l=count_let(string)
print("Upper case",u)
print("Lower case",l)
