import tkinter
from tkinter import *
from tkinter import messagebox
# for some reason I have to explicitly import messagebox although "*" should import all

# scroll bar magic, don't touch
class GUI():
	def __init__(self, master, question):
		self.master = master
		self.questiontext = question[1]
		self.master.title('The Millionare')
		self.qType = question[0]
		# a line parameter to locate the button
		self.linePos = 3

		# color design for GUI
		backgroundColor = "old lace"
		textColor = "#662E1C"
		buttonColor = "bisque"
		
		# Code to add widgets 
		# creating question label
		Label(master,fg = textColor,bg = backgroundColor,text=self.questiontext).grid(row=1,column=0)

		self.master.deiconify()
		if self.qType == "MultipleChoice":
			b1 = Button(master, bg = buttonColor,text=question[2], width=10, command = lambda: self.callback('A'))
			b1.grid(row=3,column=0, pady = 20)
			b2 = Button(master, bg = buttonColor,text=question[3], width=10, command = lambda: self.callback('B'))
			b2.grid(row=4,column=0, pady = 20)
			b3 = Button(master, bg = buttonColor,text=question[4], width=10, command = lambda: self.callback('C'))
			b3.grid(row=5,column=0, pady = 20)
			b4 = Button(master, bg = buttonColor,text=question[5], width=10, command = lambda: self.callback('D'))
			b4.grid(row=6,column=0, pady = 20)

			self.linePos += 4

		elif self.qType == 'TRUE/False':
			b1 = Button(master, bg = buttonColor,text="True", width=10, command = lambda: self.callback('True'))
			b1.grid(row=3,column=0, pady = 20)
			b2 = Button(master, bg = buttonColor,text="False", width=10, command = lambda: self.callback('False'))
			b2.grid(row=4,column=0, pady = 20)
			self.linePos += 2

		elif self.qType == 'FillInTheBlank':
			self.resultBox = Entry(master)
			self.resultBox.grid(row=2,column=0)
			self.linePos += 1
			b1 = Button(master, bg = buttonColor,text="Submit", width=10, command = lambda: self.callback(self.resultBox.get()))
			b1.grid(row=3,column=0, pady = 20)
			

		else:
			print ('Something went wrong...')



	def callback(self, answer = ''):
			tempOutput = open('tempAnswer.txt','a')
			tempOutput.write(answer + '\n')
			tempOutput.close()

			self.master.destroy()

