import random

class MultipleChoice:
	def __init__(self, question, correctAnswer, allAnswers):
		self.question = question
		self.correctAnswer = correctAnswer
		self.answers = allAnswers

	def __str__(self):
		result = self.question + "\n"
		random.shuffle(self.answers)
		for i in range(len(self.answers)):
			choice = chr(ord('A') + i)
			result += choice + ". " + self.answers[i] + "\n"

		return result

class TrueFalse:
	def __init__(self, question, correctAnswer):
		self.question = question
		self.correctAnswer = correctAnswer
		self.answers = [True, False]

	def __str__(self):
		return self.question + ". (True/False)\n"

class FillInTheBlank:
	def __init__(self, question, correctAnswer):
		self.question = question
		self.correctAnswer = correctAnswer

	def __str__(self):
		return self.question + ". (Free Response)\n"


def main():
	# makes question bank
	list_of_questions = []
	infile = open("question_bank.txt", "r")
	for line in infile:
		line = eval(line)
		if line[0] == "MultipleChoice":
			# create MC question
			allAnswers = line[2:]
			question = MultipleChoice(line[1], line[2], allAnswers)
		elif line[0] == "FillInTheBlank":
			question = FillInTheBlank(line[1], line[2])
		else: # T/F
			question = TrueFalse(line[1], line[2])

		list_of_questions.append(question)

	infile.close()

	# trivia show
	user_score = 0

	for i in range(10):
		question = random.choice(list_of_questions)
		print(question)
		list_of_questions.remove(question)
		answer = input("What is your answer? ")
		if isinstance(question, MultipleChoice):
			if (answer == "A" and question.correctAnswer == question.answers[0]) or \
			   (answer == "B" and question.correctAnswer == question.answers[1]) or \
			   (answer == "C" and question.correctAnswer == question.answers[2]) or \
			   (answer == "D" and question.correctAnswer == question.answers[3]):
				# add score
				user_score += 100000
			else:
				print("You done. Game over. Who gonna be a millionaire? not you.")
				break
		else:
			if answer.upper() == str(question.correctAnswer).upper():
				user_score += 100000
			else:
				print("\nDishonor on you, yo family, dishonor on yo cow, get outta my face.")
				break

		print()
		print("\tCurrent score: $" + str(user_score))
		print()

	if user_score == 1000000:
		print("Congrats! You is kind, you is smart, you is a millionaire.")

		
main()




