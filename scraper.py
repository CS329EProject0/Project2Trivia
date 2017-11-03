from urllib.request import urlopen
from bs4 import BeautifulSoup

class Question:
	def __init__(self, question):
		self.question = question
		self.correctAnswer = ""
		self.answers = []

	def addAnswer(self, answer):
		self.answers.append(answer)

	def __str__(self):
		result = self.question
		for answer in self.answers:
			result += "\n\t" + answer
		result += "\n"
		return result

def createQuestions():
	quote_page = "http://www.neoseeker.com/whowanttobemillionaire2/faqs/72192-who-wants-to-be-a-millionaire-gbc-questions.html"
	page = urlopen(quote_page)

	# parse the html using beautiful soup and store in variable 'soup'
	soup = BeautifulSoup(page, 'html.parser')

	questions_box = soup.find("div", attrs={'class':'text_only'})
	questions = list(questions_box.text)
	cleaned_up_questions = []
	line = ""
	for char in questions:
		if char != "\r" and char != "\n":
			line += char
		if char == "\n":
			if line != '':
				cleaned_up_questions.append(line)
			line = ""

	cleaned_up_questions = cleaned_up_questions[48:-48]
	list_of_questions = []
	for line in cleaned_up_questions:
		if line[-1] == "?":
			list_of_questions.append(Question(line))
		else:
			list_of_questions[-1].addAnswer(line)

	for question in list_of_questions:
		print(question)

createQuestions()





