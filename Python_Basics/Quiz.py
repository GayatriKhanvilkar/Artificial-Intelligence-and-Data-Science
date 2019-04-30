from answer import Answer

q_prompt = ['What is the color of apple?\n (a)red/green\t (b)white\t (c)blue\n',
            'What is the color of sky?\n (a)yellow\t (b)blue\t (c)pink\n',
            'What is the color of mango?\n (a)blue\t (b)black\t (c)yellow\n']

question = [Answer(q_prompt[0], 'a'),
            Answer(q_prompt[1], 'b'),
            Answer(q_prompt[2], 'c')]


def test(question):
    score = 0
    for q in question:
        ans = input(q.prompt)
        if ans == q.ans:
            score +=1
    print(f'Your score is {str(score)}')

test(question)








