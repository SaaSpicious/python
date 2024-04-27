def subtract(num1,num2):
    return num1 - num2

def addition(num1,num2):
    return num1+num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    if num2 == 0:
        return "ERROR: Division by Zero not allowed!"
    else:
        return num1/num2
    
num1=23
num2=56
print("Subtraction result: ",subtract(num1,num2));
print("Addition result: ",addition(num1,num2));
print("Multiplication result: ",multiply(num1,num2));
print("Division result: ",divide(num1,num2));