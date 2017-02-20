# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#Questions associated with the Easy Difficulty Quiz
easyQuiz = '''This is a quiz developed by ___1___ programming language. Python is a widely used ___2___ -level, general-purpose, interpreted, " \
    "dynamic programming language. Python was conceived in the late 1980s, and its implementation began in December ___3___. It was done by Guido ___4___ Rossum.'''

#Questions associated with the Medium Difficulty Quiz
mediumQuiz = '''The ___1___ manages the hardware of the computer system. It includes the CPU, memory,___2___ devices, and input/output " \
    "devices. The type of ___3___ system software you use depends on your computers platform. The ___4___ is the brains of every microcomputer.'''

#Questions associated with Hard Difficulty Quiz
hardQuiz = '''The ___1___ are the fastest and most expensive computers. Supercomputers were introduced in the ___2___s. Traditionally, supercomputers have been " \
    "used for ___3___ applications. They can also be used for ___4___ applications. Supercomputers must handle very large databases or do a great amount of computation (or both).'''

#List of the answers associated with each difficulty of the quiz
easyQuizAnswers = ['python', 'high', '1989', 'van']
mediumQuizAnswers = ['operating system', 'storage', 'operating', 'CPU']
hardQuizAnswers = ['supercomputer', '1960', 'scientific', 'engineering']

player_answers = ['___1___', '___2___', '___3___', '___4___']
                   
                   
# This function prompts the player to choose a difficulty for the game and returns their choice. If there selection is in valid it will provide error message and will let them try again.
def getDifficulty():
    print "Please choose your difficulty: EASY | MEDIUM | HARD"
    choice = raw_input("").lower()
    while choice not in ['easy', 'medium', 'hard', 'quit']:
        print "Choice {0} is not valid. Try again.".format(choice)
        print "Choose your difficulty: EASY | MEDIUM | HARD"
        choice = raw_input("").lower().strip()
    return choice

#This function prints the quiz, then prints each question one line at a time to for user to input, as well as checks the questions
def getAnswers(question, player_answers, answers):
    blanks = ['___1___', '___2___', '___3___', '___4___']
    index = 0
    print question, "\n"
    question = question.split(". ")
    for line in question:
        print line
        while player_answers[index].lower().strip() != answers[index]:
            player_answers[index] = raw_input("Fill In The Blank: ")
            if player_answers[index].lower().strip() != answers[index]:
                print "Incorrect! Try again"
        print "Correct!"
        print line.replace(blanks[index], answers[index]), "\n"
        index += 1
    print "Thank you for playing!"

#This function takes the difficulty selected and grabs the appropriate quiz, and answers for the game
def fillInTheBlanks(difficulty):
    if difficulty == "easy":
        getAnswers(easyQuiz, player_answers, easyQuizAnswers)
    elif difficulty == "medium":
        getAnswers(medium, player_answers, mediumQuizAnswers)
    elif difficulty == "hard":
        getAnswers(hardQuiz, player_answers, hardQuizAnswers)

#Starts the game
fillInTheBlanks(getDifficulty())
