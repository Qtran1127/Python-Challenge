PyBank
import os
import csv 
input_title = input("Revenue:")
cvspath = csvpath = os.path.join('Resources', 'budget_data.csv')
total_month =0
Net_total = 0
avg_change = 0
loss = 0
gain = 0
inc_profit = "unknown"
dec_loss = "unknown"
current_month = 0
prior_month = 0
change = 0

with open(csvpath) as profitloss_data:
    reader = csv.DictReader(profitloss_data)
    for row in reader:
        prior_month = current_month
        if prior_month == 0:
            exclude =int(row["Profit/Losses"])
        Net_total = Net_total+ int(row["Profit/Losses"])
        total_month = total_month+1
        #calculate current change in month profit/losses and keeps total
        current_month = int(row["Profit/Losses"])
        change = current_month - prior_month
        avg_change = avg_change + change
        if change > gain:
            gain = change
            inc_profit = row["Date"]
        elif change < loss:
            loss = change
            dec_loss = row ["Date"]
avg_change = avg_change - exclude
change_percentage =avg_change/(total_month-1)


text_file = open('Financial Analysis.txt', 'w')
print("  ")
text_file.write(" \n")
text_file.write("-------------------------------------------------------------------- \n")
print(" Financial Analysis")
text_file.write("  Financial Analysis \n")
print("--------------------------------------------------------------------")
text_file.write("-------------------------------------------------------------------- \n")
print("Total number of months in period: " + str(total_month))
text_file.write("Total number of months in period: " + str(total_month) + "\n")
print("Total Revenue in period: $ " + str(Net_total))
text_file.write("Total Revenue in period: $ " + str(Net_total) + "\n")
print("Average monthly change in Revenue : $" + str(change_percentage))
text_file.write("Average monthly change in Revenue : $" + str(change_percentage) + "\n")
print("Greatest monthly increase in Revenue : " + str(inc_profit) + "   $ " + str(gain))
text_file.write("Greatest monthly increase in Revenue : " + str(inc_profit) + "   $ " + str(gain) + "\n")
print("Largest monthly decrease in Revenue : " + str(dec_loss) + "   $ " + str(loss))
text_file.write("Largest monthly decrease in Revenue : " + str(dec_loss) + "   $ " + str(loss) + "\n")
print("--------------------------------------------------------------------")
text_file.write("-------------------------------------------------------------------- \n")
text_file.close()
