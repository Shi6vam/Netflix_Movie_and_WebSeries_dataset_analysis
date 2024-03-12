import plotly
import plotly.express as px 
import plotly.figure_factory as ff
import plotly.graph_objects as go

import re

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import os
import warnings
warnings.filterwarnings('ignore')
os.listdir()

data = pd.read_csv("C:\\Users\\shiva\\Desktop\\Netflix_project\\netflix_data.csv.csv")
print(data.head())

print(data.shape)
print(data.columns)

print(data.info())

print(data.describe())

print(data.isna().sum())

print(data.isna().sum().sort_values(ascending= False))

# Get the number of null values in each column
null_values = data.isnull().sum()
total_values = data.shape[0]

# Get the percentage of null values in each column
null_percentage = null_values / total_values* 100

print(null_percentage)

# Percentage of total null values in dataset
print(data.isnull().sum().sort_values(ascending= False)/ data.shape[0] * 100)

print(data['director'].value_counts().head(10))


#MOVIE AND TV SHOW DISTRIBUTION..
print(data.type)
print(data['type'].value_counts())

plt.figure(figsize=(7,5))
sns.countplot(x='type',data=data,hue='type')
plt.title('NETFLIX AS DIFFERENT TYPES OF STEAMING',fontsize=20) #Note labelling the title
plt.xlabel(' Types',fontsize=10)  #Note labelling the x-label
plt.ylabel('No.of Data',fontsize=10)       #Note labelling the y-label
plt.show()
data['type'].value_counts()



#Checking gender imbalance...
values = data.type.value_counts(normalize=True).values
labels = data.type.value_counts(normalize=True).index
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.6, title='Movies Vs Tv shows')])
fig.show()
data['type'].value_counts(normalize=True)

# # Get the number of movies and TV shows
movies = data['type'].value_counts(normalize = True)['Movie']
tv_shows = data['type'].value_counts(normalize = True)['TV Show']

# # Create a bar graph
plt.bar(["Movies", "TV Shows"], [movies, tv_shows])
plt.title("Number of Movies and TV Shows")
plt.xlabel("Type", fontsize = 20 )
plt.ylabel("Count", fontsize = 20)
plt.show()


values = data.rating.value_counts().values
labels = data.rating.value_counts().index
fig = go.Figure(data=[go.Pie(labels=labels,hole= 0.5 ,values=values,title='rating')])
fig.show()
data['rating'].value_counts()


#TOP RAITING...
ax = sns.barplot(x=data.rating.value_counts(), y=data.rating.value_counts().index, orient="h", palette="viridis")
ax.set_title('Top rating by count')
ax.set_facecolor('black')
plt.show()


print(data['country'].value_counts())

print(data.country.value_counts().head(10))


print(data.release_year.value_counts().head(15))

#Analysis of Directors........
#Next we try to look into the director field which is compound field which needs to be exploded

#Finding the top 10 directors who produced more movies/tv shows.
#Finding the range of rating categories produced by those directors.

print(data['director'].replace(np.NaN,"Unknown", inplace=True))

plt.rcParams['font.size'] = 10
plt.figure(figsize=(12,8))
ax = sns.countplot(y ="director",data = data,order = data.director.value_counts().index[0:10])
ax.set_title('Top 10 director')
ax.set_xlabel('count')
ax.set_ylabel('director')
data.director.value_counts().head(10)
plt.show()

#Analysis on year and rating of movies and shows
#Comparison between time chart of movie/shows released year and added into netflix
#Finding the No. of movies/shows ratings by year added into netflix........

plt.rcParams['font.size'] = 10
plt.figure(figsize=(12,8))
ax = sns.countplot(y ="release_year",data = data,order = data.release_year.value_counts().index[0:15])
ax.set_title('Top 15 Movies and TV show release by Years')
ax.set_xlabel('Count')
ax.set_ylabel('release_year')
ax.set_facecolor('black')
sns.set_style('darkgrid')
plt.rcParams['figure.facecolor'] = '#ffffff'


data.release_year.value_counts().head(15)
plt.show()

###4.WHICH GENRES MOVIES WERE RELEASED MOSTLY IN NETFLIX PLATFORM?

