import random
import string
def passgen ():
    a = []
    pwlen = 16
    random.seed(random.randint(1,10000))
    while pwlen > 0:
        a.append(random.randint(1, 9))
        pwlen -=1
        a.append(random.choice(string.ascii_letters))
        pwlen -= 1
        a.append(random.choice(string.punctuation))
        pwlen -= 1
    #convert elements in the list to strings
    result = ''.join(str(e) for e in a)
    print(result)
    return
while True:
    userIn = input("Generate a random password? Y/N:  ")
    if userIn.lower() == "y":
        passgen()
    elif userIn.lower() != "n" and userIn.lower != "y":
        print("Please enter a valid response. \n")
    else:
        break
