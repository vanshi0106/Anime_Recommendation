import pickle as pk
import pandas as pd

anime_data = pd.read_csv('Anime_data.csv')

similar_matrix=pk.load(open('similar_anime.pkl','rb'))

def recommend(anime):
    try:
        index = anime_data[anime_data['titles'] == anime].index[0]
        distances = sorted(list(enumerate(similar_matrix[index])),
                           reverse=True,key = lambda x: x[1])
        for i in distances[1:6]:
            print(anime_data.iloc[i[0]]['titles'])
    except:
        records = anime_data[anime_data['titles'].str.contains(anime)]['titles']
        print(records)
        index = int(input('Enter Index of the Anime : '))
        distances = sorted(list(enumerate(similar_matrix[index])),
                           reverse=True,key = lambda x: x[1])
        for i in distances[1:6]:
            print(anime_data.iloc[i[0]]['titles'])
    
recommend('One')