# Change the font size
plt.rcParams['font.size'] = 10
# font size of the ticks
ax.tick_params(labelsize=12)
plt.figure(figsize=(12,8))
plt.grid(None)
top_15_listed_in = data['listed_in'].value_counts().sort_values(ascending=False).head(15)
ax = sns.countplot(y ="listed_in",data = data,order = top_15_listed_in.index,width = 0.8)
ax.set_facecolor('black')

ax.set_title('Top 15 Genre')
ax.set_xlabel('Count')
ax.set_ylabel('Listed In')
plt.show()
data.listed_in.value_counts().head(10)


##Handling the missing values........
print(data.isnull().sum().sort_values(ascending= False)/ data.shape[0] * 10)

print(data.isnull().sum().sort_values(ascending= False))


# dropping rows for small percentage of null 
print(data.dropna(subset = ["duration","rating"],axis = 0,inplace = True))

print(data.shape)
print(data.dropna(subset = ["date_added"],axis = 0,inplace = True))

# Filling and replacing missing values in country and director with Unknown ........
print(data['country'].fillna('Unknown', inplace=True))
print(data['director'].replace(np.NaN,"Unknown", inplace=True))


print(data.cast.value_counts().head(10))


print(data['cast'].replace(np.NaN,"no_cast", inplace=True))

print(data.isnull().sum().sort_values(ascending= False))

#Analyze Released and Added Movies and Tv Shows yearwise.....


print(data.head())

print(data.info())

data['date_added'] = pd.to_datetime(data['date_added'], format='mixed')

# Create a new column for the year the show or movie was added
data['date_added_year'] = data['date_added'].dt.year

fig, ax = plt.subplots(figsize=(15,10))
plt.grid(False)


# plt.figure(figsize=(12,8))
ax = sns.countplot(data=data, x='date_added_year', hue='type',palette='Set1')
ax.set_title('Count of Shows/Movies Added by Year')
ax.set_xlabel('Year of Addition')
ax.set_ylabel('Count')
ax.tick_params(rotation=45)

# Tighten the layout
plt.tight_layout()

# Show the plot
plt.show()


##released Movies and Tv shows yearwise.........

plt.figure(figsize=(12,8))
plt.grid(False)
ax = sns.countplot(data=data[data['release_year']>=2000], x='release_year', hue='type',palette='Set1')
ax.set_title('Count of Shows/Movies Added by Year')
ax.set_xlabel('Year of Release')
ax.set_ylabel('Count')
ax.tick_params(rotation=45)
ax.tick_params(labelsize=12)


plt.rcParams['font.size'] = 10

# Tighten the layout
plt.tight_layout()
plt.tight_layout()


# Show the plot
plt.show()

#7.WHICH IS HIGHEST NUMBER OF MOVIES AND TV SHOW GENRES IN NETFLIX PLATFORM?.......

# Create a list of the top 15 genres
top_15_genres = data['listed_in'].value_counts().sort_values(ascending=False)[:15].index

# Plot the top 15 genres
plt.figure(figsize=(12, 8))
ax = sns.countplot(data=data, x='listed_in', hue='type', palette='Set2', order=top_15_genres)
ax.set_title('Highest Genre of Shows/Movies')
ax.set_xlabel('Genre')
ax.set_ylabel('Number of Shows/Movies')
ax.tick_params(rotation=90)



# Tighten the layout
plt.tight_layout()

# Show the plot
plt.show()

#Analysis about trend of movies and tv shows in netflix......

trend_data = data.groupby(['date_added_year', 'type']).size().reset_index(name='count')


plt.figure(figsize=(10, 8))
sns.scatterplot(data=trend_data, x='date_added_year', y='count', hue='type', s=100, palette='Set1')
plt.title('Trend of Movies and TV Shows Year-wise')
plt.xlabel('Added Year')
plt.ylabel('Count')
plt.legend(title='Type', loc='upper left')
plt.show()
trend_data.value_counts()


#Downloading cleaned dataset.....
data.to_csv('cleaned_data_csv.csv')

# Create a new DataFrame with the cast information
cast_shows = data[data.cast != 'no_cast'].set_index('title').cast.str.split(', ',expand = True).stack().reset_index(level=1,drop=True)
plt.figure(figsize=(12,8))
plt.grid(False)
# Get the top 10 actors with the most movies
# filtered_cast_shows = cast_shows.value_counts().index[:10] 

