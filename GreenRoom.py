#-*-coding: utf-8 -*





import os
os.system("clear")
import amino
import time
client = amino.Client()



Yellow = '\033[1;33m'
green = '\033[0;32m'
red = '\033[0;31m'



print(''+green)
print(" _____   _____   _____   _   _   _____    _   _____  __    __ ")
print("/  ___/ | ____| /  ___| | | | | |  _  \  | | |_   _| \ \  / / ")
print("| |___  | |__   | |     | | | | | |_| |  | |   | |    \ \/ /  ")
print("\___  \ |  __|  | |     | | | | |  _  /  | |   | |     \  /   ")
print(" ___| | | |___  | |___  | |_| | | | \ \  | |   | |     / /    ")
print("/_____/ |_____| \_____| \_____/ |_|  \_\ |_|   |_|    /_/     ")

time.sleep(1)


os.system("clear")

print(" _____    _____   _____       ___  ___  ")
print("|  _  \  /  _  \ /  _  \     /   |/   | ")
print("| |_| |  | | | | | | | |    / /|   /| | ")
print("|  _  /  | | | | | | | |   / / |__/ | | ")
print("| | \ \  | |_| | | |_| |  / /       | | ")
print("|_|  \_\ \_____/ \_____/ /_/        |_| ")

time.sleep(1)

os.system("clear")








print("\n\n")




print(" _       _____   _____   _   __   _  ")
print("| |     /  _  \ /  ___| | | |  \ | | ")
print("| |     | | | | | |     | | |   \| | ")
print("| |     | | | | | |  _  | | | |\   | ")
print("| |___  | |_| | | |_| | | | | | \  | ")
print("|_____| \_____/ \_____/ |_| |_|  \_| ")

time.sleep(0.5)

print("\n\n")

print("" +red)


print ("Notice :  ")
print("\n\n")
time.sleep(0.3)
print ("We will never steal your account")
print ("If you are not sure, use a new account")

print("" +green)

print("\n\n")
time.sleep(0.5)
mail=input(" Type Your Email >> ")
print("\n\n")
   
p=input(" Type Your Password >> ")
         
client.login(email=mail,password=p)

os.system("clear")

infoos=input("community URL >> ")
infoo=client.get_from_code(infoos)
comId=infoo.path[1:infoo.path.index("/")]

subclient = amino.SubClient(comId=comId,profile=client.profile)



os.system("clear")


print (" insta : asta_199")
time.sleep(0.5)
print("\n")
print (" YouTube : 8R9 ")

print("\n\n\n\n\n")
time.sleep(1)

print(" _____             _____              _____  ")
print("/  _  \           |  _  \            /  _  \ ")
print("| |_| |           | |_| |            | |_| | ")
print("}  _  {           |  _  /            \___  | ")
print("| |_| |           | | \ \             ___| | ")
print("\_____/           |_|  \_\           |_____/ ")


time.sleep(0.7)

print("\n\n")

print ("[1] Chat Security")
time.sleep(0.5)
print("\n")
print ("[2] Profile Security")
time.sleep(1)



print("\n\n")

k=input(" Type Number >> ")

if k == '1' :
    os.system("clear")
    chat=input("Chat Url >> ")
    chatId = subclient.get_from_code(chat).objectId


    subclient.edit_chat(chatId=chatId,viewOnly='yes')
    con=("security 8R9")
    ti=("security 8R9")
    subclient.edit_chat(content=con, title=ti, chatId=chatId)
                                              




    message=(".......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية.......................حماية")
    try:
        subclient.send_message(message=message,messageType=110,chatId=chatId)

    except:
        pass


    try:
        subclient.send_message(message=message,messageType=110,chatId=chatId)

    except:
        pass


    try:
        subclient.send_message(message=message,messageType=110,chatId=chatId)

    except:
        pass

    try:
        subclient.send_message(message=message,messageType=110,chatId=chatId)

    except:
        pass

    try:
        subclient.send_message(message=message,messageType=110,chatId=chatId)

    except:
        pass

    try:
        subclient.send_message(message=message,messageType=110,chatId=chatId)

    except:
        pass

    try:
        subclient.send_message(message=message,messageType=110,chatId=chatId)

    except:
        pass

    try:
        subclient.send_message(message=message,messageType=110,chatId=chatId)

    except:
        pass

    try:
        subclient.send_message(message=message,messageType=110,chatId=chatId)

    except:
        pass

    try:
        subclient.send_message(message=message,messageType=110,chatId=chatId)

    except:
        pass



    os.system("clear")
    print (" Completed !!")

    print("\n\n")

    kl=input("Type [1] To Back >>  ")


    if kl == '1' :



        os.system("python GreenRoom.py")


if k == '2' :
    os.system("clear")
   
    tt=("Security 8R9")
    cc=("Security 8R9")
    subclient.edit_profile(content=cc, nickname=tt)
    print(" Completed !! ")

    print("\n\n")

    kl=input("Type [1] To Back >>  ")


    if kl == '1' :



        os.system("python GreenRoom.py")
