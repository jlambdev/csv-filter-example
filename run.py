# Importing the CSV library
import csv

# Startup method, allows us to run at command line
if __name__ == '__main__':

    # open the CSV file called 'Companies', 
    # store it as a variable called 'csv_file'
    with open('./Companies.csv') as csv_file:

        # create a readable object we can loop though
        all_rows = csv.reader(csv_file, delimiter=',')

        # declare a variable called 'row' and loop through all the rows
        for row in all_rows:

            # print the item at position 3 in the array called 'row'
            print(row[3])
