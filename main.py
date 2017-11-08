import random
import unittest

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

def makeQuestionBank():
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
	return list_of_questions

def printLifelines(lifelines):
	print()
	print("Available lifelines:")
	for i in range(len(lifelines)):
		print("\t" + chr(ord('A') + i) + ". " + lifelines[i])
	print()

def main():
	# makes question bank
	list_of_questions = makeQuestionBank()

	# trivia show
	user_score = 0

	A = "Aa"
	B = "Bb"
	C = "Cc"
	D = "Dd"

	payout = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
	lifelines = ["50:50", "Double Dip", "Change Question"]
	for i in range(15):
		question = random.choice(list_of_questions)
		print(question)
		list_of_questions.remove(question)
		answer = input("If you would like to use a lifeline, enter \"lifeline\"\nIf you would like to answer, enter answer: ")

		# if the user wants to use a lifeine
		while answer == "lifeline":
			printLifelines(lifelines)
			lifeline_answer = input("Which lifeline would you like to use? 'q' to cancel: ")
			print()
			if lifeline_answer in A:
				# use 50:50 lifeline
				pass
			elif lifeline_answer in B:
				# use Double Dip lifeline
				pass
			elif lifeline_answer in C:
				# use Change Question lifeline
				pass
			else:
				# cancel
				answer = input("If you would like to use a lifeline, enter \"lifeline\"\nIf you would like to answer, enter answer: ")


		if isinstance(question, MultipleChoice):
			# booleans checking if answer is correct
			A_Correct = answer in A and question.correctAnswer == question.answers[0]
			B_Correct = answer in B and question.correctAnswer == question.answers[1]
			C_Correct = answer in C and question.correctAnswer == question.answers[2]
			D_Correct = answer in D and question.correctAnswer == question.answers[3]

			if A_Correct or B_Correct or C_Correct or D_Correct:
				# add score
				user_score = payout[i]
			else:
				print("You done. Game over. Who gonna be a millionaire? not you.")
				break
		else:
			if answer.upper() == str(question.correctAnswer).upper():
				user_score = payout[i]
			else:
				print("\nDishonor on you, yo family, dishonor on yo cow, get outta my face.")
				break

		print()
		print("\tCurrent score: $" + str(user_score))
		print()

	if user_score == 1000000:
		print("Congrats! You is kind, you is smart, you is a millionaire.")

		
main()


class TestSuite (unittest.TestCase):

	# create a test MC question for testing
	question = "What is 2 + 2?"
	correctAnswer = "4"
	allAnswers = ["2", '4', '0', '1']
	testMC = MultipleChoice(question, correctAnswer, allAnswers)

	# simply test the creation of a question object, we will be testing the MC type question
	def testQuestionCreation (self):
		self.assertEqual(self.testMC.question, self.question)
		self.assertEqual(self.testMC.correctAnswer, self.correctAnswer)
		self.assertEqual(self.testMC.answers, self.allAnswers)

	list_of_questions = []
	infile = open("question_bank.txt", "r")
	for line in infile:
		line = eval(line)
		if line[0] == "MultipleChoice":
			# create MC question
			tempAllAnswers = line[2:]
			tempQuestion = MultipleChoice(line[1], line[2], tempAllAnswers)
		elif line[0] == "FillInTheBlank":
			tempQuestion = FillInTheBlank(line[1], line[2])
		else: # T/F
			tempQuestion = TrueFalse(line[1], line[2])

		list_of_questions.append(tempQuestion)

	infile.close()
	# test if create questions are successful
	def testquestiongeneral1(self):
		assert self.list_of_questions is not None

	def testquestiongeneral2(self):
		for i in range(10):
			temp = random.choice(self.list_of_questions)
			assert temp is not None

	# test MC output
	def testMCQuestionStr (self):
		returnFlag = True
		MCStrOutput = str(self.testMC)
		for answer in self.allAnswers:
			if answer not in MCStrOutput:
				returnFlag = False
		self.assertTrue(returnFlag)

	# create a test fill in the blank question for testing
	testFillInTheBlank = FillInTheBlank("The Dog goes: ", "Woof")

	# test Fill in the blank output
	def testFillInTheBlankStr (self):
		expectedReturn = "The Dog goes: . (Free Response)\n"
		self.assertEqual(str(self.testFillInTheBlank), expectedReturn)

if __name__ == '__main__':
	unittest.main()