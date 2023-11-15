#import the operating system (os) module
import os

#import the comma-seperated values (csv) module
import csv

#create a variable to hold the string which
#represents the path to our csv file
#the return value of the os.path.join() function is a string

count_of_months = 0
net_total = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
profit_loss_month_current = 0
profit_loss_month_previous = 0
#create a dictionary to hold profit/loss
profit_change = {}
change_in_profit_loss = 0 
budgetData_csv = os.path.join("PyBank","Resources", "budget_data.csv")
print(budgetData_csv)

#open and read csv
#alias the returned file object to the variable name budgetData_File
with open (budgetData_csv) as budgetData_File:

    #create variable to "return a reader object"
    csv_reader = csv.reader(budgetData_File, delimiter = ",")

    #read the header row and print 
    csv_header = next(budgetData_File)
    print(f"Header: {csv_header}")

#Read through each row of data after the header
#CSV Rows are Python Lists
    for row in csv_reader:
        count_of_months+=1
        net_total += int(row[1])
        
        profit_loss_month_current = int(row[1])

        if count_of_months == 1:
            #first month should not count towards the average
            profit_loss_month_previous = profit_loss_month_current
            continue

        else:
            #calculate the change in profit/loss and add to dictionary
            change_in_profit_loss = profit_loss_month_current - profit_loss_month_previous
            profit_change[row[0]] = change_in_profit_loss
            profit_loss_month_previous = profit_loss_month_current

#calculate the average            
average_change = round((sum(profit_change.values()))/len(profit_change),2)

#get the date for the maximum and minimum profit/loss
max_key = max(profit_change, key= profit_change.get)
min_key = min(profit_change, key= profit_change.get)
#get the greatest increase and decrease for profit/loss
greatest_increase = max(profit_change.values())
greatest_decrease = min(profit_change.values())

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count_of_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_key} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {min_key} (${greatest_decrease})")


#create folder
createFolder = os.path.join("PyBank","analysis")
if not os.path.exists(createFolder):
    os.makedirs(createFolder)

#create a new text file and populate with same information
budgetData_text = os.path.join("PyBank","analysis", "Results.txt")
with open(budgetData_text, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------\n")
    outfile.write(f"Total Months: {count_of_months}\n")
    outfile.write(f"Total: ${net_total}\n")
    outfile.write(f"Average Change: ${average_change}\n")
    outfile.write(f"Greatest Increase in Profits: {max_key} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {min_key} (${greatest_decrease})\n")
