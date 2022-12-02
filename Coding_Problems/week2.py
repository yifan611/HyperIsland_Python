

"""1. Using problem 4 in week 1, write functions for the following:
    a. Collecting the inputs for the problem. 
       Convert the inputs to the relevant types they should be.
    b. Calculating the equation given the inputs from the above.
    c. Printing your result in a preformatted string.   
    Ensure to include a main program that reads the values from the user."""
  
def converter():
    ft = float(input("Put in a value in feet: "))
    inche = round(ft*12,2)
    yard = round(ft/3,2)
    mile = round(ft/5280,2)
    # return inche, yard, mile
    print(f"{ft} feet is {inche} inches, {yard} yards, and {mile} miles.")
    # print(f"in inche, is: ", float(inche))

converter()

print(converter())
  
