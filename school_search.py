import csv 
import time
from count_schools import get_school_data

def search_schools(query):
    keys = query.upper().split(" ")
    schools = get_school_data()[1]
    most_in_common = [0,0,0] 
    top_3 = [[],[],[]]
    start_time = time.time() #begin timer 
    for school in schools:
        elements = school[3].split(" ") + school[4].split(" ") + school[5].split(" ") #combine all search terms to be compared to school dataset
        if common_member(keys,elements): # whichever schools have the most keywords in common with the query are returned in order of most matching terms. 
            if common_member(keys,elements) > min(most_in_common):
                top_3[most_in_common.index(min(most_in_common))] = school
                most_in_common[most_in_common.index(min(most_in_common))] = common_member(keys,elements)
    end_time = time.time() 
    print('Results for "' + str(query) + '" (search took: ' + str(round(end_time - start_time,3)) + "s)")
    while 0 in most_in_common: #in the case that there are no common terms 
        del top_3[most_in_common.index(0)]
        del most_in_common[most_in_common.index(0)]
    i = 1 
    while len(top_3) > 0: 
        print(str(i) + ". " + str(top_3[most_in_common.index(max(most_in_common))][3]))
        print(str(top_3[most_in_common.index(max(most_in_common))][4]) + ", " + str(top_3[most_in_common.index(max(most_in_common))][5]))
        top_3.remove(top_3[most_in_common.index(max(most_in_common))])
        most_in_common.remove(max(most_in_common))
        i = i + 1


#helper function checks to see any of the words searched are present in a a given school description  
def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return len((a_set & b_set))
    else: 
        return False
           