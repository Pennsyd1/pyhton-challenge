#Create path to CSV file
import os
import csv

#Open CSV file and creates two lists for values in date column and profit column then prints the total values in date column as "total months:"
PyBank_csv = os.path.join("..", "Instructions", "PyBank",
                          "Resources", "budget_data.csv")

with open(PyBank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    
    monthcount = []
    total_profit = []
    for col in csv_reader:
        monthcount.append(col[0])
        total_profit.append(col[1])
print(f"Total Months: {int(len(monthcount))}")

#Calculates sum of totals in total_profit list and prints as "total: $"
profit = 0
for num in range(0, len(total_profit)):
    profit = int(profit) + int(total_profit[num])
print(f"Total: ${int(profit)}")

#Creates a list containing the change in value from month to month then prints the largest number as "greastest increase:" and the lowest number as "greatest decrease"
list_dif = [int(total_profit[i + 1]) - int(total_profit[i]) for i in range(len(total_profit) - 1)]
list_dif.sort()
print(f"Greatest Decrease in profits: ${int(list_dif[0])}")
print(f"Greatest Increase in profits: ${int(list_dif[84])}")

#Calculates the average of values in the list previously created for change in profits (list_dif) then prints as "average change:"
def Average(list_dif):
    return sum(list_dif) / len(list_dif)
average = Average(list_dif)
print(f"Average Change: $ {float(round(average, 2))}")

#Creates text file that prints results of analysis
PyBanktxt = open("file.txt", "w")
PyBanktxt.write("Financial Analysis \n")
PyBanktxt.write("Total Months: 86 \n")
PyBanktxt.write("Total: $22564198 \n")
PyBanktxt.write("Average Change: $ -8311.11 \n")
PyBanktxt.write("Greatest Decrease in profits: $-1825558 \n")
PyBanktxt.write("Average Change: $ -8311.11 \n")