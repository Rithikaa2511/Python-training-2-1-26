from collections import Counter

a = Counter("encyclopediaa") #it checks each character and print the count by the number of priority and occurance.
print(a)
print(a.most_common(3)) # highest value containing pair will display .
print(a.clear()) # it clears all the values .
print(a.most_common(3)) # because of this clear function it displays empty square brackets.