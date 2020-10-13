file = open("triviaRev.txt", "r")
fileData = file.readlines()
questions = []
for line in fileData: 
    splitData = line.split('|')
    questionData = {
        "category": splitData[0],
        "question": splitData[1],
        "answers": splitData[2].split(','),
        "explanation": splitData[3],
        "points":splitData[4]
    }
    questions.append(questionData)
    
def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Game! \n")
    print("\t\t", title, "\n")

for question in questions:
    print(question.get('category'))
    print(question.get("question"))
    