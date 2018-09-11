#FizzBuzz finder that asks for a starting and ending number. Prints out results.

start = int(input('Say what number to start with: '))
ending = int(input('Say what number to end with: '))

numbers = range(start, (ending + 1))

for number in numbers:
    if number %3 == 0 and number %5 == 0:
        print('FizzBuzz')
    elif number %3 == 0:
        print('Fizz')
    elif number %5 == 0:
        print('Buzz')
    else:
        print(number)
