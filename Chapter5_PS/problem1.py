# Question 1 : Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
words = {
    "madad" : "help",
    "kursi" : "chair",
    "chai" : "tea",
    "bhookha" : "hungery",
    "kutta" : "dog",
    "billi" : "cat",
    "gaw" : "cow",
    "hathi" : "elephent",
    "bhaish" : "beffelow"
}

word = input("Enter the word you want meaning of : ")
print("English meaning of you want word in english : ",words[word])