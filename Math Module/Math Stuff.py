# WAP to print the area of a circle and its circumference

import math

# Function to calculate the area of a circle
def area_of_circle(r:float):
    return math.pi*math.pow(r,2)    # returns pi * r * r

# Function to calculate the circumference of the circle
def circ_of_circle(r:float):
    return 2*math.pi*r  # returns 2 * pi * r

if __name__=='__main__':
    # Ask the user for a numeric input
    radius = float(input('Enter the radius of a circle: ')) # For some reason type casting before input still resulted
                                                            # in the input getting converted into string
                                                            # is the default data type for input function 'String' ?

    print(f'The area of the the circle with radius {radius} is: {area_of_circle(radius)}')

    print(f'The circumference of the circle with radius {radius} is: {circ_of_circle(radius)}')

    print(type(area_of_circle(radius))) # The function returns float