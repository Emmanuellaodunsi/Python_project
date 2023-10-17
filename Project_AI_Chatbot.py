#Importing the OpenAI module to access the chatgpt-3.5 model
import openai
#Importing datetime module to access the current time and date
import datetime
"""Since we are using openai api key...to get response from chatgpt-3.5 model,
this code can only run with the use of internet connection"""

#Storing my OpenAI API key in a variable
openai.api_key = "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"
#Printing out the current time and date
current_date=datetime.datetime.now()
print("Date: ",current_date.strftime("%Y-%m-%d"))
print("Time: ",datetime.datetime.now().strftime("%H:%M %p\n"))
#Asking the user for input and providing instructions for exiting
name= input("Chatbot: Hello welcome :)....Enter your name?\nYou: ")
print("Chatbot: Nice to meet you",name,"!\n")
print("Chatbot: I'm a chatbot,I'm here to help with any questions....just ask ;)...\n")
print("What would you like to know",name,"?""....Enter 'exit' to end the conversation..\n")
#Using a boolean variable to control the conversation loop
conversation = True
#Starting a conversation loop that continues until the user enter 'exit' to end the conversation
while conversation:
    #Asking the user for input
    User_input=input("You: ")
    #Checking if the user wants to exit the conversation
    if User_input == 'exit':
        print("Alright...Goodbye",name,"feel free to come back anytime..I'm here to assist you.")
        conversation = False
    else:
        #Calling the API for chatgpt-3.5 model to return a response
        response = openai.Completion.create(
            model='text-davinci-003',  #The selected model from chatgpt
            prompt=User_input,  #The user's input
            temperature=0.9,  #The temperature parameter controls the randomness of the response
            max_tokens=300,  #The maximum length of the generated response
        )
        #Printing the chatbot response"
        print("Chatbot:Sure",name,"I have an answer to that:",response['choices'][0]['text'])