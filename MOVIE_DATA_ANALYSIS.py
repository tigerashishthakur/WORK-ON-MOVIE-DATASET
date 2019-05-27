##  here first we are importing required libraries ,they are, pandas ,matplotlib ,sys.


import pandas as pd
import sys
import matplotlib.pyplot as plt

## here i append my system with this path to search

## also pd.read_csv is reading the movie dataset file which is stored on my system.if u want to work u can download movie_|
##   metadata.csv and add the path to file like i did


sys.path.append("D:/kaushal/Desktop/movie_metadata.csv")
df=pd.read_csv("D:/kaushal/Desktop/movie_metadata.csv/movie_metadata.csv")
print(df)

## here i am creating a list of all the columns present in movie dataset
l=df.columns
print(l)


## here i am creating a dictionary of movie and its imdb_score
score=list(df.get("imdb_score"))
print(score)
print(len(score))

##  code to check the type of score
print(type(score))

## code to check the type of dataframe
print(type(df))
data=df.values
print(data.shape)
print(type(data))



## try to gain some insights
## plot x-axis(len(movie)) and y-axis(frequency)
titles=df.get("movie_title")
print(titles)
freq_title={}

## calculating the no of times a movie_title having same title length is repeated,i.e., its frequency
for t in titles:
    length=len(t)
    try:
        freq_title[length]+=1;
    except:
        freq_title[length]=1;
print(freq_title)
x=list(freq_title.keys())
y=list(freq_title.values())

## plotting a scatter graph where x-axis is "length of movie title"
## and y-axis shows "frequency of appearence of movie title with same title length"
plt.scatter(x,y,marker="^",color="red",label="stock price")
plt.legend()
plt.show()


## plotting a plot where x-axis is "length of movie title"
## and y-axis shows "frequency of appearence of movie title with same title length"
plt.plot(x,y)
plt.xlabel("length of movietitle")
plt.ylabel("no.of movies")
plt.show()

## plotting a bar graph where x-axis is "length of movie title"
## and y-axis shows "frequency of appearence of movie title with same title length"
plt.bar(x,y,0.25,color="orange")
plt.show()

## plotting a scatter graph where label is "length of movie title"
## and values shows "frequency of appearence of movie title with same title length"
plt.pie(y,labels=x,radius=1,shadow="True")
plt.show()
