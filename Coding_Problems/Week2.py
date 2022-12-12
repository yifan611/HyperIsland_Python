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



"""2. Write a function that takes three numbers as parameters, 
    and returns the mean value of those parameters as its result. 
    Include a main program that reads three values from the user 
    and displays their mean."""

def scoreMean():
    score_1 = int(input("What is your chinese score?"))
    score_2 = int(input("What is your maths score?"))
    score_3 = int(input("What is your English score?"))
    score_mean = round((score_1 + score_2 + score_3) / 3, 1)
    
    if score_mean > 80:
        print("Congratulations!")
    else:
        print("You need to work harder!")
    print(f"Your mean score for this semester is {score_mean}.")    

scoreMean()



"""3. Only the words: Create a program that identifies all of the words 
    in a string entered by a user. Begin by writing a function that 
    takes a string of text as its only parameter. Your function should 
    return a list of the words in the string with the punctuation marks removed. 
    Punctuation marks include commas, periods, question marks, hyphens, 
    apostrophes, exclamation points, colons, and semicolons. 

    Hint: *****************String Operations*****************"""

import re 
    
text = str(input("How was your day today?"))

def wordsListWithoutP(text):
    textWithoutP = re.sub(r'[^\w\s]','',text)
    listText = list(textWithoutP.split())
    return listText

print(wordsListWithoutP(text))
  
    
    
"""4. Create a program that will serve as a class database and 
 will allow users to add names and scores to the database. 
 For each name and score that is added, print the dictionary database for the user.    
    Further Work:     
    1. Add an improvement to subtract scores from a given user.
    2. Add an improvement to save the database to a local file."""

import numpy as np
import csv

class_scores = {}

def addScore(studentName, score):    
   class_scores[studentName] = score  
   print(class_scores)

def subtractScores(studentName):
    if studentName not in class_scores:
       print("This student is not in class.")
    else:
        del class_scores[studentName]
        print(class_scores)

# def save_file():
#    np.save('my_file.npy', class_scores) 

def save_file():
    with open('dict.csv', 'w+', newline='') as csvfile:
        for name in class_scores.keys():
            csvfile.write(name + "," + class_scores[name] + "\n")

addScore(input("Student name: "), input("Score: "))
addScore(input("Student name: "), input("Score: "))
addScore(input("Student name: "), input("Score: "))

subtractScores(input("Remove Student name: "))

save_file()



"""5. A prime number is an integer greater than 1 that is only divisible 
    by one and itself. Write a function that determines whether or not 
    its parameter is prime, returning True if it is and False otherwise. 
    Write a main program that reads an integer from the user and displays 
    a message indicating whether or not it is a prime. Ensure tht the main 
    program will not run if the file containing your solution is imported into 
    another program."""

def prime_check(num) -> bool:
    if num >= 1 and num <=3:
        return True
    elif num<1:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True  

def print_result():
    if prime_check(num):
        print(num, "is a prime number.")
    else:
        print(num, "is Not prime number.")
        
num = int(input("Check (prime number or not) this number: "))

print_result()
