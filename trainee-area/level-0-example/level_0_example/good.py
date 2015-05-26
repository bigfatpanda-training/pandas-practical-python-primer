"""
This programs connects to an API and presents selected data to user.
"""
import requests

import level_0_example.meanpanda as meanpanda

dv = '-' * 25
dv.capitalize()


def prscores(i):
    """
    {'sat_math_avg_score': '402', 'num_of_sat_test_takers': '70', 'dbn': '01M450', 'school_name': 'EAST SIDE COMMUNITY SCHOOL', 'sat_critical_reading_avg_score': '377', 'sat_writing_avg_score': '370'}

    """
    print(dv)
    print("{}: {}\n{}: {}".format(
        meanpanda.text_strings['one'], i['school_name'],
        meanpanda.text_strings['two'], i['num_of_sat_test_takers']))
    print("Average Math Score: {}\n"
          "Average Reading Score: {}\n"
          "Average Writing Score: {}".format(
              i['sat_math_avg_score'],
              i['sat_writing_avg_score'],
              i['sat_critical_reading_avg_score']))

get_result = requests.get(meanpanda.api_url)
dfd = get_result.json()[0:5]
for i in dfd: prscores(i)
