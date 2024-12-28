# WAP to add 2 numbers

# A function to add 2 numbers
def addition(a,b):
    return int(a)+int(b)

if __name__=='__main__':
    a = input('Enter your 1st number: ')
    b = input('Enter your 2nd number: ')
    print(f'{a} + {b} is equal to {addition(a,b)}')