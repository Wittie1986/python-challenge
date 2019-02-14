# Import modules

import os
import csv

# Establish file path

BnkRevCSV = os.path.join("Resources", "budget_data.csv")


# Set up value containers

revenue = []
month_val = []
date = []

# Establish counting variables

row = 0
total_revenue = 0
total_change = 0
init_rev = 0

# Open file

with open(BnkRevCSV, newline="") as budget_data:
    bnksheet = csv.reader(budget_data, delimiter=",")
    bnksheet_head = next(bnksheet)

    # Begin iterations
    for x in bnksheet:
        row = row + 1
        date.append(x[0])
        revenue.append(x[1])
        total_revenue = total_revenue + int(x[1])


        end_revenue = int(x[1])
        month_chng = end_revenue - init_rev
        total_change = total_change + month_chng
        month_val.append(month_chng)
        init_rev = end_revenue
        avg_chng = (total_change/row)


        max_inc = max(month_val)
        inc_date = date[month_val.index(max_inc)]
        max_dec = min(month_val)
        dec_date = date[month_val.index(max_dec)]


# Print results

printout = (f"\nFinancial Analysis:\n"
            f"____________________\n"
            f"Total Months: {str(row)}\n"
            f"Net Profit/Losses: ${total_revenue}\n"
            f"Average Change Profit/Losses: ${round(avg_chng, 2)}\n"
            f"Greatest Increase: {inc_date} - ${max_inc}\n"
            f"Greatest Decrease: {dec_date} - ${max_dec}\n")
#printout = month_chng
print(printout)

#Export to Text File

f = open("PyBank_analysis.txt", "w")
f.write(printout)
f.close()