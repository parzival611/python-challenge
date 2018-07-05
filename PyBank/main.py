import os
import csv

# Files to load (Remember to change these)
file_to_load = "Resources/budget_data.csv"

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.reader(revenue_data)

    # use of next to skip first title row in csv file
    next(reader) 
    revenue = []
    date = []
    rev_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in reader:
        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   

        avg_rev_change = sum(rev_change)/len(rev_change)
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])

    print("Average Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Profits:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")

    # Zip lists together
    # cleaned_csv = zip(date, revenue, round(avg_rev_change), max_rev_change, min_rev_change)
    cleaned_csv = zip(date, revenue)

    # Set variable for output file
    output_file = os.path.join("budget_final.csv")

    #  Open the output file
    with open(output_file, "w") as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(["Date", "Revenue"])

        # Write in zipped rows
        writer.writerow(cleaned_csv)
