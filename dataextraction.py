import csv
import re

def data_extractor():
    """ Function that reads in the csv file, counts the data required using regular expressions and prints it back to the terminal in a nicely formatted way """

# Opens the csv file and read it in
    with open('NYPD_Arrests_Data__Historic_.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

# Create four different counters for the variables that are needed
        total_arrests2012_2013 = 0
        total_arrests2016_2017 = 0
        marijuana_arrests2012_2013 = 0
        marijuana_arrests2016_2017 = 0

# Create the regular expression patterns that allow us to search trough the data
        p = re.compile('.*201[23]')
        p2 = re.compile('.*201[67]')
        pm = re.compile('MARIJUANA, POSSESSION.*')

# Loop trough the data once to count all the required data using conditions
        for row in csv_reader:
            if p.match(row[1]) and pm.match(row[3]):
                marijuana_arrests2012_2013 += 1
                total_arrests2012_2013 += 1
            elif p.match(row[1]):
                total_arrests2012_2013 += 1
            elif p2.match(row[1]) and pm.match(row[3]):
                marijuana_arrests2016_2017 += 1
                total_arrests2016_2017 += 1
            elif p2.match(row[1]):
                total_arrests2016_2017 += 1

# Print out the results of the countings in a formatted way
    print("Total arrests made for marijuana related crimes in the period 2012-2013: {0}".format(marijuana_arrests2012_2013))
    print("Total arrests made for marijuana related crimes in the period 2016-2017: {0}".format(marijuana_arrests2016_2017))
    print("Total arrests made in the period 2012-2013: {0}".format(total_arrests2012_2013))
    print("Total arrests made in the period 2016-2017: {0}".format(total_arrests2016_2017))

    

data_extractor()
