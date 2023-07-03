file = open("PyBank/Resources/budget_data.csv", "r")
next(file)
number_of_lines = 0
total_profit_loss = 0
total_difference = 0

greatest_increase_in_profits = 0
date_greatest_increase_in_profits = ""

greatest_decrease_in_profits = 0
date_greatest_decrease_in_profits = ""
for line in file:
    if number_of_lines > 0:
        previous_profit_loss = profit_loss
    line = line.strip()
    line = line.split(",")
    this_date = line[0]
    profit_loss = line[1]
    profit_loss = int(profit_loss)
    # print(profit_loss)
    total_profit_loss = total_profit_loss + profit_loss
    if number_of_lines > 0:
        difference = profit_loss - previous_profit_loss
        total_difference = total_difference + difference

        if difference > greatest_increase_in_profits:
            greatest_increase_in_profits = difference
            date_greatest_increase_in_profits = this_date

        if difference < greatest_decrease_in_profits:
            greatest_decrease_in_profits = difference
            date_greatest_decrease_in_profits = this_date
    number_of_lines = number_of_lines + 1
file.close()
average_difference = total_difference / (number_of_lines - 1)
print ("Financial Analysis")
print ("-----------------------------\n")
print("Total Months: "+ str(number_of_lines), "\n")
print("Total: $" + str(total_profit_loss), "\n")
print("Average Change: $"+ str(round(average_difference, 2)), "\n")
print("Greatest Increase in Profits: " + str(date_greatest_increase_in_profits) + " ($"+ str(greatest_increase_in_profits)+") \n")
print("Greatest Decrease in Profits: " + str(date_greatest_decrease_in_profits) + " ($" + str(greatest_decrease_in_profits) +")")
print ("\n")

