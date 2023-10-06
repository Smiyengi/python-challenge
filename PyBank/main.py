#!/usr/bin/env python3
# -- coding: utf-8 --

# Necessary Imports
import csv
import os

# The path to the file is relative to the location of the running file.
# This ensures that we always get the right directory
dirname, filename= os.path.split(os.path.abspath(__file__)) # Sometimes it was not running and got this 
                                                      # from https://stackoverflow.com/a/1296522
actual_file = os.path.join(dirname, "Resources/budget_data.csv")

# Processing budget data file
with open(actual_file, 'r') as financial_dataset:
    this_file = csv.reader(financial_dataset)
    headers = next(this_file) # Headers as a list.
    total = 0 # Tracker of the totals accrued
    months = 0 # Tracker of the months elapsed.
    greatest_increase = 0 # Tracker of the greatest increase
    greatest_decrease = 0 # Tracker of the greatest decrease
    last_month = None # Placeholder for last month
    total_difference = 0
    change_in_months = 0 # tracker of change in months
    
    for row in this_file:
        this_value = int(row[1])
        months += 1
        total += this_value
        if last_month:
            difference = this_value - last_month
            total_difference += difference # tracker of differences
            change_in_months += 1 
            if greatest_increase < difference:
                greatest_increase = difference
                increase_month = row[0]
            if greatest_decrease > difference:
                greatest_decrease = difference
                decrease_month = row[0]
        last_month = this_value

    average = total_difference / change_in_months # There is one less change than the number of 
                                                  # months

# Report
financial_analysis = (
    f"Budget Analysis Output\n"
    f"----------------------------\n"
    f"Total Count of Months: {months}\n"
    f"Total Sum of Changes: ${total}\n"
    f"Average Change: ${average:.2f}\n"
    f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n"
    f"Greatest Increase in Profits: {decrease_month} (${greatest_decrease})\n"
    )

# Report printed to terminal
print(financial_analysis, end="") 

# Report printed to file
analysis_file = os.path.join(dirname, "analysis/financial_analysis.txt")
with open(analysis_file, "w") as financial_dataset:
    print(financial_analysis, file=financial_dataset)