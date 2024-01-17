import math
print("                              MENU                           ")
print("investment - to calculate the amount of interest you will earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("")


menu = str(input("Please enter either 'investment' or 'bond' from the menu above to proceed: "))
# Any case input is allowed using the lower function.
menu = menu.lower()
print(menu)
# Here I've added an error while loop to ensure that the user enters either investment or bond.
while menu not in ["investment", "bond"]:
    print("error...")
    menu = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ")
    menu = menu.lower()
    print(menu)

if menu == "investment":
        p = int(input("Please enter the amount of money you are depositing: "))
        r = int(input("Please enter the interest rate e.g. 8 if 8%: "))
        t = int(input("Please enter the number of years you are planning on investing:  "))

        interest = str(input("Please enter 'simple' or 'compound' interest:  "))
        interest = interest.lower()
        print(interest)
        # I've added an error while loop to ensure that the user enters either simple or compound.
        while interest not in ["simple", "compound"]:
            print("error...")
            interest = input("Please enter either 'simple' or 'compound' from the menu above to proceed: ")
            interest = interest.lower()
            print(interest)
        if interest == "simple":
            print(f"The amount you will get back on your investment after the given period is: {int(p * (1 + (r/100)*t))}.")
        if interest == "compound":
            # I've used the math.pow function to calculate the compound interest.
            print(f"The amount you will get back on your investment after the given period is: {int(p * math.pow((1 + (r/100)),t))}.")
# Cast the interest formulae from strings to integers to enable the calculations.
if menu == "bond":
        
        p = int(input("Please enter the present value of the house: "))
        i = int(input("Please enter the interest rate: "))
        n = int(input("Please enter the number of months you plan to take to repay the bond e.g. 120 months: "))
        #I used f statement to print the monthly repayment.
        print(f"Your monthly repayment is: {(int((i/100/12) * p)/(1 - (1 + (i/100/12))**(-n)))}.")
        