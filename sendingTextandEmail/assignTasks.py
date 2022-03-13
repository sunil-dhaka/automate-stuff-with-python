from random import random
import login, csv, random
from sendEamil import sendEmail
password=login.password_2t
sender_email=login.email_2t


with open('files/tasks.txt','r') as file:
    task_options=[task.strip() for task in file.readlines()]

# read from csv
with open('files/assignedTasks.csv','r') as file:
    task_data=list(csv.reader(file))

'''
people's information and subject line
'''
persons_=task_data[0][1:]
emails_=task_data[1][1:]
subject_='Alert! This week\'s task.'

# some info for indexing
week_no=len(task_data)-1
total_persons=len(persons_)


week_task=[f'week{week_no}']

'''
get week tasks
and
send assined task
'''
for i in range(total_persons): # see csv file to understand it
    '''
    control flow to ensure that nobody gets same task as they got in previous week
    unless there is only one task to do
    '''
    if week_no>1 and len(task_options)>1:
        previous_task=task_data[-1][i+1]
        while(True):
            task=random.choice(task_options)
            if previous_task!=task:
                break
        week_task.append(task)
        # remove this task to avoid same task being assinged to multiple people
        task_options.remove(task)
    else:
        task=random.choice(task_options)
        week_task.append(task)
        # remove this task to avoid same task being assinged to multiple people
        task_options.remove(task)

    sendEmail(sender_email,password,emails_[i],subject=subject_,body=f'Dear {persons_[i]},\n\nFor this week your task is to "{task}"\n\nThank You.')

# add this weeks tasks to the task-data
task_data.append(week_task)


# write in csv
with open('files/assignedTasks.csv','w') as file:
    csvWriter=csv.writer(file)
    csvWriter.writerows(task_data)