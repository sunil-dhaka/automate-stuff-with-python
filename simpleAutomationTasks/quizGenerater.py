import os
import random
# create 50 questions

## store quiz data into a dict
stateCapitalDict= {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

print('Working in ---- ',os.getcwd())
#os.makedirs('Quizzes') #<-- when running first time create this
# creates if dir does not exits
if not os.path.exists(os.getcwd()+'/Quizzes'):
    os.makedirs('Quizzes')
os.chdir('Quizzes')
print('Working in ---- ',os.getcwd())

stateNames=[state for state in stateCapitalDict]

totalStudents=35
totalQue=len(stateNames)

for k in range(totalStudents):
    with open('Quiz'+str(k+1)+'.txt','w') as quiz, open('Ans'+str(k+1)+'.txt','w') as ans:
        quiz.write('\t\t\t\t Question Paper - Geography \n')
        quiz.write('--------------------------------------------------------------------\n')
        quiz.write('Name: \n')
        quiz.write('Roll NO: \n')
        quiz.write('Class: \n')
        quiz.write('--------------------------------------------------------------------\n\n')
        # for answers
        ans.write('\t\t\t\t Answer Sheet - Geography \n')
        ans.write('--------------------------------------------------------------------\n\n')
        random.shuffle(stateNames)
        # this is the stuff that generates random quizzes
        for i in range(totalQue):
            rightOption=stateCapitalDict[stateNames[i]]
            wrongOptions=[]
            wrongOptions.append(rightOption)
            count=0
            while(count<3):
                choiceNo=random.randint(0,49)
                if choiceNo!=i:
                    count+=1
                    wrongOptions.append(stateCapitalDict[stateNames[choiceNo]])

            options=wrongOptions
            random.shuffle(options)
            optionsDict={options[0]:'A',options[1]:'B',options[2]:'C',options[3]:'D'}
            quiz.write(str(i+1)+'. What is the capital of state '+stateNames[i]+'?\n')
            for j in range(4):
                quiz.write('\t'+optionsDict[options[j]]+'. '+options[j]+'\n')
            quiz.write('\n')
            # for answers
            for j in range(4):
                if options[j]==rightOption:
                    ans.write(str(i+1)+'. '+optionsDict[rightOption]+'\n')
    quiz.close()
    ans.close()

# to dos=================
# can easily make it more interactive and even ask students to give exam on terminal(on PC) and show answers and marks right after submitting
# ask them their roll no and then give appropriate quiz to work with based on their roll no
# prompt can be used for option input and then store them into another text file
# compare lines and give score
#========================