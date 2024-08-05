import csv


with open("login_data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

    if not any(row for row in reader):
        print("CSV file is empty")
        from log_in_page import *

    else:
        from main_page import *
