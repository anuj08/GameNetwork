import json
import numpy as np
import pandas as pd

thresh = 2
metafile = './meta/steam.csv'

tags = ['Indie', 'Adventure', 'Action', 'Singleplayer', 'Casual', 'Strategy', 'Simulation', 'RPG', 'Multiplayer',
         'Puzzle', 'Early Access', 'Open World', 'Story Rich', 'Difficult', 'Shooter', 'Sci-fi', '2D',
         'VR', 'Free to Play', 'Horror']

tags2 = ['Strategy', 'Simulation', 'RPG', 'Multiplayer',
         'Puzzle', 'Open World', 'Shooter', '2D',
         'VR', 'Horror']

dwieghts = {'Indie' : 1, 'Adventure' : 0.6, 'Action' : 0.6, 'Singleplayer' : 0.6, 'Casual' : 0.6, 'Strategy' : 2, 'Simulation' : 2, 'RPG' : 2, 'Multiplayer' : 0.6,
         'Puzzle' : 2.1, 'Early Access' : 0.4, 'Open World' : 0.7, 'Story Rich' : 0.6, 'Difficult' : 0.6, 'Shooter' : 1.6, 'Sci-fi' : 2, '2D' : 2.1,
         'VR' : 2.1, 'Free to Play' : 0.6, 'Horror' : 2.1}

vecs = dict()

df = pd.read_csv(metafile)
# print(df.summary())

for idx,tag in enumerate(tags2):
    with open(tag + '.json', 'r') as f:
        j = json.load(f)
        for obj in j:
            try:
                x = df[df.appid == int(obj)].positive_ratings.iloc[0]
            except IndexError:
                continue
            if df[df.appid == int(obj)].positive_ratings.iloc[0] < 800:
                continue
            if obj in vecs:
                vecs[obj][idx] = 1
            else :
                vecs[obj] = np.zeros(20)
                vecs[obj][idx] = dwieghts[tag]

d = 0
lis = list(vecs.keys())
print(len(lis))
with open('cons7.csv', 'w') as f:
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            d = np.dot(vecs[lis[i]], vecs[lis[j]])
            if(d > thresh):
                f.write("{},{},{}\n".format(lis[i], lis[j],d-1))

        




