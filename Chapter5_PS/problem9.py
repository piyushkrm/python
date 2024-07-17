'''Question 9 : Can you change the values inside a list which is contained in set S? S = {8, 7, 12, "Harry", [1,2]}'''
S = {8, 7, 12, "Pihu", [1,2]}


''''

No, you cannot change the values inside a list contained in a set in Python. This is because sets in Python require their elements to be immutable (i.e., their values cannot be changed). Lists, on the other hand, are mutable (i.e., their values can be changed). Therefore, including a list within a set would violate this immutability requirement, leading to an error.

If you try to include a list in a set, you will encounter a TypeError. Here's an example demonstrating this:

python
Copy code
S = {8, 7, 12, "Pihu", [1, 2]}
'''