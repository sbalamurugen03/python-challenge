#import the operating system (os) module
import os

#import the comma-seperated values (csv) module
import csv

#create a variable to hold the string which
#represents the path to our csv file
#the return value of the os.path.join() function is a string
#electionData_csv = os.path.join("..","Resources", "election_data.csv")
#electionData_csv_Test = os.path.join(os.getcwd(),"Resources", "election_data.csv")
#print(electionData_csv_Test)
electionData_csv = os.path.join("PyPoll","Resources", "election_data.csv")
print(electionData_csv)
votes_Per_Candidate = 0
total_Votes = 0
#create dictionary to hold voter/votes
vote_Dict = {}
#open and read csv
#alias the returned file object to the variable name electionData_File
with open (electionData_csv) as electionData_File:

    #create variable to "return a reader object"
    csv_reader = csv.reader(electionData_File, delimiter = ",")

    #read the header row
    csv_header = next(electionData_File)
    print(f"Header: {csv_header}")

#Read through each row of data after the header
#CSV Rows are Python Lists
    for row in csv_reader:
        total_Votes+=1
        if row[2] not in vote_Dict:
            vote_Dict[row[2]] = 1
        else:
            vote_Dict[row[2]] +=1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_Votes}")
print("-------------------------")
#iterate through dictionary and print values
for key, value in vote_Dict.items():
    votes_Per_Candidate = round(((value/total_Votes) * 100),3)
    print(key + ': ' +str(votes_Per_Candidate)+ '% ('+str(value)+ ')')
winner = max(vote_Dict, key = vote_Dict.get)
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

#create folder
createFolder = os.path.join("PyPoll","analysis")
if not os.path.exists(createFolder):
    os.makedirs(createFolder)

#create a new text file and populate with same information
electionData_text = os.path.join("PyPoll","analysis", "Results.txt")
with open(electionData_text, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("\n")
    outfile.write("-------------------------\n")
    outfile.write("\n")
    outfile.write(f"Total Votes: {total_Votes}\n")
    outfile.write("\n")
    outfile.write("-------------------------\n")
    for key, value in vote_Dict.items():
        votes_Per_Candidate = round(((value/total_Votes) * 100),3)
        outfile.write(key + ': ' +str(votes_Per_Candidate)+ '% ('+str(value)+ ')\n')
    outfile.write("-------------------------\n")
    outfile.write("\n")
    outfile.write(f'Winner: {winner}\n')
    outfile.write("\n")
    outfile.write("-------------------------\n")
