#Import libraries and scan the csv file
import os
import csv

file = os.path.join(r"C:\Users\sandy\OneDrive\Desktop\Python Assignments\python-challenge\PyBank\Resources\budget_data.csv")


#variables mentioned
dates_array = []
profits_loss_array = []
total_profit_loss = 0
no_of_months = 0
x = 0
val = 0


#read the file
with open(file, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    
    csv_header = next(csvreader)

    #Track row 1 for the changes occuring in profit and loss
    row1 = next(csvreader)
    no_of_months = no_of_months + 1
    total_profit_loss = total_profit_loss + int(row1[1])
    val = int(row1[1])
    
    #Using for loop for the calculation
    for r1 in csvreader:
        dates_array.append(r1[0])
        x = int(r1[1])-val
        profits_loss_array.append(x)
        val = int(r1[1])
    
     
        #No of Months
        no_of_months = no_of_months + 1
        #Total Profit
        total_profit_loss = total_profit_loss + int(r1[1])


    #Greatest profit increase
    inc = max(profits_loss_array)
    g_index = profits_loss_array.index(inc)
    g_date = dates_array[g_index]


    #Greatest profit decrease
    dec = min(profits_loss_array)
    b_index = profits_loss_array.index(dec)
    b_date = dates_array[b_index]


    #Average change in the profit
    avg = sum(profits_loss_array)/len(profits_loss_array)
    
    
#Print the requisite details
print("Financial Analysis")
print(f"Total Months: {str(no_of_months)}")
print(f"Total: ${str(total_profit_loss)}")
print(f"Average Change: ${str(round(avg,2))}")
print(f"Greatest Increase in Profit: {g_date} (${str(inc)})")
print(f"Greatest Decrease in Profit: {b_date} (${str(dec)})")