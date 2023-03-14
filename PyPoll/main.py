import os
import csv
data = os.path.join(r"C:\Users\sandy\OneDrive\Desktop\Python Assignments\python-challenge\PyPoll\Resources\election_data.csv")

people = []
number = []
percent = []
counter = 0


with open(data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for r in csvreader:
        
        counter = counter + 1 

        if r[2] not in people:
            people.append(r[2])
            index = people.index(r[2])
            number.append(1)
        else:
            index = people.index(r[2])
            number[index] += 1
    
     
    for votes in number:
        percentage = (votes/counter) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent.append(percentage)
    
    
    # Winning candidate
    x = max(number)
    index = number.index(x)
    winner = people[index]


# Results
print("Results")
print(f"Total Votes: {str(counter)}")
for i in range(len(people)):
    print(f"{people[i]}: {str(percent[i])} ({str(number[i])})")
print(f"Winner: {winner}")