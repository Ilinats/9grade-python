import random

greetings = ["Hello!", "Hi!", "What's up?", "It’s great to see you!", "It's been a while!"]
goodbyes = ["See you soon!", "Bye!", "Goodbye!", "Hoping to hear from you!"]

keywords = ["book", "movie", "school", "pet", "weather"]
responses = ["My favourite book is Clockwork Princess.", "I haven't watched any movies in a while.", "School is for losers!", "My cat is better than YOURS!", "I like snow!"]

print(random.choice(greetings))

user = input("Say something (bye to quit): ")
user = user.lower()

while user != "bye":
    keyword_found = 0
    
    for index in range(len(keywords)):
        if keywords[index] in user:
            print("Bot: " + responses[index])
            keyword_found = 1
     
    if keyword_found == 0:
        print("Bot: I'm not sure how to respond. To what keyword should I respond?")
        new_keyword = input()
        new_keyword = new_keyword.lower()
        keywords.append(new_keyword)
        print("Bot: How should I respond to " + new_keyword + "?")
        new_response = input()
        responses.append(new_response)
        
    user = input("Say something (bye to quit): ")
    user = user.lower()
    
print(random.choice(goodbyes))