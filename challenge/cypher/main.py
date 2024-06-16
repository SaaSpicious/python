import caesar

print(caesar.logo)
next_action="yes"

while next_action=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    output = caesar.cypher(text=text, shift=shift, direction=direction)
    print(f"Your result is: {output}")
    next_action = input("Do you want to start another task? (yes/no) ")

print("Thank you for using the caesar cypher")