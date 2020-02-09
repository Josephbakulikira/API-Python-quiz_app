import requests
import random

quiz = 'Quiz_App'
URL = 'https://opentdb.com/api.php?amount=10&category=11&type=boolean'

PARAMS = {'results': quiz}
info = requests.get(url= URL, params = PARAMS)

data = info.json()
print(data['results'][0]["question"])

q_a = {}
questions = []
index = 0

for anything in data["results"]:
	questions.append(anything['question'])
	q_a.update({anything['question']: anything['correct_answer']})

run = True
while run:
	question = questions[random.randint(0, 9)]
	
	print(question)
	print('\n')
	answer = q_a[question]
	print(answer)
	player_answer = input('Answer with True or False: ')
	
	if answer == player_answer:
		print('\n')
		print('Correct')
		print('\n')
		run = False
	else:
		print('incorrect')
		player_answer = bool(input('Answer with True or False: '))

	