'''Question 7 : Write a program to find out whether a given post is talking about "Piyush" or not.'''
post = "This is not talk about any person. Today we are solved most of the question with self and unless i will do the practice. This is Piyush mishra"
name = "Piyush"
if name.lower().strip() in post.lower().strip():
    print("Yes, the post is talking about Piyush.")
else:
    print("No, the post is not talking about Piyush.")