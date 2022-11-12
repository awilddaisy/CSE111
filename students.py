import csv

def main():
    students_index= 2
    students_dict=read_dict("students.csv", students_index)
    
    print(students_dict)


def read_dict(filename, key_column_index):

    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary= {}
    with open(filename, "rt") as csv_file:
        reader=csv.reader(csv_file)
        next(reader)
    
main()