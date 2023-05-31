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

# for author in authors:
#     print('')
#     print('-------')
#     print('Author: ' + author.name)
#     print('-------')
#
#     print('\t' + '---------------')
#     print('\t' + 'Publication(s): ' + str(len(author.publications)))
#     print('\t' + '---------------')
#     for publication in author.publications:
#         print('\t' + publication.key)
#         print('\t' + '\t' + publication.title)
#         print('\t' + '\t' + str(publication.journal))
#         print('\t' + '\t' + str(publication.year))

# Laufzeit
end_date_time = datetime.now()
diff_date_time = end_date_time - start_date_time

# Ausgabe Console
print('-------------------------------------------------------------')
print("End time: ", end_date_time.strftime("%Y-%m-%d %H:%M:%S"))
print("Duration: ", diff_date_time)
print('-------------------------------------------------------------')


print(authors)

search_string = input('Exit => press any button')

