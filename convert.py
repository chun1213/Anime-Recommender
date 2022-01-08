import pandas as pd
import time
from datetime import datetime

def convert_time(x):
    timestamp = int(x)
    return timestamp

def clean_user(x):
    x=str(x)
    x = x.strip("::")
    return x

def strain(df, column, cutoffs):
    criteria = (lambda x: (len(x) > cutoffs[0]) & (len(x) < cutoffs[1]))
    subset = df.groupby(column).filter(criteria)
    return subset

def convert(path, data):
    with open(path, 'a') as filehandle:
        for x in data:
            user = str(x[0])
            item = str(x[1])
            rating = str(x[2])
            timestamp = str(x[3])
            line = user + "::" + item + "::" + rating + "::" + timestamp
            filehandle.write('%s\n' % line)

df = pd.read_csv('10-UserAnimeList.csv')
print("done read")
df['my_last_updated'] = df['my_last_updated'].apply(convert_time)
df['username'] = df['username'].apply(clean_user)
df.rename(columns = {'my_last_updated': 'Timestamp'}, inplace=True)
df.rename(columns = {'anime_id': 'Movie ID'}, inplace=True)
df.rename(columns = {'username': 'User'}, inplace=True)
df.rename(columns = {'my_score': 'Rating'}, inplace=True)
sub = strain(df, "Movie ID", [10, 10000])
print("strain1")
sub = strain(sub, "User", [5, 10000])
print("done")
data = sub[['User', 'Movie ID', 'Rating', 'Timestamp']].values.tolist()

path = 'full_ratings.dat'
convert(path, data)

