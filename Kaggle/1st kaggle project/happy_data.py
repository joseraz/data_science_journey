"""
Analytics in Business
Assignment 01
Employee Absentism
"""
import pandas as pd
import matplotlib.pyplot as plt

#Learning to read data
comp_dict = pd.read_csv(r'C:\Users\joera\OneDrive - Imperial College London\Term 3\Analytics in Business\Assignments 01\clean data\company_dictionary.csv')
votes = pd.read_csv(r'C:\Users\joera\OneDrive - Imperial College London\Term 3\Analytics in Business\Assignments 01\clean data\votes.csv')
last_par = pd.read_csv(r'C:\Users\joera\OneDrive - Imperial College London\Term 3\Analytics in Business\Assignments 01\clean data\lastParticipationExists.csv')
comments = pd.read_csv(r'C:\Users\joera\OneDrive - Imperial College London\Term 3\Analytics in Business\Assignments 01\clean data\comments_by_employees_in_anonymous_forum.csv')
interactions = pd.read_csv(r'C:\Users\joera\OneDrive - Imperial College London\Term 3\Analytics in Business\Assignments 01\clean data\commentInteractions.csv')

#'Grouping by' to get averages
data = pd.read_csv(r"C:\Users\joera\Downloads\CommentsAnalytics.csv")
avg_comments = data.groupby('employee')['commentLength'].mean()
avg_happy = data.groupby('employee')['Average Happy'].mean()
data_merge = pd.merge(avg_comments, avg_happy, on= 'employee')
data_merge.plot(x='Average Happy', y='commentLength', kind='scatter')

#Using the new data. Warning file was moved!
data = pd.read_csv(r"C:\Users\joera\Downloads\CommentsAnalytics.csv")
com_per_emp = data.groupby('employee')['commentId'].count()
com_per_emp.plot(kind='hist', bins=5)
vot_per_emp = data.groupby('employee')['commentId'].count()

#Simple histogram plot
last_par.plot(kind='hist')
last_par['numVotes'].describe()

#This is to get the happiest and unhappy employees, for unhappy change 'ascending to false'
happy = pd.DataFrame(avg_happy)
happy.sort_values(by='Average Happy', ascending=True).tail(10)

#Tracking the top four comments
com = pd.read_csv(r'C:\Users\joera\OneDrive - Imperial College London\Term 3\Analytics in Business\Assignments 01\clean data\comments_by_employees_in_anonymous_forum.csv', 
                  parse_dates=True, index_col='commentDateRevised')
com.loc['10-09-2018'].groupby('feedbackType').count()
	#Spikes in 2018 for Sep 10,  Oct 15, Nov 12, and Dic 10

#What are the longest comments about?
comments['commentLength'].describe()
comments[['commentLength','feedbackType']].sort_values(by='commentLength', ascending=False).head(10)
com2=comments[['commentLength','feedbackType']].sort_values(by='commentLength', ascending=False)
com2.plot(kind='hist', bins=20)

#Who comments the most?
emp_by_com = comments.groupby(by='employee')['employee'].count()
emp_by_com = pd.DataFrame(emp_by_com)
emp_by_com.rename(columns={"employee": "employee", "employee": "comment_count"})

#Finding correlation between happiness and comments by using a scatter plot
emp = last_par['employee']          #I used the file of last_participation, because it has the whole list of employees
emp = pd.merge(emp, avg_happy, how='left', on='employee') #Use left join to keep total of 480 employees and add the avg_happy
emp.set_index('employee')           #I not if this was necessary, it keeps the data a bit cleaner
emp = pd.merge(emp, emp_by_com, how='left', on='employee') #Second left join to add the comments
emp.info()          #I was expecting the number of comments to be less than the number of people that vote, im a bit skeptical if I did this correctly
emp.sort_values(by='Average Happy', ascending=True).head(10)
emp.plot(x='Average Happy', y='comment_count', kind='scatter')
