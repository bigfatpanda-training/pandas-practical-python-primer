import sys, os, csv, requests, level_0_example.MEANPANDA as MEANPANDA
dv='-'*25
def PRSCORES(i):
    """
    {'sat_math_avg_score': '402', 'num_of_sat_test_takers': '70', 'dbn': '01M450', 'school_name': 'EAST SIDE COMMUNITY SCHOOL', 'sat_critical_reading_avg_score': '377', 'sat_writing_avg_score': '370'}

    """
    print(dv)
    print("{}: {}\n{}: {}".format(MEANPANDA.text_strings['one'], i['school_name'], MEANPANDA.text_strings['two'], i['num_of_sat_test_takers']))
    print("Average Math Score: {}\nAverage Reading Score: {}\nAverage Writing Score: {}".format(i['sat_math_avg_score'], i['sat_writing_avg_score'], i['sat_critical_reading_avg_score']))

NYCjson = requests.get(MEANPANDA.api_url)
dfd = NYCjson.json()[0:5]
for i in dfd: PRSCORES(i)