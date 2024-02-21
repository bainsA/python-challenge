import csv
date = []
profitloss = []
change = []
f = open("PyBank.txt", 'w')
# I created three list for each of the column heads
# First step is to open the csv file called PyBank
with open('C:/Users/Karamjit/Documents/PyBank.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}", file = f)

    for row in csvreader:
        print(row, file = f)
        date.append(row[0])
        profitloss.append(row[1])
        change.append(int(row[1]))
# The above 'for loop' has the lists appended with the original data file information for each column head
print(date, file = f)
print(profitloss, file = f)
print(change, file = f)
print("Financial Analysis", file = f)
print("-------------------", file = f)
num_of_months = len(date)    
print("Total months: " + str(num_of_months), file = f)
# The number of months is determined using the len() function
total = 0
for i in profitloss:
    total += int(i)
print("Total: $" + str(total), file = f)
# Above 'for loop' goes through the profitloss list to compute the total sum

difference = [change[n]-change[n-1] for n in range(1, len(change))]
avechange = sum(difference)/float(len(change)-1)
rounded = round(avechange, 2)
print("Average Change: $" + str(rounded), file = f)
# Difference represents the change of Profit/Loss across all the entries
# Average change takes the total differences and divides by the number of entries
# We round the Average Change to two decimal places

max_value = max(difference)
max_index = difference.index(max_value)
min_value = min(difference)
min_index = difference.index(min_value)
print("Greatest Increase In Profits: " + str(date[max_index+1]) + " ($" + str(max_value) + ")", file = f)
print("Greatest Decrease in Profits: " + str(date[min_index+1]) + " ($" + str(min_value) + ")", file = f)

# Max value is the maximum difference in Profit/Loss, which is located using the max() function
# Location of the index for this maximum change is found through using difference.index(max_value). The index helps determine the corresponding date of change
# Min value is likewise the minimum differece in Profit/Loss and located through min() function. Index of change found through difference.index(min_value)
# Important to add 1 as seen in date[max_index+1] and date[min_index+1]. This marks the correct end of the change. 
f.close()