import tkinter
from tkinter import *
from tkinter import messagebox
from random import shuffle
# for some reason I have to explicitly import messagebox although "*" should import all

# scroll bar magic, don't touch
class GUI():
	def __init__(self, master, question, score, lifelinesRemaining):
		self.master = master
		self.question = question
		self.master.title('The Millionare')
		self.score = score
		self.lifelinesRemaining = lifelinesRemaining

		# a line parameter to locate the button
		self.linePos = 4

		# color design for GUI
		backgroundColor = "old lace"
		textColor = "#662E1C"
		buttonColor = "bisque"
		
		# Code to add widgets 
		# creating question label
		Label(master, fg = textColor, bg = backgroundColor, text=self.question.questiontext).grid(row=1,column = 1)

		# customize the GUI per question type
		if self.question.qtype == "Multiple Choice":
			# ensure button width fits size of answers
			maxQuestionLength = 0
			for answer in question.answers:
				if len(answer) > maxQuestionLength:
					maxQuestionLength = len(answer)
			maxQuestionLength += 4

			# randomize the questions
			ABCDIndex = [0, 1, 2, 3]
			shuffle(ABCDIndex)


			b1 = Button(master, bg = buttonColor,text=question.answers[ABCDIndex[0]], width=maxQuestionLength, command = lambda: self.callback(chr(ABCDIndex[0] + 65)))
			b1.grid(row=3,column = 1, pady = 15)
			b2 = Button(master, bg = buttonColor,text=question.answers[ABCDIndex[1]], width=maxQuestionLength, command = lambda: self.callback(chr(ABCDIndex[1] + 65)))
			b2.grid(row=4,column = 1, pady = 15)
			b3 = Button(master, bg = buttonColor,text=question.answers[ABCDIndex[2]], width=maxQuestionLength, command = lambda: self.callback(chr(ABCDIndex[2] + 65)))
			b3.grid(row=5,column = 1, pady = 15)
			b4 = Button(master, bg = buttonColor,text=question.answers[ABCDIndex[3]], width=maxQuestionLength, command = lambda: self.callback(chr(ABCDIndex[3] + 65)))
			b4.grid(row=6,column = 1, pady = 15)

			self.linePos += 4

		elif self.question.qtype == 'True / False':
			b1 = Button(master, bg = buttonColor,text="True", width=10, command = lambda: self.callback('True'))
			b1.grid(row=3,column = 1, pady = 15)
			b2 = Button(master, bg = buttonColor,text="False", width=10, command = lambda: self.callback('False'))
			b2.grid(row=4,column = 1, pady = 15)
			self.linePos += 2

		elif self.question.qtype == 'Fill in the Blank':
			self.resultBox = Entry(master)
			self.resultBox.grid(row=2,column = 1)
			self.linePos += 1
			b1 = Button(master, bg = buttonColor,text="Submit", width=10, command = lambda: self.callback(self.resultBox.get()))
			b1.grid(row=3,column = 1, pady = 15)
			

		else:
			print ('Something went wrong...')


		Label(master, fg = textColor, bg = backgroundColor, text = "You've won $" + self.score + ' so far.').grid (row = self.linePos, column = 1, pady = 5)
		Label(master, fg = textColor, bg = backgroundColor, text = "You have " + str(lifelinesRemaining) + " lifelines remaining.").grid (row = self.linePos + 1, column = 1, pady = 5)

		# create lifeline buttons
		button5050 = Button(master, bg = buttonColor, text = '50 / 50', width = 14, command = lambda: self.callback('50 / 50')).grid(row = self.linePos + 2, column = 0, padx = 20, pady = 15)
		buttonDoubleDip = Button(master, bg = buttonColor, text = 'Double Dip', width = 14, command = lambda: self.callback('Double Dip')).grid(row = self.linePos + 2, column = 1, padx = 20, pady = 15)
		buttonChangeQuestion = Button(master, bg = buttonColor, text = 'New Question', width = 14, command = lambda: self.callback('New Question')).grid(row = self.linePos + 2, column = 2, padx = 20, pady = 15)



	def callback(self, answer = ''):
		tempOutput = open('tempAnswer.txt','w')
		tempOutput.write(answer + '\n')
		tempOutput.close()

		self.master.destroy()

