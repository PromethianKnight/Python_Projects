# WAP to display what generation someone might belong to based on the year of their birth using basic IF-ELSE statements

# Function that takes an integer as an input
def age_based_gez_calc (age:int):

    how_old = 2025-age

    if how_old <= 0:
        print('You are not yet born!')
    elif how_old <= 12:
        print('You belong to Gen Alpha')
    elif how_old <= 28:
        print('You belong to Gen Z')
    elif how_old <= 44:
        print('You are a Millennial')
    elif how_old <= 60:
        print('You are Gen X')
    elif how_old <= 79:
        print('You are the Baby Boomers')
    else:
        print('How are you even alive ?')


if __name__ == '__main__':
    age_based_gez_calc(int(input('Enter the year you were born: ')))    # Accept user input and covert it into int