""" Arithmetic

1. Create a program that reads two integers, **a** and *b*, from the user. Your program should compute and display:
    1. The sum of **a** and **b.**
    2. The difference when **b** is subtracted from *a*
    3. The product of **a** and *b*
    4. The quotient when **a** is divided by *b*
    5. The remainder when **a** is divided by *b*
    6. The result of $log_{10}a$
    7. The result of $a^b$
    
    ****************************Hint: ***The `math` module may contain some advanced mathematical operations. Also you can use the python inbuilt `input()` command to receive input from the user. """

# collect input from user for a and b
a = int(input("Input a number: "))
b = int(input("Input a number: "))
# 1. The sum of **a** and **b.**
sum_num = a + b
print(sum_num)
#2. The difference when **b** is subtracted from *a*
diff_num = abs(a - b)
print(diff_num)
#3. The product of **a** and *b*
pro_num = a * b
print(pro_num)
#4. The quotient when **a** is divided by *b*
quo_num = a // b
print(quo_num)
#5. The remainder when **a** is divided by *b*
rem_num = a % b
print(rem_num)


"""# 2. In the US, fuel efficiency for vehicles is normally expressed in miles-per-gallon (*MPG*). In Canada, fuel efficiency is normally expressed in liters-per-hundred-kilometers *(L/100 km)*. Use your research skills to determine how to convert from *MPG* to *L/100 km*. Then create a program that reads a value from the user (in American units) and displays the equivalent fuel efficiency in Canadian units.
    
#     ************Hint:************ ********************You can use Google to research and use both the `input()` command to receive user input and the `print()` command to return results to the console or the terminal.*"""

mpg = float(input("MPG: "))  
l100km = 2.35 * mpg
  
print(f"{mpg} is {l100km} L/100KM.")



""" 3. The surface of the earth is curved, and the distance between degrees of longitude varies with latitude. As a result, finding the distance between two points on the surface of the earth is more complicated than simply using the Pythagorean theorem. The equation for finding the distance between two points on the surface of the earth in kilometers is given by:
    
     $distance = 6371.01 \times arccos(sin(lat_1) \times sin(lat_2)+cos(lat_1)\times cos(lat_2)\times cos(long_1-long_2))$
    
     where: $(lat_1, long_1)$ and $(lat_2,long_2)$  are the latitude and longitude of two points on the Earth’s surface.
    
     Create a program that allows the user to enter the latitude and longitude of two points on the Earth in degrees. Your program should display the distance between the points in kilometers.
    
     Also assuming we travel using an aeroplane that is moving at a minimum speed of `740 km/h` how long will it take us to travel that distance?
    
     ************Hint:************ ****************Allow your program receive 4 user inputs for 4 different latitudes and longitudes on the earth. Choose any 2 locations using google maps (or google search) and get their latitude and longitude values. When printing the outputs, use the names of the locations to display the distance between locations. Longitude and latitude values are usually shown in degrees, while python usually calculates trigonometric functions using radians, therefore you will need to first convert the values to radians to use in the equation. Precedence of operations is important. Use `math` module*"""


import math

country_depart = input("Depart country: ")
country_arrive = input("Arrive country: ")

lat_dep = math.radians(float(input("latitude of depart country: ")))
long_dep = math.radians(float(input("longitude of depart country: ")))

lat_arr = math.radians(float(input("latitude of arrive country: ")))
long_arr = math.radians(float(input("longitude of arrive country: ")))

distance = 6371.01*math.acos(math.sin(lat_dep)*math.sin(lat_arr)+math.cos(lat_dep)*math.cos(lat_arr)*math.cos(long_dep-long_arr))



"""4. Distance units: Create a program that begins by reading a measurement from the user in feet. Then your program should display the equivalent distance in inches, yards and miles. Use your research skills to look up the necessary conversion factors.
    
     ************Hint:************ ******************Use the `input()` function, but add a little spice to it, by displaying a prompt for the user to understand they are inputting a value in feet.*"""


ft = float(input("Put in a value in feet: "))
inche = round(ft*12,2)
yard = round(ft/3,2)
mile = round(ft/5280,2)
# return inche, yard, mile
print(f"{ft} feet is {inche} inches, {yard} yards, and {mile} miles.")





"""5. Area of a regular polygon: A polygon is regular if its sides are all the same length and the angles between all of the adjacent sides are equal. The area of a regular polygon can be computed using the following formula, where ***s*** is the length of a side and ***n*** is the number of sides.
    
     $\boxed{area = \frac {n \times s^2} {4 \times \tan (\frac{\pi}{n})} }$
    
     Write a program that reads ***s*** and ***n*** from the user and then displays the area of a regular polygon constructed from these values."""

import math

n = int(input("number of sides: "))
s = int(input("length of the side: "))

area = n * (s ** 2) / (4 * math.tan(math.pi/n))

print(area)




"""6. Current Time: Python has a couple of modules that can be used when working with time. This includes a module called `time` and a function/method within the `time` module called `asctime`. It reads the current time from the computer’s internal clock and returns it in a human-readable format. Write a program that displays the current time and date. Your program will not require any input from the user.
    
     ************Hint:************ **import `time` to your working environment/kernel and explore all functions within the time module.*"""

import time
t = time.localtime()
print(time.asctime(t))




"""7. Wind Chill Index: When the wind blows in cold weather, the air feels even colder that it actually is because the movement of the air increases the rate of cooling for warm objects, like people. This effect is known as wind chill.
    
     The formula below is used to compute the wind chill index. 
    
     $WCI = 13.12 + 0.6215T_a - 11.37V^{0.16}+0.3965T_aV^{0.16}$
    
     Where: $T_a$ is the air temperature in degrees Celsius and $V$ is the wind speed in kilometers per hour. Write a program that begins by reading the air temperature and wind speed from the user. Once these values have been read, your program should display the wind chill index rounded to the closes integer.
    
     ************Hint:************ ********************************************************Use the `round()` python inbuilt function to round values to a determinate number of decimal places.*"""


import math

temp = float(input("Current temperature(degree): "))
wsped = float(input("Current wind speed(m/s): "))

wind_chill_index = round(13.12+ 0.6215 * temp - 1.37 * (wsped** 0.16) + 0.3965 * temp * (wsped ** 0.16))

print(f"At {temp} degree, {wsped} m/s wind speed, the wind chill index is {wind_chill_index}.")




"""8. **********************************************TEASER/BONUS QUESTION:********************************************** Sum of digits in an integer: Develop a program that reads a four digit integer from the user and displays the sum of the digits in the number. For example, if the user enters 3141 then your program should display the result of the sum $3+1+4+1=9$.
    
     ************Hint:************ ***************************Type conversion, string split operation, python sum operation.***************************"""


num = input("Write a 4 digits number: ")
num = list(num)

# for i in range(0,len(num)):
#     num[i] = int(num[i])

int_num= [eval(i) for i in num]

result_sum = num[0] + num[1] + num[2] + num[3]

print(result_sum)
