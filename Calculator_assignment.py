num_1 = float(input("Enter First Number: "))
num_2 = float(input("Enter Second Number: "))
function = input("Enter the function you want to perform (+, -, *, /): ")

if function == "+":
    Answer = num_1 + num_2
elif function == "-":
    Answer = num_1 - num_2
elif function == "*":
    Answer = num_1 * num_2
elif function == "/":
    Answer = num_1 / num_2
else:
    Answer = "Invalid function"
    print("Invalid function. Please enter +, -, *, or /.")
    
print (num_1, function, num_2, "=", Answer)