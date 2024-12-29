description = 'This is a string, they can be big or small, filled with any range of characters and as long as they are between the single or double quotes, they can even include keywords'

# Different operations possible
print(description)  # Print the entire string
print(len(description)) # Print the length of the string
print(description.upper()) # Now you are shouting at someone
print(description.capitalize()) # 1st alphabet of every sentence is now caps
print(description.strip()) # Return a copy of the string with leading and trailing whitespace removed.
print(description.find('filled')) # Return the 1st index in a string where substring sub is found, can also be a single character
print(description.isdigit()) # Will return false bcz my string is not digits
print(description.isalpha()) # Will still return false bcz my string has special characters as well
print(description.count('t')) # This will return the count of the EXACT occurrence i.e. it is case-sensitive
print(description.replace('t','T')) # Replaces a character(s) with another without actually affecting the original string
print(description*3) # Silly thing, but Python lets you show your string multiple times with this