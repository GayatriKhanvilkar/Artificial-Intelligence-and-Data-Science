Secret_Word = 'Python'
score = 50
guess_count = 1
trail = 3
while guess_count <= trail:
    Guesses = input(f'Guess word. Trial number {guess_count}')
    if Guesses == Secret_Word.lower():
        print('You won!!!')
        score -= (guess_count -1)*10
        print(f"your score {score}")
        break
    if guess_count == trail:
        print('Sorry!!! Out of guess trails, lost the game')
    guess_count += 1