from urllib.request import urlopen
from bs4 import BeautifulSoup

class Question:
	def __init__(self, question):
		self.question = question
		self.correctAnswer = ""
		self.answers = []

	def addAnswer(self, answer):
		self.answers.append(answer)

	def correctQuestion(self, next):
		addOn = self.answers.pop()
		next.question = addOn + next.question

	def __str__(self):
		result = self.question
		answerChoice = 0
		for answer in self.answers:
			result += "\n\t" + str(answerChoice) + ": " + answer
			answerChoice += 1
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

	cleaned_up_questions = cleaned_up_questions[48:-298]
	list_of_questions = []
	for line in cleaned_up_questions:
		if line[-1] == "?":
			list_of_questions.append(Question(line))
		else:
			list_of_questions[-1].addAnswer(line)

	list_of_questions = list_of_questions[:301]

	list_of_questions[0].correctQuestion(list_of_questions[1])
	list_of_questions[8].correctQuestion(list_of_questions[9])
	list_of_questions[9].correctQuestion(list_of_questions[10])
	list_of_questions[10].correctQuestion(list_of_questions[11])
	list_of_questions[19].correctQuestion(list_of_questions[20])
	list_of_questions[20].correctQuestion(list_of_questions[21])
	list_of_questions[23].correctQuestion(list_of_questions[24])
	list_of_questions[28].correctQuestion(list_of_questions[29])
	list_of_questions[31].correctQuestion(list_of_questions[32])
	list_of_questions[56].correctQuestion(list_of_questions[57])
	list_of_questions[75].correctQuestion(list_of_questions[76])
	list_of_questions[84].correctQuestion(list_of_questions[85])
	list_of_questions[85].correctQuestion(list_of_questions[86])
	list_of_questions[91].correctQuestion(list_of_questions[92])
	list_of_questions[94].correctQuestion(list_of_questions[95])
	list_of_questions[95].correctQuestion(list_of_questions[96])
	list_of_questions[104].correctQuestion(list_of_questions[105])
	list_of_questions[105].correctQuestion(list_of_questions[106])
	list_of_questions[106].correctQuestion(list_of_questions[107])
	list_of_questions[110].correctQuestion(list_of_questions[111])
	list_of_questions[114].correctQuestion(list_of_questions[115])
	list_of_questions[117].correctQuestion(list_of_questions[118])
	list_of_questions[119].correctQuestion(list_of_questions[120])
	list_of_questions[124].correctQuestion(list_of_questions[125])
	list_of_questions[140].correctQuestion(list_of_questions[141])
	list_of_questions[142].correctQuestion(list_of_questions[143])
	list_of_questions[145].correctQuestion(list_of_questions[146])
	list_of_questions[146].correctQuestion(list_of_questions[147])
	list_of_questions[149].correctQuestion(list_of_questions[150])
	list_of_questions[155].correctQuestion(list_of_questions[156])
	list_of_questions[164].correctQuestion(list_of_questions[165])
	list_of_questions[180].correctQuestion(list_of_questions[181])
	list_of_questions[190].correctQuestion(list_of_questions[191])
	list_of_questions[203].correctQuestion(list_of_questions[204])
	list_of_questions[204].correctQuestion(list_of_questions[205])
	list_of_questions[210].correctQuestion(list_of_questions[211])
	list_of_questions[220].correctQuestion(list_of_questions[221])
	list_of_questions[225].correctQuestion(list_of_questions[226])
	list_of_questions[231].correctQuestion(list_of_questions[232])
	list_of_questions[233].correctQuestion(list_of_questions[234])
	list_of_questions[242].correctQuestion(list_of_questions[243])
	list_of_questions[250].correctQuestion(list_of_questions[251])
	list_of_questions[253].correctQuestion(list_of_questions[254])
	list_of_questions[258].correctQuestion(list_of_questions[259])
	list_of_questions[295].correctQuestion(list_of_questions[296])
	list_of_questions[30].correctQuestion(list_of_questions[31])
	list_of_questions[141].answers = ["George Washington", "Thomas Jefferson", "Benjamin Franklin", "Franklin Roosevelt"]
	list_of_questions[142].answers = ["Errol Flynn", "Clark Gable", "Cary Grant", "Humphrey Bogart"]
	list_of_questions[156].answers = ["ducks in a pond", "pigs in a blanket", "cows in a pasture", "dogs in the oven"]
	list_of_questions[182].answers = list_of_questions[182].answers[:-1]
	list_of_questions[183].answers = list_of_questions[183].answers[:-1]

	
	#53, 74, 86, 99, 120, 142, 162
	
	list_of_questions[8].answers = ["Denny's", "McDonald's", "Burger King", "Hardee's"]
	list_of_questions[1].answers[1] = "bill of landing"
	list_of_questions[1].answers.append("driver's license")
	
	file = open("questions.txt", "w")
	file.close()
	
	location = 0
	for i in range(142, len(list_of_questions)):
		file = open("questions.txt", "a")
		question = list_of_questions[i]
		print(str(i+1) + ": " + str(question))
		answer = int(input("What is the correct answer? "))
		question.correctAnswer = question.answers[answer]
		question.answers.remove(question.correctAnswer)
		print()
		result = "MultipleChoice " + question.question + " " + question.correctAnswer + " " + question.answers[0] + " " + question.answers[1]+ " " + question.answers[2] + "\n"
		file.write(result)
		file.close()

	print("Done")

createQuestions()





