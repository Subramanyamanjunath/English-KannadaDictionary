# this program is about converting an defined english word to kannada by iterating a dictionary logic

#if they give single word at at time

kannada_dictionary = {
    "there" : "alli",
    "here" : "elli",
    "one" : 1
}

user_entered_word = input("please enter the english word to find the kannada version : ")

print(kannada_dictionary.get(user_entered_word))


#if they give multiple word at at time

kannada_dictionary = {
    "there" : "alli",
    "here" : "elli",
    "one" : 1
}
user_entered_word = input("please enter the english word to find the kannada version : ")
words = user_entered_word.split()
print(words)

for every_word in words:
    print(kannada_dictionary.get(every_word))








