import csv
import ast
import pandas as pd

movies = []
# how to read a csv into a list
with open('input.csv', 'rb') as f:
    reader = csv.reader(f)
    movies = list(reader)

my_list = []

for movie in movies:
    # print '****** one movie ******'
    for genre in ast.literal_eval(movie[1]):
        line = []
        # print '****** one genre ******'
        # print movie[0]
        # print genre['id']
        # print genre['name']
        line.append(int(movie[0]))
        line.append(genre['id'])
        # print line
        my_list.append(line)

print(my_list)
my_df = pd.DataFrame(my_list)
my_df.to_csv('movie_genre.csv', index=False, header=False)
print 'See result in movie_genre.csv file'
