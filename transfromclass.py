def main():
	infile = open("question_bank.txt", "r")
	outfile = open('transformedBank.txt', 'w')
	for line in infile:
		line = eval(line)
		for i in range(len(line)):
			if i >= 2 and (type(line[i]) != type(True)):
				line[i] = str(line[i]).upper()
		outfile.write(str(line))
		outfile.write("\n")
	infile.close()
	outfile.close()
main()
