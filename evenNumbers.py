setSet = set()
while True:
    number = input('Input a number or click "Enter" to stop adding numbers:  ')
    if number == '':
        break
    setSet.add(int(number))
evenNumbers = set(range(0, 101, 2))

print(f'You inputted {len(setSet & evenNumbers)} even numbers in the range 0 - 100')