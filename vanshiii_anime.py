import tkinter as tk
import pandas as pd
import pickle as pk
import random

anime = pd.read_csv('Anime_data.csv')

similar_matrix=pk.load(open('similar_anime.pkl','rb'))

def find_movie():
    anime_name = text_area.get(0.0,tk.END)
    anime_name = anime_name.strip()
    recommend(anime_name)

def recommend(anime_name):
    # try:
        index = anime[anime['titles'] == anime_name].index[0]
        distances = sorted(list(enumerate(similar_matrix[index])),
                           reverse=True,key = lambda x: x[1])
        # recommended_anime=[]
        count = 1
        for index,_ in distances[1:6]:
            title = anime.iloc[index]['titles']
            movie_labels[f'movie{count}'].config(text=title)
            count +=1
            # return recommended_anime
    # except:
    #     tk.Label(text='Please Enter Valid Movie Name',font=('Impact',20)).pack()
        # records = anime[anime['titles'].str.contains(anime)]['titles']
        # print(records)
        # index = int(input('Enter Index of the Anime : '))
        # distances = sorted(list(enumerate(similar_matrix[index])),
        #                    reverse=True,key = lambda x: x[1])
        # for i in distances[1:6]:
        #    return recommended_anime

window=tk.Tk()
window.title('Anime Recommend System')
window.geometry('700x900')   
window.config(bg='white')

heading=tk.Label(text='Movie Recommend System',font=('Edwardian Script ITC',60),padx=30,pady=50)
heading.pack(pady=0,fill='x')

option=tk.Label(text=('How would u like to contact'),font=('Bahnschrift SemiLight Condensed',20))
option.pack(pady=20)

text_area=tk.Text(font=('Bahnschrift SemiLight Condensed',20),bg='white',width=50,height=5)
text_area.pack()

recommendation=tk.Button(text='Recommend',font=('Franklin Gothic Medium',20),bg='#DCA47C',fg='white',command=find_movie)
recommendation.pack(pady=50)

movie_labels = {
     'movie1':tk.Label(text='',font=('Bahnschrift',13),background='white'),
     'movie2':tk.Label(text='',font=('Bahnschrift',13),background='white'),
     'movie3':tk.Label(text='',font=('Bahnschrift',13),background='white'),
     'movie4':tk.Label(text='',font=('Bahnschrift',13),background='white'),
     'movie5':tk.Label(text='',font=('Bahnschrift',13),background='white'),
}
movie_labels['movie1'].pack()
movie_labels['movie2'].pack()
movie_labels['movie3'].pack()
movie_labels['movie4'].pack()
movie_labels['movie5'].pack()

window.mainloop()