import csv 
import itertools
#read and format the CSV data, return the fields and the data itself as two seperate items 
def get_school_data(): 
    fields = [] 
    rows = []  
    with open("school_data.csv", 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
        fields = next(csvreader)  
        for row in csvreader: 
            rows.append(row) 
    return fields,rows

def print_counts():
    schools = get_school_data()
    print(schools[0]) #print the number of schools 
    states = {}
    Metro_centric_locals = {}
    cities = {}
    for school in schools[1]:
        #states 
        if school[5] not in states:
            states[school[5]] = 1
        else: 
            states[school[5]] += 1 
        #Metro centric locals 
        if school[8] not in Metro_centric_locals:
            Metro_centric_locals[school[8]] = 1
        else: 
            Metro_centric_locals[school[8]] += 1 
        #cities
        if school[4] not in cities:
            cities[school[4]] = 1
        else: 
            cities[school[4]] += 1 
    max_keys = [k for k, v in cities.items() if v == max(cities.values())] #find the max number of schools in a single city 
    #print results
    print('total schools: ' + str(len(schools[1])))
    print('Schools by State:')
    for key, value in states.items():
        print(key, ' : ', value)
    print('Schools by Metro-centric locale:')
    for key, value in Metro_centric_locals.items():
        print(key, ' : ', value)
    print('city with most schools: ' + str(max_keys[0]) + ' (' + str(cities[max_keys[0]]) + ' schools)')
    print('Unique cities with at least one school: ' + str(len(cities)))

  