# Create a count plot
ax = sns.countplot(y=cast_shows, order=cast_shows.value_counts().index[:10], palette='pastel')


# Set the title and labels

plt.title('Top 10 Actors with the Most Movies')
ax.set_ylabel('Actor')

# Show the plot
plt.show()
# top 10 actors with the most movies
cast_shows.value_counts()[:10]



# Create a DataFrame of movies
movies_df = data[data['type'] == 'Movie']

# Remove the " min" from the duration strings
movies_df['duration'] = movies_df['duration'].apply(lambda x: x.replace(" min", "") if 'min' in x else x)

# Convert the duration strings to integers
movies_df['duration'] = movies_df['duration'].astype('int64', errors='ignore')

# Print the summary statistics of the duration column
print(movies_df['duration'].describe())

# Find the shortest and longest movies
#shortest_movie = movies_df[movies_df['duration'] == movies_df['duration'].min()]
#print(shortest_movie)
#longest_movie = movies_df[movies_df['duration'] == movies_df['duration'].max()]
#print(longest_movie)

shortest_movie = movies_df[movies_df['duration'] == np.min(movies_df.duration)]
print(shortest_movie)

longest_movie = movies_df[movies_df.duration == np.max(movies_df.duration)]
print(longest_movie)
longest_movie.rating.value_counts()

print(shortest_movie[['title', 'cast']])

print(longest_movie[['title', 'cast']])

# we can see greater than 100 min movies 
longest_movies = movies_df[movies_df.duration >= 100]
print(longest_movies)

#Analysis of TV shows....

#make a dataframe for TV Shows only

tv_shows= data[data['type'] == 'TV Show']
tv_shows = tv_shows.copy(deep=True)
tv_shows.head(2)

#WHICH MOST NUMBER OF TV SHOW SEASON IN NETFLIX PLATFORM?
show_data = tv_shows['duration'].value_counts()

plt.figure(figsize=(10,6))
plt.grid(False)

show_data.plot(kind='bar')
plt.xlabel('Duration of TV shows')
plt.ylabel('Count')
plt.title('Count of TV show\'s duration')
tv_shows['duration'].value_counts()
plit.show()


plt.figure(figsize=(12, 8))
data['release_year'].value_counts()[:20].plot(kind="bar",color=['blue','green','yellow','orange']) #plotting the bar chart in matplotlib library with colors
plt.title('Highest Number Of Netflix Tv Show Released in Years',fontsize=25) #Note labelling the data
plt.xlabel('YEARS',fontsize=10)                         #Note labelling the x-label
plt.ylabel('Netflix Tv Show counts',fontsize=10)        #Note labelling the y-label
plt.grid(None)
plt.show()

tv_shows["listed_in"] = tv_shows["listed_in"].str.split(",")

tv_shows = tv_shows.explode('listed_in')

tv_shows.info()

tv_shows["listed_in"] = tv_shows["listed_in"].apply(lambda x:x.strip())

plt.figure(figsize=(10,6))
plt.grid(False)

sns.countplot(data=tv_shows,x="listed_in")
plt.xticks(rotation=90)
plt.title("TV Shows categories")

datam=data.loc[data['type']=='Movie']

datam.to_csv('netflix_movies.csv')    #output dataset for netflix movies


datam.head(2)     #read this data for movies in netflix platform


datam['duration']=datam['duration'].astype('int')   #Converts the given columns to "int64" type
datam.set_index('title',inplace=True)  #setting index as title for movies dataset

#WHICH MOVIES IN NETFLIX HAS MORE DURATION OF TIMES IN MINUTES?..
plt.figure(figsize=(8,6))
datam.duration.sort_values(ascending=False)[:10].plot(kind="barh",color=['red','black','blue']) #notes that BARH plot in matplotlib library with colors  
plt.title('NETFLIX MOVIES MORE TIME DURATION(MINUES)',fontsize=25)   #Note labelling the title
plt.xlabel('Minutes')  #Note labelling X-labels
plt.ylabel('Title')    #Note labelling Y-labels
plt.show()


