# Importing the CSV library
import csv

# Import useful functions to work with dates
from datetime import datetime

# Declare a function that will look up the Region based on Person name
def get_region(region_map, person):
    return region_map.get(person, 'Unknown')

# Startup method, allows us to run at command line
if __name__ == '__main__':

    # Create a Map for finding Region
    region_map = {}
    with open('./People.csv') as people_file:
        all_people = csv.reader(people_file, delimiter=',')
        for person in all_people:
            region_map[person[0]] = person[1]

    # open the CSV file called 'Companies', 
    # store it as a variable called 'csv_file'
    with open('./Companies.csv') as csv_file:

        # specify where to create the end result
        with open('./result.csv', 'w', newline='') as output_file:

            # create a readable object we can loop though
            all_rows = csv.reader(csv_file, delimiter=',')

            # mechanism for writing new lines to the file 'output_file'
            writer = csv.writer(output_file, delimiter=',')

            # declare a variable called 'row' and loop through all the rows
            for row in all_rows:
                
                # Only for Corporate clients
                if (row[2] == 'Corporate'):

                    # Only for clients updated in November
                    parsed_date = datetime.strptime(row[1], '%d.%m.%Y')
                    if (parsed_date.month == 11):

                        # Look up the Region based on the Responsible Person
                        region = get_region(region_map, row[4])

                        # write a new row in the file 'result.csv'
                        writer.writerow([row[3], row[4], region, row[5]])
                
