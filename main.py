import random
import unittest
import tkinter
from tkinter import messagebox

class MultipleChoice:
	def __init__(self, questiontext, correctAnswer, allAnswers):
		self.questiontext = questiontext
		self.correctAnswer = correctAnswer
		self.answers = allAnswers
		self.qtype = "Multiple Choice"

	def __str__(self):
		result = self.questiontext + "\n"
		random.shuffle(self.answers)
		for i in range(len(self.answers)):
			choice = chr(ord('A') + i)
			result += choice + ". " + self.answers[i] + "\n"

		return result

class TrueFalse:
	def __init__(self, questiontext, correctAnswer):
		self.questiontext = questiontext
		self.correctAnswer = correctAnswer
		self.answers = [True, False]
		self.qtype = "True / False"

	def __str__(self):
		return self.questiontext + ". (True/False)\n"

class FillInTheBlank:
	def __init__(self, questiontext, correctAnswer):
		self.questiontext = questiontext
		self.correctAnswer = correctAnswer
		self.qtype = "Fill in the Blank"

	def __str__(self):
		return self.questiontext + ". (Free Response)\n"

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

	# import the GUI class
	from GUIreader import GUI

	# trivia show variables
	payout = ['100', '200', '300', '500', '1,000', '2,000', '4,000', '8,000', '16,000', '32,000', '64,000', '125,000', '250,000', '500,000', '1,000,000']
	lifelines = ["50:50", "Double Dip", "Change Question"]
	lifelinesRemaining = 3

	for i in range (15):
		question = random.choice(list_of_questions)
		master = tkinter.Tk()
		currentQuestion = GUI(master, question, payout[i], lifelinesRemaining)
		master.mainloop()

		list_of_questions.remove(question)

		'''
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
		'''

		# open the temporary Answer file to check if the answer is correct
		answerCheck = open("tempAnswer.txt","r")
		answer = answerCheck.readline().strip()
		answerCheck.close()

		if isinstance(question, MultipleChoice):
			if answer != 'A':
				break
		else:
			if answer.upper() != str(question.correctAnswer).upper():
				break

	# check to see if the player won or not
	print ()
	if i == 14:
		messageTitle = "Congratulations!"
		messageInfo = "You is kind, you is smart, you is a millionaire!"

	else:
		messageTitle = "Incorrect Answer"
		messageInfo = "You done. Game over. Who gonna be a millionaire? not you." + \
		"\n\nThe correct answer was: " + str(question.correctAnswer) + "\nFinal Score: $" + payout[i]

	master = tkinter.Tk()
	master.withdraw()
	messagebox.showinfo(messageTitle, messageInfo)
	master.destroy()

		
main()


class TestSuite (unittest.TestCase):

	# create a test MC question for testing
	question = "What is 2 + 2?"
	correctAnswer = "4"
	allAnswers = ["2", '4', '0', '1']
	testMC = MultipleChoice(question, correctAnswer, allAnswers)

	# simply test the creation of a question object, we will be testing the MC type question
	def testQuestionCreation (self):
		self.assertEqual(self.testMC.questiontext, self.question)
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