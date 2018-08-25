import os
import csv
import collections

lstcan=[]
lstnew=[]
inttot = 0
hcnt=0
filetouse = os.path.join("Resources", "election_data.csv")
with open(filetouse,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvfile)
    candidates = collections.Counter() 

#Read in from csv    
    for row in csvreader:
        #Create counts for individual candidates
        candidates[row[2]] += 1 
        #Create a list of unique candidates
        if row[2] not in lstcan:
            lstcan.append(row[2])
 #Get the total of votes
    inttot=sum(candidates.values())
          
    print("Election Results")
    print("-------------------------")     
    print(f"Total Votes: {inttot}")
    print("-------------------------")
  
#Do the math    
    for item in lstcan:
        pct = round(((candidates[item]/inttot)*100),4)
        lstnew.append([item,pct, candidates[item]]) 
        
#Sort the results by highest number   
    lstnew.sort(key = lambda row: row[2], reverse= True)
    
#Print the sorted results. first result is the winner    
    for item in lstnew:
        if hcnt == 0:
            winner = item[0]
        hcnt=hcnt+1
        print(f'{item[0]}: {item[1]}% {item[2]}') 

print("-------------------------")
print(f"Winner:{ winner}")
print("-------------------------")

output_path = os.path.join("Resources","Election_output.csv")
with open(output_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------"]+["-------------------"]+["-------------------"])     
    writer.writerow([f"Total Votes:"] + [inttot])
    writer.writerow(["-------------------"]+["-------------------"]+["-------------------"]) 
    writer.writerow(['Candidate'] + ['Percent of Votes'] + ['Count of Votes'])        
    for item in lstnew:
        writer.writerow([f'{item[0]}:'] + [f'{item[1]}%'] + [item[2]]) 
    writer.writerow(["-------------------"]+["-------------------"]+["-------------------"]) 
    writer.writerow([f"Winner:"] + [ winner])
    writer.writerow(["-------------------"]+["-------------------"]+["-------------------"]) 















