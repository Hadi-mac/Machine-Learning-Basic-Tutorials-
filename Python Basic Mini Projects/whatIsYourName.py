name = input("What is your name?")

try:
    myName = name
except:
    print('wrong input,', name)
    quit()

def greet(x):
    print('hello', x)

greet(myName)
