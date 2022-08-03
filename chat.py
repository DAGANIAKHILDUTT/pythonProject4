class chat:
    def chatbot(ques):
        if(ques=="hi|hello|hey"):
            print("hello")
        elif(ques=="no"):
            print("CEC: deals with cloud and edge computing")
            print("SM: deals with software modelling")
            print("GUX : deals with game design")
            print("AI: deals with Artificial Intelligence")
            print("DS : deals with data science")
            print("CYS : deals with Cyber security")
            print("IOT : deals with Internet of Things")
            print("These are the Specialiasatoin offered by KL University")
            print("Which specialisation you want to choose??")
        elif(ques=="yes"):
            print("oh good which specialization did you choose")
        if(ques=="CEC|SM|GUX|AI|DS|CYS|IOT"):
            print("you have made a great choice")
        else:
            print("Can't able to understand what you have entered")
print("Hello Monty!! \nI am bot created by LIKITH SAI to help you to choose specialization\n")
print("Do you know What are the specializations are offered in KL University")
q=input("Yes if you know (or) No if you don't know:\n")
chat.chatbot(q)
print()
q=input("Enter the Specialization\n CEC \n SM \n GUX \n AI \n DS \n CYS \n IOT\n")
chat.choosingspec(q)

