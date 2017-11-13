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

def getAnswer():
	tempAnswer = open("tempAnswer.txt","r")
	answer = tempAnswer.readline().strip()
	tempAnswer.close()
	return answer

def main():
	# makes question bank
	list_of_questions = makeQuestionBank()

	# import the GUI class
	from GUIreader import GUI

	# trivia show variables
	payout = ['100', '200', '300', '500', '1,000', '2,000', '4,000', '8,000', '16,000', '32,000', '64,000', '125,000', '250,000', '500,000', '1,000,000']
	lifelinesRemaining = 3
	correctAnswers = 0

	while correctAnswers < 15:
		question = random.choice(list_of_questions)
		master = tkinter.Tk()
		currentGUI = GUI(master, question, payout[correctAnswers], lifelinesRemaining)
		master.mainloop()

		list_of_questions.remove(question)

		# open the temporary Answer file to check if the answer is correct
		answer = getAnswer()

		# check if the player used a lifeline
		if answer[:8] == 'Lifeline':
			lifelinesRemaining -= 4
			if answer[9:] == "50 / 50":
				master = tkinter.Tk()
				master.withdraw()
				messagebox.showinfo("50 / 50", "Two answer choices will be eliminated.")
				question = MultipleChoice(question.questiontext, question.correctAnswer, question.answers[:2])

			elif answer[9:] == "New Question":
				master = tkinter.Tk()
				master.withdraw()
				messagebox.showinfo("New Question", "You will be given a new question at no penalty.")
				question = random.choice(list_of_questions)

			else:
				master = tkinter.Tk()
				master.withdraw()
				messagebox.showinfo("Double Dip!", "You have two chances to select the correct answer.")
				master.deiconify()
				currentGUI = GUI(master, question, payout[correctAnswers], lifelinesRemaining)
				master.mainloop()
				answer = getAnswer()
				if answer != 'A':
						master = tkinter.Tk()
						master.withdraw()
						messagebox.showinfo('Double Dip!', 'One more chance remaining!')
				else:
					correctAnswers += 1
					continue
		
			master.deiconify()
			currentGUI = GUI(master, question, payout[correctAnswers], lifelinesRemaining)
			master.mainloop()
			lifelinesRemaining += 3

		# check if the answer is correct
		answer = getAnswer()
		if isinstance(question, MultipleChoice):
			if answer != 'A':
				break
		else:
			if answer.upper() != str(question.correctAnswer).upper():
				break

		correctAnswers += 1

	# check to see if the player won or not and customize popup message
	print ()
	if correctAnswers == 14:
		messageTitle = "Congratulations!"
		messageInfo = "You is kind, you is smart, you is a millionaire!"

	else:
		messageTitle = "Incorrect Answer"
		messageInfo = "You done. Game over. Who gonna be a millionaire? not you." + \
		"\n\nThe correct answer was: " + str(question.correctAnswer) + "\nFinal Score: $" + payout[correctAnswers]

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