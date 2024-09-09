#Name: Tawonga Taibu
#Task Name: Capstone Project Variables and Data Types
#Task Number: 14

import math  # extends the list of mathematical functions


def get_valid_selection():
    '''
    This function gets prompts the user to enter a prefered selection depending on how '
    they want to purchase their property. It returns the prefered selection and ultimately
    uses that selection to handle the rest of the calculations.
    '''
    while True:
        selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
        if selection in ['investment', 'bond']:
            return selection
        else:
            print("Invalid selection. Please choose either 'investment' or 'bond'.")

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

#Calling the 'get_valid_selection' function
selection = get_valid_selection()

if selection == "investment":
    try:
        P = float(input("Please enter the money you're investing (P): "))
        r = float(input("Please enter the interest rate (r): ")) / 100
        t = int(input("Please enter your investment duration in years (t): "))
        interest = input("Please select the type of interest you're using (simple or compound): ").lower()

        if interest == "simple":
            A = round(P * (1 + r * t), 2)
            print("The total amount is:", A)
        elif interest == "compound":
            A = round(P * math.pow((1 + r), t), 2)
            print("The total amount is:", A)
        else:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")
    
    except ValueError:
        print("Invalid input. Please enter numerical values for money, interest rate, and duration.")
    
elif selection == "bond":
    try:
        P = float(input("Please enter the value of the house: "))
        i = (float(input("Please enter the annual interest rate (as a percentage): ")) / 100) / 12
        n = int(input("Please enter the number of months for repayment: "))
        repayment = round((i * P) / (1 - (1 + i) ** (-n)), 2)
        print("Your monthly repayment is:", repayment)
    
    except ValueError:
        print("Invalid input. Please enter numerical values for house value, interest rate, and number of months.")

#References
#https://www.w3schools.com/python/python_functions.asp