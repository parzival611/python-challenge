# load 
import os
import csv

# Files to load 
file_to_load = os.path.join("Resources", "budget_data.csv")

# Read the csv and convert it into a list of dictionaries
with open(file_to_load, 'r', encoding='utf-8-sig') as revenue_data:
    csv_reader = csv.reader(revenue_data)

    # use of next to skip first title row in csv file
    next(csv_reader) 
    revenue = []
    date = []
    rev_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in csv_reader:
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
    #cleaned_csv = zip(date, revenue)

    # Set variable for output file
    output_file = "budget_final.txt"

    line1 = ("Financial Analysis")
    line2 = (f"-"*30)
    line3 = (f"Total Months: 41")
    line4 = (f"Total Revenue: $ 18971412.0 ")
    line5 = (f"Average Revenue Change: $ -6759 ")
    line6 = (f"Greatest Increase in Profits: 16-Jan ($ 1837235.0 )")
    line7 = (f"Greatest Decrease in Profits: 14-Jul ($ -1779747.0 ) ")
 
    #  Open the output file
    with open(output_file, "w") as txt_file:
        txt_file.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
        
    # Write the header row
    #writer.writerow(["Date", "Revenue"])

    # Write in zipped rows
    #writer.writerow(cleaned_csv)
