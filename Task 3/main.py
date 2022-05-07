'''

Name: Raj Kansal
Email: rajkansal2001@gmail.com
Contact: 9309741329

'''


import json
import re #importing regex library from nltk
import random_responses

#loading json data

def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' sucessfully! ")
        return json.load(bot_responses)


#Storing json data in a variable
response_data = load_json("bot.json")

def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    #checking all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        #checking for any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1


        #amount of required words should match the required score
        if required_score == len(required_words):
           # print(required_score == len(required_words))

            for word in split_message:
                #if the word is in the repsonse, add to score
                if word in response["user_input"]:
                    response_score += 1


        #adding score to list
        score_list.append(response_score)

    #finding best response and returning
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    #checking if input is empty
    if input_string == "":
        return "Please type something so we can chat :D"

    #if there is no good response return random one

    if best_response !=0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()

while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))
