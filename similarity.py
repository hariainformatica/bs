# Import the difflib module for computing string similarity
import difflib

# Define a function to calculate the similarity ratio between two strings
def string_similarity(str1, str2):
    # Create a SequenceMatcher object with the lowercase versions of the input strings
    result = difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
    
    # Return the similarity ratio between the two strings
    return result.ratio()

# Initialize two strings for comparison
str1 = 'Python Exercises'
str2 = 'Python Exercises'

# Print the original strings
print("Original string:")
print(str1)
print(str2)

# Print a message indicating the similarity between the two strings
print("Similarity between two said strings:")
print(string_similarity(str1, str2))

# Repeat the process with different pairs of strings
str1 = 'Python Exercises'
str2 = 'Python Exercise'
print("\nOriginal string:")
print(str1)
print(str2)
print("Similarity between two said strings:")
print(string_similarity(str1, str2))

str1 = 'Python Exercises'
str2 = 'Python Ex.'
print("\nOriginal string:")
print(str1)
print(str2)
print("Similarity between two said strings:")
print(string_similarity(str1, str2))

str1 = 'Python Exercises'
str2 = 'Python'
print("\nOriginal string:")
print(str1)
print(str2)
print("Similarity between two said strings:")
print(string_similarity(str1, str2))

str1 = 'Python Exercises'
str2 = 'Java Exercises'
print("\nOriginal string:")
print(str1)
print(str2)
print("Similarity between two said strings:")
print(string_similarity(str1, str2)) 