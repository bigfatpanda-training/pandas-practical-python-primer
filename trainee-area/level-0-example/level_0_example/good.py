"""
This programs connects to an API and presents selected data to user.
"""
import requests

from .MEANPANDA import api_url, text_strings
from level_0_example import MEANPANDA

divider = '-' * 25

def print_scores(scores):
    """
    {'sat_math_avg_score': '402', 'num_of_sat_test_takers': '70', 'dbn': '01M450', 'school_name': 'EAST SIDE COMMUNITY SCHOOL', 'sat_critical_reading_avg_score': '377', 'sat_writing_avg_score': '370'}

    """
    print(divider)
    print("{}: {}\n{}: {}".format(
        MEANPANDA.text_strings['one'], scores['school_name'],
        text_strings['two'], scores['num_of_sat_test_takers']))
    print("Average Math Score: {}\n"
          "Average Reading Score: {}\n"
          "Average Writing Score: {}".format(
              scores['sat_math_avg_score'],
              scores['sat_writing_avg_score'],
              scores['sat_critical_reading_avg_score']))

get_result = requests.get(api_url)
school_sat_scores = get_result.json()[0:5]

for school_score in school_sat_scores:
    print_scores(school_score)
