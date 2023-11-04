#func for 2 number

def add(x,y):
    return x + y
def substract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def devide(x,y):
    return x / y
def power(x, y):
    return pow(x,y)

#take input

print("select operation.")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
print("5.power")
choice = input("Enter choice :")
num1 = int(input("enter number one :"))
num2 = int(input("enter number two :"))

#if result

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",substract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=",devide(num1,num2))
elif choice == '5':
    print(num1,"^",num2,"=",power(num1,num2))
else:
    print("invalid input")
