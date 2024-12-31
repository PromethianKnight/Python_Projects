# WAP to demonstrate various string slicing use cases

# Slicing: creates a substring by extracting elements from another string [start:stop:step]

sentence = 'This is a sentence with words 1234567890 !@#$%^&*()_+'

print(sentence[0:21])   # Print the substring from index 0 till 21 but not including the 21's index

print(sentence[:21])   # Another way of writing it

print(sentence[40:])   # Similarly

print(sentence[::2])    # Step of 2 a.k.a. every other alphabet

print(sentence[::-1])   # Everything is backwards