from chatterbot.trainers import  ListTrainer # this is  our method to train our chatter bot
from chatterbot import  ChatBot

bot=ChatBot("test") # creare a chat object
conv=open("venkat.txt","r").readlines()
bot.set_trainer(ListTrainer)# set the trainer
bot.train(conv) # train

while True:

    request=input("you:")
    if request.strip()=="Byee":
        break

    response=bot.get_response(request)
    print("bot:",response)

