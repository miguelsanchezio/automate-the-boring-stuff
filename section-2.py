name = input('What is your name? ')
age = int(input('...and, how old are you? '))

if name:
    print('Hello ' + name)
else:
    name = input('Enter a valid name: ')

if age > 1000:
    print('You must be immortal.')
elif age < 50:
    print('You are in your prime years.')
elif age < 21:
    print('You are still very young.')
elif age < 18:
    print('You have so much to learn.')
