import csv
from datetime import datetime

def log_result(accuracy, total_time):
    with open("results.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), accuracy, total_time])
