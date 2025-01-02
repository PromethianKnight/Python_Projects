# WAP to demonstrate various string slicing use cases

# Slicing: creates a substring by extracting elements from another string [start:stop:step]

sentence = 'This is a sentence with words 1234567890 !@#$%^&*()_+'

print(sentence[0:21])   # Print the substring from index 0 till 21 but not including the 21's index

print(sentence[:21])   # Another way of writing it

print(sentence[40:])   # Similarly

print(sentence[::2])    # Step of 2 a.k.a. every other alphabet

print(sentence[::-1])   # Everything is backwards

# Time for some slice function

# WAP to pull only the website name from their respective URLs

website1 = 'https://google.com' # Sample data 1
website2 = 'https://wikipedia.com'  # Sample data 2
website3 = 'https://spotify.com'    # Sample data 3
website4 =

slicer = slice(8,-4)    # slice function --> creates a slice object that can be re-used.
                        # syntax slice(start index,end index)

print(website1[slicer])

print(website2[slicer])

print(website3[slicer])