#Exercise1
print("this is \\\ double backslash")
print("these are /\\/\\/\\/\\ mountains")
print("he is \t awesome")
print('\\\" \\n \\t \\\'')
#Exercise2
num1,num2,num3=input("enter three numbers comma seperated:").split(",")
print(f"{(int(num1)+int(num2)+int(num3))/3}")
#Exercise3
a=input("Please enter your name: ")
print(a[-1::-1])
# Exercise4
winning_number=11
user_input=int(input("guess any number between 1 and 20:"))
if user_input== winning_number:
    print("YOU WON")
else:
    if user_input> winning_number:
        print("TOO HIGH")
    else:
        print("TOO LOW")
#Exercise5
user_name=input("Please enter your name: ")
user_age=int(input("Please enter your age: "))
if user_age>= 14 and user_name[0]=='a' or user_name[0]=='A':
    print('You can watch COCO')
else:
    print("You can't watch COCO")
# Exercise6
n=int(input("enter a number: "))
s=0
i=1
while i<=n:
    s+=i
    i+=1
print(s)
# Exercise7
number=input("Please enter a number: ")
s=0
i=0
while i < len(number):
    s+=len(number[i])
    i+=1
print(s)
#Exercise8
name=input("Please enter your name: ")
temp_var=""
i=0
while i< len(name):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f"{name[i]}:{name.count(name[i])}")
    i+=1