import sys, os, csv, requests                                                   # Multiple Imports / 1 Line, Improper Order
dv='-'*25                                                                       # Bad White Space
def PRSCORES(Item):                                                             # Invalid Function Name / Incorrect Whitespace rel. Function Def
    """
    {'sat_math_avg_score': '402', 'num_of_sat_test_takers': '70', 'dbn': '01M450', 'school_name': 'EAST SIDE COMMUNITY SCHOOL', 'sat_critical_reading_avg_score': '377', 'sat_writing_avg_score': '370'}

    """
    print(dv)                                                                   # Implicit Global Variable Use
    print("School: {}".format(i['school_name']))
    print("Number of Students: {}".format(i['num_of_sat_test_takers']))
    print("Average Math Score: {}\nAverage Reading Score: {}\nAverage Writing Score: {}".format(i['sat_math_avg_score'], i['sat_writing_avg_score'], i['sat_critical_reading_avg_score']))

NewYorkCitySATdatadownload = requests.get("https://data.cityofnewyork.us/resource/f9bf-2cp4.json")  # Too Long / Bad Name
dfd = NewYorkCitySATdatadownload.json()[0:5]
for i in dfd: PRSCORES(i)                                                         # multiple statements on one line.