color = input('Enter name of favourite color: ')
Number = input('Enter your favourite number: ')

n = int(Number)     #length of list of friends
friends = []

print(f'Enter names of {Number} friends: ')

for x in range(n):        #take input from user and store in list
    person = input(f'Enter name of friend {x+1}: ')
    friends.append(person)

# Print the poem w.r.t. user's input
print(f'''Baa, Baa, {color} sheep,
have you any wool?
Yes sir, yes sir -
{Number} bags full:''')

for i in range(n):      #print names of friends in poem
    if i == n-1:
        print(f'''And one for the {friends[i]}''')  #prints last friend's name
        break
    print(f'''One for the {friends[i]}''')

print(f'''that lives down the lane.
Baa, Baa, {color} sheep,
have you any wool?
Yes sir, yes sir
{Number} bags full.''')

