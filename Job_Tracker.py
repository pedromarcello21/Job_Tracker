#Pedro Vincenty HW 9

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from datetime import date
from datetime import timedelta
import warnings
warnings.filterwarnings("ignore")
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pyg
pyg.init()
path = '/Users/Pedro/Desktop/Fordham/Python/HW/'
errorSound = pyg.mixer.Sound(path+"errorBuzz.wav")
alertSound = pyg.mixer.Sound(path+"IM.wav")
masterJobTracker = path+'Master_Job_Tracker.xlsx'

df = pd.read_excel(masterJobTracker)

################### wrangling notes ######################
#df = df.fillna('')
# print(df.fillna('').to_string(index = False))#(index = 'Company'))
# print('\n')
#df = df.set_index(['Company']).to_string()
#set_index(['Date'])
# #Creates a named, empty column
# #df = df.assign(Reminders = '')
#Renames column, first value is existing column name
#df = df.rename(columns={"notes": "Notes"})
################### end of wrangling notes ######################

#The following link was used to help understand how to row bind dataframes together https://www.geeksforgeeks.org/how-to-concatenate-two-or-more-pandas-dataframes/
def dfAdd(c,a,m,p,n,df):
    df2 = pd.DataFrame({'Company': c, 'Alumni': a, 'Motivation': m, 'Postings': p, 'Notes': n}, index = [0])
    dfAddTest = pd.concat([df,df2], ignore_index = True)
    dfAddTest.to_excel(masterJobTracker, index = False)
    dfUpdate = dfAddTest
    return dfUpdate
#End of code from https://www.geeksforgeeks.org/how-to-concatenate-two-or-more-pandas-dataframes/
 
def dfDel(c,df):
    dfDelTest = df[df['Company'] != c]
    dfDelTest.to_excel(masterJobTracker, index = False)
    dfUpdate = dfDelTest
    return dfUpdate
     
def dfAmmend(c,a,m,p,n,df):
    dfAmmendCompany = df[df['Company'] == c]
    dfAmmendCompany[['Alumni','Motivation','Postings','Notes']] = [a,m,p,n]
    df[df['Company'] == c] = dfAmmendCompany
    df.to_excel(masterJobTracker, index = False)
    dfUpdate = df
    return dfUpdate

def dfError(dfPrompt,prompt):
    sentiment = SIA().polarity_scores(dfPrompt)
    while sentiment['neu'] == float(1) or dfPrompt =='':
        errorSound.play()
        print("This program didn\'t register your answer.")
        dfPrompt = input(prompt)
        sentiment = SIA().polarity_scores(dfPrompt)
    return sentiment

###########################Reminders implementation################
today = date.today()
print("Today\'s date is:", today)
print("\n")

#Deletes Reminders from the past 
df['Reminders'] = df['Reminders'].fillna(today - pd.DateOffset(years= 100))
for i in df['Reminders']:
    if i < today:
        df['Reminders'] = df['Reminders'].replace(i,'')
    else:
        pass

alerts = df[df['Reminders'].notna()]
alertsDict = alerts.set_index('Company').to_dict()['Reminders']
if len(alertsDict) > 0:
    alertSound.play()
class Format:
    end = '\033[0m'
    underline = '\033[4m'
for i in alertsDict:
    if alertsDict[i] == today:
        print(Format.underline+"Follow up with "+i+" today"+ Format.end)
    elif alertsDict[i] == today + timedelta(days=1):
        print(Format.underline+"Follow up with "+i+" tomorrow"+ Format.end)
    elif alertsDict[i] == today + timedelta(days=2):
        print(Format.underline+"Follow up with "+i+" in a couple days"+ Format.end)
    else:
        pass

#################################################################################
#Prompt the user if s/he would like to make any changes to their master job tracker
prompt = "\nWould you like to make changes to your master job tracker?\n>>>"
dfPrompt = input(prompt)
sentiment = dfError(dfPrompt,prompt)
#############################################

while sentiment['pos'] > sentiment['neg']:
    
    #prompt the user if s/he would like to add, delete, or ammend to their master tracker        
    dfPrompt = input("Would you like to add, delete, or ammend to your master job tracker?\n>>>")
    dfPrompt = dfPrompt.lower()
    while dfPrompt not in ('add', 'delete','ammend'):
        errorSound.play()
        dfPrompt = input("Please indicate if you\'d like to add, delete, or ammend to your master job tracker?\n>>>")
        dfPrompt = dfPrompt.lower()
        
    if dfPrompt == 'add':
        c = input("What company would you like to include\n>>>")
        if c not in df['Company'].to_list():
            a = input("Are there alumni from you school at the company or do you know anyone who works there? (Y/N)\n>>>").upper()
            m = input("How would you rate your interest in the role? High (H), Medium (M), Low(L). \n>>>").upper()
            p = input("Does this company have job postings currently available? (Y/N)\n>>>").upper()
            n = input("Are there any miscellanous notes you'd like to include for this entry? Press enter if none.\n>>>")
            dfUpdate = dfAdd(c,a,m,p,n,df)
        else:
            errorSound.play()
            print("This company is already listed in your tracker.\n")
            dfUpdate = df


    elif dfPrompt == 'delete':
        c = input("What company do you want to delete?\n>>>")
        if c not in df['Company'].to_list():
            errorSound.play()
            print("This company not listed in your tracker.\n")
            dfUpdate = df
        else:
            dfUpdate = dfDel(c,df)
        
        
    elif dfPrompt == 'ammend':
        c = input("What company do you want to ammend?\n>>>")
        if c in df['Company'].to_list():
            a = input("Are there alumni from you school at the company or do you know anyone who works there? (Y/N)\n>>>").upper()
            m = input("How would you rate your interest in the role? High (H), Medium (M), Low(L). \n>>>").upper()
            p = input("Does this company have job postings currently available? (Y/N)\n>>>").upper()
            n = input("Are there any miscellanous notes you'd like to include for this entry? Press enter if none.\n>>>")
            dfUpdate = dfAmmend(c,a,m,p,n,df)
        else:
            errorSound.play()
            print("Company not found in tracker :/\n")
            dfUpdate = df
  
    df = dfUpdate
    dfPrompt = input("Would you like to make any more changes to your master job tracker?\n>>>")
    sentiment = SIA().polarity_scores(dfPrompt)

##################### Reminders implementation #######################
prompt = "Would you like to set a reminder for any job prospects\n>>>"
reminder = input(prompt)
reminderSentiment = dfError(reminder,prompt)    

#############

while reminderSentiment['pos'] > reminderSentiment['neg']:
    reminderPrompt = input('Enter the date for the reminder (YY-MM-DD)')

    try:
        reminderPrompt = pd.to_datetime(reminderPrompt,format = ("%y-%m-%d"))
        reminderPrompt = reminderPrompt.date()
    except ValueError as errVar:
        print('Error description:', errVar)
        print('You entered the wrong time format.  Good bye')
        quit()
    #reminder = int(reminder.strftime("%y-%m-%d"))
    #print(reminder)
    c = input("What company do you want to set a reminder for?\n>>>")
    dfRemind = df[df['Company'] == c]
    dfRemind['Reminders'] = reminderPrompt
    df[df['Company'] == c] = dfRemind
    reminder = input('Would you like to set any more reminders?')
    reminderSentiment = SIA().polarity_scores(reminder)
    
##################### End of Reminders implementation #######################

df.to_excel(masterJobTracker, index = False)
print(df.iloc[:, : 5].fillna('').to_string(index = False))