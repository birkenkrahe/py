import random

wins = 0
loss = 0
ties = 0

print('ROCK, PAPER, SCISSORS')

while True:

    print(f'{wins} wins, {loss} losses, {ties} ties',end='\n\n')

    user = input('Enter your move: r(ock), (p)aper, (s)cissors or (q)uit: ')

    if user == 'q':
	break

    comp = random.choice(['r','p','s'])

    print(f'{user.upper()} versus...\n\n {comp.upper()}:')

    if comp == user:
	tie += 1
	print("It's a tie!")
    elif (user == 'r' and comp == 's') or\
	 (user == 'p' and comp == 'p') or\
	 (user == 's' and comp == 'r'):
	win += 1
	print('You win!')
    else:
	loss += 1
	print("You loose!")
