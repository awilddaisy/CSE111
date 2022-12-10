# Climbing Route Consensus Averaging
 ## This program will create exact and accurate averaging on routes based on climber's consensus.
 ### I chose this program because in my workplace, climbers will add their opinions on the difficulty
 #### of a route. Sometimes this gets hazy because of the + and - that can change the grade. I wanted
 ##### to have a program that calculated the most accurate average of consensus despite that. 

import math

def main():
    input_grades = []
    # For easy testing 
    # input_grades = ["5.7", "5.7+", "5.8", "5.9", "5.9+", "5.10-","5.6","5.7","5.8","5.9-"]

    # User inputs grades
    while len(input_grades) <= 9 :
        input_grade=input("Enter your grade: ")
        input_grades.append(input_grade)
    grades_dict = make_grade_dict()
    keys_dict = make_key_dict()

    GRADE_INDEX = 0
    VALUE_INDEX = 1

    num_list = []
    # Take the input values and create a list
    for count in input_grades:
        num=grades_dict[count]
        num_list.append(num[0])
    # print(num_list)

    # Calculate the sum of the list above and divde by 10
    # to find the average
    grade_sum = sum(num_list)
    grade_sum = int(grade_sum)
    average = (grade_sum) / 10
    average = round(average)

    # Pulls calculated average from diff. dictionary
    average = str(average)
    # print(average)
    get_average = keys_dict[average]
    print(f"The exact grade is: {get_average}.")
    
def make_grade_dict():
    grade_dict = {
        "5.6-": [0],
        "5.6": [1],
        "5.6+" : [2],
        "5.7-" : [3],
        "5.7" : [4],
        "5.7+" : [5],
        "5.8-" : [6],
        "5.8" : [7],
        "5.8+" : [8],
        "5.9-" : [9],
        "5.9" : [10],
        "5.9+" : [11],
        "5.10-" : [12],
        "5.10" : [13],
        "5.10+" : [14],
        "5.11-" : [15],
        "5.11" : [16],
        "5.11+" : [17],
        "5.12-" : [18],
        "5.12" : [19],
        "5.12+" : [20],
        "5.13-" : [21],
        "5.13" : [22],
        "5.13+" : [23],
        "5.14-" : [24],
        "5.14" : [25]
    }
    return grade_dict

def make_key_dict():
    key_dict = {
        "0" : ['5.6-'],
        "1" : ['5.6'],
        "2" : ['5.6'],
        "3" : ['5.7-'],
        "4" : ['5.7'],
        "5" : ['5.7+'],
        "6" : ['5.8-'],
        "7" : ['5.8'],
        "8" : ['5.8+'],
        "9" : ['5.9-'],
        "10" : ['5.9'],
        "11" : ['5.9+'],
        "12" : ['5.10-'],
        "13" : ['5.10'],
        "14" : ['5.10+'],
        "15" : ['5.11-'],
        "16" : ['5.11'],
        "17" : ['5.11+'],
        "18" : ['5.12-'],
        "19" : ['5.12'],
        "20" : ['5.12+'],
        "21" : ['5.13-'],
        "22" : ['5.13'],
        "23" : ['5.13+'],
        "24" : ['5.14-'],
        "25": ['5.14']
        }
    return key_dict

main()

# Program by Daisy Mueller @ BYU-Idaho
## December 10, 2022
