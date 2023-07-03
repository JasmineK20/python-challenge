file = open("../Resources/budget_data.csv", "r")
next(file)
number_of_lines = 0
total_profit_loss = 0
total_difference = 0

max_increase_profits = 0
date_max_increase_profits = ""

max_decrease_profits = 0
date_max_decrease_profits = ""
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

        if difference > max_increase_profits:
            max_increase_profits = difference
            date_max_increase_profits = this_date

        if difference < max_decrease_profits:
            max_decrease_profits = difference
            date_max_decrease_profits = this_date
    number_of_lines = number_of_lines + 1
file.close()
average_difference = total_difference / (number_of_lines - 1)
print("number_of_lines", number_of_lines)
print("total_profit_loss", total_profit_loss)
print("average_difference", average_difference)
print("max_increase_profits", max_increase_profits)
print("date_max_increase_profits", date_max_increase_profits)
print("max_decrease_profits", max_decrease_profits)
print("date_max_decrease_profits", date_max_decrease_profits)
