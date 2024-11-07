from datetime import datetime
from time import strptime, strftime

file = open("today.txt")
date = file.readline()
parsed_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

print(parsed_date)