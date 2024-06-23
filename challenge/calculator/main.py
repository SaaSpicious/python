import art


def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1,n2):
    return n1 / n2

def multiply(n1,n2):
    return n1 * n2

operators = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}
print(art.logo)
num1 = float(input("What's the first number to process?: "))

next_operation = "yes"
while next_operation == "yes":
    print("Which of the following operations do you want to execute? ")
    for n in operators:
        print(n)

    operation = ""
    while not operation in operators:
        operation = input()

    num2 = float(input("What's the second number to process?: "))

    calc_function = operators[operation]
    solution = calc_function(num1,num2)

    print(f"Your solution is {solution}!")
    next_operation=input("Do you want to run another operation (yes/no) ")
    num1=solution

print("Thank you for using the calculator!")