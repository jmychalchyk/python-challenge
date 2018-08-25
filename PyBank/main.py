
 
import os
import csv
import datetime
 
#open CSV file
budgetcsv = os.path.join("Resources","budget_data.csv")
with open(budgetcsv,newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvfile)
#Read from CSV file
    intmn=0
    prevmn=0
    intnet=0
    intprev=0
    totflavg=0.0
    cntavg =1
    intavg=0
    intminavg=0
    intmaxavg = 0
    for row in csvreader:
#Convert date column to readable format and count months '86
        dtcur = datetime.datetime.strptime(row[0],'%b-%Y').date()
#The total number of months included in the dataset
        if str(dtcur.month)  != str(prevmn):     
            intmn=intmn +1
            prevmn = dtcur.month
#The total net amount of "Profit/Losses" over the entire period            
        intnet=intnet + int(row[1]) 
#The average change in "Profit/Losses" between months over the entire period 
        if intprev != 0:
            intavg = int(row[1]) - intprev
        intprev = int(row[1])   
        totflavg = totflavg + intavg
#The greatest increase in profits (date and amount) over the entire period
        if intavg !=0 and intavg > intmaxavg:
            intmaxavg =intavg 
            maxdt = dtcur.strftime('%b-%Y') 
 #The greatest decrease in losses (date and amount) over the entire period           
        if intavg !=0 and intavg < intminavg:
            intminavg =intavg 
            mindt = dtcur.strftime('%b-%Y')  
 
flavgchng ='{:,.2f}'.format((totflavg/(intmn-1)))

print ("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {intmn}")
print(f"Total: ${intnet}")
print(f"Average Change: ${flavgchng}")
print(f"Greatest Increase in Profits: {maxdt} (${intmaxavg})")
print(f"Greatest Decrease in Profits: {mindt} (${intminavg})")

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
output_path = os.path.join("Resources","budget_output.csv")
with open(output_path, 'w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------------------"])
    writer.writerow([f"Total Months: {intmn}"])
    writer.writerow([f"Total: ${intnet}"])
    writer.writerow([f"Average Change: ${flavgchng}"])
    writer.writerow([f"Greatest Increase in Profits: {maxdt} (${intmaxavg})"])
    writer.writerow([f"Greatest Decrease in Profits: {mindt} (${intminavg})"])

