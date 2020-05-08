import os
import csv

# path for file
budget_csv = os.path.join("Resources", "budget_data.csv")

# lists to store data
months = []
profits_losses = []

# open csv file to read
with open(budget_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        months.append(row[0])
        profits_losses.append(row[1])

# total the months
total_months = len(months)

# sum the profits_losses
total_p_l = 0

# set initial value
x = 0
for x in range(total_months):
    total_p_l = total_p_l + int(profits_losses[x])

# calculate change in revenue per month
change_per_month = []

# variables to represent current value and previous value
y = 0
z = 0
for y in range(0, total_months):
    if y == 0:
        change_per_month.append(0)
    else:
        change_per_month.append(int(profits_losses[y]) - int(profits_losses[z]))
        z = z+1

# average change per month
Total_changes = 0
c = 0
for c in range(total_months):
    Total_changes = Total_changes + int(change_per_month[c])

average_change = int(Total_changes) / int(total_months - 1)

# find greatest profit
greatest_profit = max(change_per_month)
profit_index = change_per_month.index(greatest_profit)
profit_date = months[profit_index]

#find greatest loss
greatest_loss = min(change_per_month)
loss_index = change_per_month.index(greatest_loss)
loss_date = months[loss_index]

# write summary to txt file
analysis_txt = os.path.join("analysis", "Financial_analysis.txt")
with open(analysis_txt, "w") as txtfile:
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("----------------------" + "\n")
    txtfile.write("Total Months: " + str(total_months) + "\n")
    txtfile.write("Total Revenue: " + "$" + str(total_p_l) + "\n")
    txtfile.write("Average Revenue Change: " + str(average_change) + "\n")
    txtfile.write("Greatest Increase in Profits: " + str(profit_date) + " " + str(greatest_profit) + "\n")
    txtfile.write("Greatest Loss in Profits: " + str(loss_date) + " " + str(greatest_loss) + "\n")

# print results in terminal
print("Financial Analysis")
print("----------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$" + str(total_p_l))
print("Average Revenue Change: " + str(average_change))
print("Greatest Increase in Profits: " + str(profit_date) + " " + str(greatest_profit))
print("Greatest Loss in Profits: " + str(loss_date) + " " + str(greatest_loss))



    # change = 0
    # for row in csvreader:
    
    #     months.append(str(row[0]))

    #     profits_losses.append(int(row[1]))

    #     if change == int(row[1]):
    #         continue

    #     avg_change.append(int(row[1]) - change)

    #     change = int(row[1])
        
       
    # print("Financial Analysis")
    # print("--------------------")
    # print(len(months))
    # print("$" + str(sum(profits_losses)))
    # print(sum(avg_change) / len(avg_change))
    # print(min(avg_change))
    # print(max(avg_change))
    # print(min_date)

    # min_change = min(avg_change)
    # for row in csvreader:
    #     if min_change == int(row[1]):
    #         min_date.append(row[0]) 