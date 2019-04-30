def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation += 'G'
            else:
                translation += 'g'
        else:
            translation += letter
    print(translation)
    decision(input('do you want to continue? y = yes and n = no:'))

def decision(i):
    if i == 'y' or i == 'Y':
        translate(input('enter phrase: '))
    elif i == 'n' or i == 'N':
        print('Done')
    else:
        print('Please, enter right option')
        decision(input('do you want to continue? y = yes and n = no:'))

def call():
    translate(input('enter phrase: '))

call()



