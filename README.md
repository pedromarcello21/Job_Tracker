# Job Tracker Program

This repository provides the tools for those looking for their next professional opportunity.  I've created a program that assists a user's journey in tracking their progress with company prospects.  The inspiration for this program came from Steve Dalton's book, "The 2 Hour Job Search", who demonstrates a technical approach to maximize one's probability of landing a professional opportunity.

The Master_Job_Tracker is the excel file that is written to and read by the program and consists of 5 columns, Company, Alumni, Motivation, Postings, and Reminders.  Here are the indications of each column:

Company: A list companies provided by the user.  This column is the index for both the tracker file and python program.
Alumni: Indicates if the user knows of anyone working at the company (Y/N).  
Motivation: A scale of how interested the user is in the company.  The levels are High, Medium, or Low (H/M/L). 
Postings: Indication if the company has any job vacancies open on any professional website such as LinkedIn, Glassdoor, ZipRecuiter (Y/N).  
Reminders: Consists of dates that serve as reminders set by the user to follow up with the Company.  
****** Reminder values must be provided in the following date format: YY-MM-DD  ********

Once all files are saved within the same directory and the path variable has been updated to reflect the user's directory, it's time to run the program.  I wrote this program with the Python IDE, Thonny.  I'm currently a graduate student at the Gabelli School of Business and this is the IDE we used for our Python course.

When the program runs, the first thing the user will recognize is an alert to follow up with company prospects for reminders that have been set for today, tomorrow, and/or in a couple days.  Any old reminders will be deleted.  The user is prompted if any changes should be made to the Master_Job_Tracker excel file.  If the user provides an answer with positive sentiment ("yes", "yeah","I'd love too") the user has the choice to add, delete, or ammend an entry of the excel file.  An answer of negative sentiment ("no","nope") will bring the user to the next segment of the program.  Here's what happens depending on the user's choice:

************* Company names provided by the user are case sensitive ******************
add: The program asks what company to add to the tracker along with providing the values for the company's Alumni, Motivation, and Postings keys.
delete: The program asks what company to delete from the tracker.
ammend: The program asks what company to ammend from the tracker and proceedes to prompt the user to provide the values for the company's Alumni, Motivation, and Postings keys.

Once the user doesn't want to make any more changes to the tracker, the program then prompts the user if any upcoming reminders should be set.  After the user provides an answer of positive sentiment ("yes", "yeah","I'd love too"), the user must enter a date with format YY-MM-DD or else the program will terminate without saving any changes to the Master_Job_Tracker.  An answer of negative sentiment ("no","nope") will bring the user to the next segment of the program.  

Once there are no more reminders to log, the program prints the updated Company, Alumni, Motivation, and Postings keys to the console and rewrites the Master_Job_Tracker file to reflect all updated values.  


