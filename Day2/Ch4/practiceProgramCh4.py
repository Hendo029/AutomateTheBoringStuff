def collatz(number):
    if number % 2 == 0:
        temp2 = number // 2
        print(str(temp2), end = ' ')
        return temp2
    else:
        temp2 = 3 * number + 1
        print(str(temp2), end=' ')
        return temp2

print('Enter number:')

while True:
    try:
        numberInput = int(input())
        if numberInput <= 0:
            print('Give a value higher than 0')
            continue
        break
    except ValueError:
        print('You must enter an integer')
        continue

while True:
    numberInput = collatz(numberInput)
    if numberInput == 1:
        break

    