#WHICH COUNTRY RELEASES MOST NUMBER MOVIES IN NETFLIX?.......
plt.figure(figsize=(6,6))
plt.grid(None)
datam.country.value_counts()[:14].plot(kind='pie',autopct='%.1f%%',pctdistance=0.9) #plotting the data with pie chart with country most relased.
plt.title('COUNTRY RELEASED MOST NUMBER MOVIES IN NETFLIX PLATFORM',fontsize=20) #note the labelling the title
plt.show()

datam.reset_index('title',inplace=True)  #reseting the index into previous index.
datam['listed_in'].drop_duplicates(inplace=True)    #drop the duplicates


#WHICH GENRES MOVIES WERE RELEASED MOSTLY IN NETFLIX PLATFORM?...
plt.figure(figsize=(8,6))
datam['listed_in'].value_counts()[:15].plot(kind='barh',color=['red','blue','green','yellow']) #plotting the barh chart in matplotlib library with colors
plt.title('MOST GENRES MOVIES IN NETFLIX PLATFORM',fontsize=30) #Note labelling the title
plt.xlabel('COUNTS')       #Note labelling the x-label
plt.ylabel('LISTED IN')   #Note labelling the y-label
plt.show()



# Create a list of the top 15 listed_in genres
# top_15_listed_in = data['listed_in'].value_counts()[:15].index

# Plot the top 15 listed_in genres
plt.figure(figsize=(10,6))
ax = data['listed_in'].value_counts()[:15].plot(kind='barh', color=['red', 'blue', 'green', 'yellow'])

# Set the title and labels
ax.set_title('Most Genres Movies in Netflix Platform', fontsize=30)
ax.set_xlabel('Counts')
ax.set_ylabel('Listed In')

ax.grid(False)

# Tighten the layout
plt.tight_layout()

# Show the plot
plt.show()

#DATA EXACTRATIONS FOR TV SHOWS..
datas=data.loc[data['type']=='TV Show']     #data exactration from Netflix_Shows dataset into TV SHOW types.
datas.to_csv('netflix_tvshow.csv')      #output dataset for netflix tv shows.


#WHICH MOST NUMBER OF TV SHOW SEASON IN NETFLIX PLATFORM?..
plt.figure(figsize=(12, 8))

explode=[0,0,0,0,0,0,0,0.2,0.4,1.1]
datas.duration.value_counts()[:10].plot(kind='pie',hatch='title',explode=explode,autopct='%.1f%%',pctdistance=0.8) #plotting the pie chart in matplotlib with explode datas 
plt.title('Most number Tv Show Season in Netflix',fontsize=30)   #Note labelling the title
plt.show()


#WHICH HIS HIGHEST NUMBER OF NETFLIX TV SHOW RELEASED IN YEARS?......
plt.figure(figsize=(12, 8))
datas['release_year'].value_counts()[:20].plot(kind="bar",color=['blue','green','yellow','orange']) #plotting the bar chart in matplotlib library with colors
plt.title('Highest Number Of Netflix Tv Show Released in Years',fontsize=25) #Note labelling the data
plt.xlabel('YEARS',fontsize=10)                         #Note labelling the x-label
plt.ylabel('Netflix Tv Show counts',fontsize=10)        #Note labelling the y-label
plt.show()


# Create a bar plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(datas['release_year'].value_counts()[:20].index, datas['release_year'].value_counts()[:20], color=['blue', 'green', 'yellow', 'orange'])

# Set the title and labels
ax.set_title('Highest Number Of Netflix Tv Show Released in Years', fontsize=25)
ax.set_xlabel('YEARS', fontsize=10)
ax.set_ylabel('Netflix Tv Show counts', fontsize=10)

# Show the plot
plt.show()


#WHICH IS HIGHEST NUMBER OF TV SHOW GENRES IN NETFLIX PLATFORM?...
plt.figure(figsize=(15,12))
datas['listed_in'].value_counts()[:15].plot(kind='barh',color=['red','black','blue']) #plotting the barh chart in matplotlib with colors
plt.title('Highest Number Of Tv Show Genre in Netflix',fontsize=55)  #Note labelling the title
plt.xlabel('No.Of Tv Show',fontsize=15)      #Note labelling the x-label
plt.ylabel('Listed in',fontsize=15)          #Note labelling the y-label
plt.show()


