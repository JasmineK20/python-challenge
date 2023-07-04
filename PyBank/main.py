#open csv file 
file = open("PyBank/Resources/budget_data.csv", "r")
next(file)
#define
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

output_text = "Financial Analysis\n\n"
output_text += "----------------------------\n\n"
output_text += f"Total Months: {number_of_lines}\n\n"
output_text += f"Total: ${total_profit_loss}\n\n"
output_text += f"Average Change: ${round(average_difference,2)}\n\n"
output_text += f"Greatest Increase in Profits: {date_greatest_increase_in_profits} (${greatest_increase_in_profits})\n\n"
output_text += f"Greatest Decrease in Profits: {date_greatest_decrease_in_profits} (${greatest_decrease_in_profits})\n\n"

print(output_text)

output_file = open ("PyBank/analysis/budget_data.txt","w")
output_file.write(output_text)
output_file.close()