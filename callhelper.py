# an auxiliary method to test the right code to readin
import tkinter
from tkinter import *
import GUIreader
from GUIreader import GUI
# scroll bar magic, don't touch
def main():
	for i in range(3):
		questiontext = ["MultipleChoice", "Who is the star of the movie 'Casablanca'?", "Humphrey Bogart", "Errol Flynn", "Clark Gable", "Cary Grant"]
		root = tkinter.Tk()
		textEntry = ""
		displayGUI = GUI(root, questiontext)
		root.mainloop()

main()
