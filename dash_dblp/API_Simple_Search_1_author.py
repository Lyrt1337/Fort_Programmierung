import dblp
from datetime import datetime

start_date_time = datetime.now()
print('-------------------------------------------------------------')
print("Start time: ", start_date_time.strftime("%Y-%m-%d %H:%M:%S"))
print('-------------------------------------------------------------')

print('----------------------')
print('DBLP find: michael ley')
print('----------------------')
authors = dblp.search('michael ley')

for author in authors:
    print('Author: ' + author.name + '\t' + '\t' + 'Publications: ' + str(len(author.publications)))

# Laufzeit
end_date_time = datetime.now()
diff_date_time = end_date_time - start_date_time

# Ausgabe Console
print('-------------------------------------------------------------')
print("End time: ", end_date_time.strftime("%Y-%m-%d %H:%M:%S"))
print("Duration: ", diff_date_time)
print('-------------------------------------------------------------')

