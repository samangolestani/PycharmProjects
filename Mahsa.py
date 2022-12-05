import datetime
a = True
while a :
    str = input("Enter a sentence:")
    pl = str.lower()
    if pl == "how are you" :
        print("I'm fine")
    elif pl == "what is your name?" :
        print("My name is DENNIS!")
    elif pl == "when is the time?" :
        print(datetime.datetime.now())
    elif pl == "are you alright?":
        print("Yes I am!")
    elif pl =="bye" :
        a=False
    else : print("THAT DOESN'T MAKE ANY SENSE TO ME")
