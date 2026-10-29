import random
# Jacob Arzadon
# 10/29/2026

#In Class Example 1
while True:
    try:
        user_input = input("Enter some words: ")

        if user_input.strip() == "":
            print("Error: Input cannot be empty!")
        if not user_input.replace(" ", "").isalpha():
            print("Error: Letters only!")
        else:
            user_input = user_input.upper()
            print("CAPS version:", user_input)
            break

    except Exception as e:
        print("An error occurred:", e)


#In Class Example 2
while True:

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        total = num1 + num2

        print("The answer is: ", total)
        break

    except ValueError:
        print("Error: Please enter numbers only!")


#In Class Example 3
total = 0
while True:
    try:
        num = float(input("Enter a number: "))
        total += num
        print("Current total:", total)

        choice = input("Do you want to add another number? (y/n): ").lower()
        if choice == "n":
            break
        elif choice != "y":
            print("Invalid choice, please enter y or n.")

    except ValueError:
        print("Error: Please enter a valid number!")

print("Total:", total)


#In Class Example 4
while True:
    try:
        max_num = int(input("Enter the maximum number: "))

        if max_num < 1:
            print("Error: Enter a number greater than 0!")
        else:
            random_num = random.randint(1, max_num)
            print("Random number:", random_num)
            break

    except ValueError:
        print("Error: Please enter a whole number!")


#In Class Example 5
for i in range(10):
    num = random.randint(1, 100)

    if num % 2 == 0:
        print("RIGHT")
    else:
        print("LEFT")