#  brandon treu 900704435

import csv
from countyData import CountyData

with open("/Users/brandontreu/PycharmProjects/CIS189/Module12/Iowa 2010 Census Data Population Income.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    county = {}

    for row in csv_reader:
        #skip first line header
        if line_count == 0:
            line_count += 1
            continue
        if str(row[1]) == 'Iowa State' or str(row[1]) == 'United States':
            pass
        else:
            county[str(row[1])] = CountyData(row[0], row[2], row[3], row[4], row[5], row[6])

    def find_population_per_household(cnty):
        pop = county[str(cnty)].pop
        pop = int(pop.replace(',', ''))

        households = county[str(cnty)].num_house
        households = int(households.replace(',', ''))

        pop_per_household = pop/households
        return "{:.2f}".format(pop_per_household)


    def total_population():
        total = 0
        for key in county:
            total += int(county[key].pop.replace(',',''))
        return total




print(find_population_per_household('Polk'))
print(total_population())