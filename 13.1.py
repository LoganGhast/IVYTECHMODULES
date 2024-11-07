from datetime import datetime

f = open('today.txt', 'w')
f.write(str(datetime.now()))
f.close()