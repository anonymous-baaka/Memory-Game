import tkinter
from tkinter import messagebox
import random

class window:
    wordList=[]#["hello","world","one","two","hey","apple"]
    occuredList=[]
    lives=3
    score=0
    def __init__(self):
        self.initWords()
        self.root=tkinter.Tk()
        self.addCanvas()
        self.populate()
        self.root.mainloop()

    def initWords(self):
        wordfile=open('wordlist.txt','r')
        wordlist=wordfile.read()
        wordlist=wordlist.replace('\n','\t').split('\t')
        print(wordlist)
        self.wordList=random.sample(wordlist,20)

    def addCanvas(self):
        self.canvas=tkinter.Canvas(self.root,height=480,width=800)
        self.canvas.pack()

    def populate(self):
        #textbox for word

        self.wordBox = tkinter.Text(self.canvas, height=1, width=25, font=("Helvetica", 40),fg='blue')
        self.setWord()
        self.wordBox.tag_configure("center", justify='center')
        self.wordBox.tag_add("center", 1.0, "end")
        #self.wordBox.config(state=tkinter.DISABLED)
        self.wordBox.pack()

        #textbox for message
        self.msgbox = tkinter.Text(self.canvas, height=1, width=25, font=("Helvetica", 12))
        self.msgbox.insert(tkinter.INSERT, "have you seen this word before?")
        self.msgbox.tag_configure("center", justify='center')
        self.msgbox.tag_add("center", 1.0, "end")
        self.msgbox.config(state=tkinter.DISABLED)
        self.msgbox.pack()

        #buttoncanvas
        self.buttoncanvas=tkinter.Canvas(self.canvas)
        self.buttoncanvas.pack()

        #buttons
        self.yesButton=tkinter.Button(self.buttoncanvas,width=40,height=3,text="YES",command=lambda:self.checkAns('yes'),bg='green',fg='white')
        self.yesButton.grid(row=3,column=3,padx=10,pady=30)
        self.noButton = tkinter.Button(self.buttoncanvas,width=40,height=3,text="NO",command=lambda:self.checkAns('no'),bg='red',fg='white')
        self.noButton.grid(row=3,column=1)

    def restart(self):
        self.occuredList=[]
        self.lives=3
        self.score=0

    def setWord(self):
        if self.lives>0:
            self.currentWord = self.generateWord()
            self.wordBox.config(state=tkinter.NORMAL)
            self.wordBox.delete(1.0,tkinter.END)
            self.wordBox.insert(1.0,self.currentWord)
            self.wordBox.tag_configure("center", justify='center')
            self.wordBox.tag_add("center", 1.0, "end")
            self.wordBox.config(state=tkinter.DISABLED)

        else:
            self.wordBox.config(state=tkinter.NORMAL,fg='red')
            self.wordBox.delete(1.0, tkinter.END)
            self.wordBox.insert(1.0, "Game over")
            self.wordBox.tag_configure("center", justify='center')
            self.wordBox.tag_add("center", 1.0, "end")
            self.wordBox.config(state=tkinter.DISABLED)
            answer = tkinter.messagebox.askyesno("Question", "Do you want to play again?")
            if answer:
                self.restart()
            else:
                self.root.destroy()


    def checkAns(self,ans):
        if ans=='yes' and self.currentWord in self.occuredList or ans=='no' and self.currentWord not in self.occuredList:
            self.score+=1
        else:
            self.lives-=1
        print("lives={} score={}".format(self.lives,self.score))
        self.occuredList.append(self.currentWord)
        self.setWord()

    def generateWord(self):
        word= self.wordList[random.randrange(len(self.wordList))]
        return word

root=window()
