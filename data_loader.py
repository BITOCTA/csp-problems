import csv
import re


def load_sudoku():
    with open('data/Sudoku.csv', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        result = []
        for row in reader:
            sudoku = list(iter(re.findall(r'\d|\.', row[2])))
            if len(sudoku) == 81:
                result.append(list(sudoku))

    return result
