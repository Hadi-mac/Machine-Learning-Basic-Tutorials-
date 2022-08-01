print('start')
sum = 0
count = 0

while True:
    inp = input('Enter numbers or Write :done: if you want to finish')
    if inp == 'done': 
        break
    inp2 = (float(inp))
    count = count + 1
    sum = sum + inp2
average = sum / count
print('Average: ', average)


print('end')
input()