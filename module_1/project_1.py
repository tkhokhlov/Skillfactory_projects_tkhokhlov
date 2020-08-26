#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


# In[2]:
data = pd.read_csv('movie_bd_v5.csv')
data.sample(15)


# In[3]:
data.describe()


# In[4]:
data.info()


# # Предобработка
# In[5]:
# Cоздадим словарь для ответов
answers = {}


# In[6]:
# Cозданим колонку с информацией о прибыле (убытках) фильмов
data['profit'] = data['revenue'] - data['budget']


# In[7]:
# Преобразуем колонку "release_date" в формат "datetime64", чтобы работать с ней, как датой
data['release_date'] = pd.to_datetime(data['release_date'])

# Создадим колонку "release_month" в которую сохраним значение месяца выхода фильма
data['release_month'] = data['release_date'].dt.month
data.info()


# In[8]:
# Создадим колонку "title_length" в которую сохраним количество символов в названии фильма
data['title_length'] = data['original_title'].apply(len)
data.info()


# In[9]:
# Создадим колонку "overview_word_amount" в которую сохраним количество слов в фильме
data['overview_word_amount'] = data['overview'].apply(lambda word_amount: len(str(word_amount).split(' ')))
data.info()


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[10]:
# в словарь вставляем номер вопроса и ваш ответ на него
answers['1'] = 'Pirates of the Caribbean: On Stranger Tides (tt1298650)' #+


# In[11]:
# тут пишем ваш код для решения данного вопроса:
data[data['budget'] == data['budget'].max()][['imdb_id', 'original_title', 'budget']]


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[12]:
# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = 'Gods and Generals (tt0279111)' #+


# In[13]:


data[data['runtime'] == data['runtime'].max()][['imdb_id', 'original_title', 'runtime']]


# # 3. Какой из фильмов самый короткий (в минутах)?

# In[14]:
data[data['runtime'] == data['runtime'].min()][['imdb_id', 'original_title', 'runtime']]


# In[15]:
answers['3'] = 'Winnie the Pooh (tt1449283)' #+


# # 4. Какова средняя длительность фильмов?

# In[16]:
int(round(data['runtime'].mean(), 0))


# In[17]:
answers['4'] = '110' #+


# # 5. Каково медианное значение длительности фильмов? 

# In[18]:
int(round(data['runtime'].median(), 0))


# In[19]:
answers['5'] = '107' #+


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[20]:
data[data['profit'] == data['profit'].max()][['imdb_id', 'original_title', 'profit']]


# In[21]:
answers['6'] = 'Avatar (tt0499549)' #+


# # 7. Какой фильм самый убыточный? 

# In[22]:
data[data['profit'] == data['profit'].min()][['imdb_id', 'original_title', 'profit']]


# In[23]:
answers['7'] = 'The Lone Ranger (tt1210819)' #+


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[24]:
len(data[data['revenue'] > data['budget']])


# In[25]:
answers['8'] = '1478' #+


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[26]:
# Первый варинат решения задачи (с помощью доп. переменной)
max_revenue_2008 = data[data['release_year'] == 2008]['revenue'].max()
data[(data['release_year'] == 2008) & (data['revenue'] == max_revenue_2008)][['imdb_id', 'original_title', 'revenue']]


# In[27]:
# Второй варинат решения задачи (с помощью сортировки)
data[data['release_year'] == 2008][['imdb_id', 'original_title', 'revenue']].sort_values(by = ['revenue'], ascending=False).head(1)


# In[28]:
answers['9'] = 'The Dark Knight (tt0468569)' #+


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[29]:
data[(data['release_year'] >= 2012) & 
     (data['release_year'] <= 2014)][['imdb_id', 'original_title', 'profit']].sort_values(by = ['profit']).head(1)


# In[30]:
answers['10'] = 'The Lone Ranger (tt1210819)' #+


# # 11. Какого жанра фильмов больше всего?

# In[31]:
# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале

# Вариант 1, с помощью цикла
genres_list = []

for item in data['genres'].tolist():
    genres_in_row = item.split('|')
    
    for genre in genres_in_row:
        genres_list.append(genre)

genres_series = pd.Series(genres_list)
genres_series.value_counts().head(1)


# ВАРИАНТ 2

# In[32]:
# Вариант 2, с помощью метода ...str.cat()
genres_series = pd.Series(data['genres'].str.cat(sep='|').split('|'))
genres_series.value_counts().sort_values(ascending = False).head(1)


# In[33]:
answers['11'] = 'Drama' #+


# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[34]:
pd.Series(data[data['profit'] > 0]['genres'].str.cat(sep='|').split('|')).value_counts().sort_values(ascending = False).head(1)


# In[35]:
answers['12'] = 'Drama' #+


# # 13. У какого режиссера самые большие суммарные кассовые сборы?

# In[36]:
# Создаем серию, индексами которой будут все режиссеры (по отдельности),
# а в качестве значений - информация о том, сколько раз каждый из них встречается в датасэте

directors = pd.Series(data['director'].str.cat(sep='|').split('|')).value_counts()

# Теперь заменим информацию в серии "directors" на сумму кассовых сборов всех фильмов, где встречается данный режиссер
for director in directors.index:
    directors[director] = data[data['director'].str.contains(director)]['profit'].sum()

directors.sort_values(ascending = False).head(1)


# In[37]:
answers['13'] = 'Peter Jackson' #+


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[38]:
pd.Series(data[data['genres'].str.contains('Action')]['director']
          .str.cat(sep='|').split('|')).value_counts().sort_values(ascending = False).head(1)


# In[39]:
answers['14'] = 'Robert Rodriguez' #+


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[40]:
# Создаем серию, индексами которой будут все актеры (по отдельности),
# а в качестве значений - информация о том, сколько раз каждый из них встречается в датасэте

actors = pd.Series(data['cast'].str.cat(sep='|').split('|')).value_counts()

# Теперь заменим информацию в серии "actors" на сумму кассовых сборов всех фильмов, вышедших в 2012 году
for actor in actors.index:
    actors[actor] = data[(data['release_year'] == 2012) & (data['cast'].str.contains(actor))]['revenue'].sum()

actors.sort_values(ascending = False).head(1)


# In[41]:
answers['15'] = 'Chris Hemsworth' #+


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[42]:
# В качестве "высокобюджетных" фильмов возьмем те фильмы, бюджет которых выше среднего по датасэту

pd.Series(data[data['budget'] > data['budget'].mean()]
          ['cast'].str.cat(sep='|').split('|')).value_counts().sort_values(ascending = False).head(1)


# In[43]:
answers['16'] = 'Matt Damon' #+


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[44]:
pd.Series(data[data['cast'].str.contains('Nicolas Cage')]
          ['genres'].str.cat(sep='|').split('|')).value_counts().sort_values(ascending = False).head(1)


# In[45]:
answers['17'] = 'Action' #+


# # 18. Самый убыточный фильм от Paramount Pictures

# In[46]:
data[data['production_companies'].str.contains('Paramount Pictures')][['imdb_id', 'original_title', 'profit']].sort_values(by = ['profit']).head(1)


# In[47]:
answers['18'] = 'K-19: The Widowmaker (tt0267626)' #+


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[48]:
data.groupby('release_year')['revenue'].sum().sort_values(ascending = False).head(1)


# In[49]:
answers['19'] = '2015' #+


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[50]:
data[data['production_companies'].str.contains('Warner Bros')].groupby('release_year')['profit'].sum().sort_values(ascending = False).head(1)


# In[51]:
answers['20'] = '2014' #+


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[52]:
data.groupby('release_month')['imdb_id'].count().sort_values(ascending = False).head(1)


# In[53]:
answers['21'] = 'Сентябрь' #+


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[54]:
len(data[(data['release_month'] >= 6) & (data['release_month'] <= 8)])


# In[55]:
answers['22'] = '450' #+


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[56]:
pd.Series(data[(data['release_month'] == 12) | (data['release_month'] <= 2)]
          ['director'].str.cat(sep='|').split('|')).value_counts().head(1)


# In[57]:
answers['23'] = 'Peter Jackson' #+


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[69]:
# Создаем серию, индексами которой будут все киностудии (по отдельности),
# а в качестве значений - информация о том, сколько раз каждая из них встречается в датасэте
production_companies = pd.Series(data['production_companies'].str.cat(sep='|').split('|')).value_counts()

# Теперь заменим информацию в серии "production_companies" на среднюю длину названия фильма
for production_company in production_companies.index:
    production_companies[production_company] = data[data['production_companies'].str.contains(production_company)]['title_length'].mean()
    
production_companies.sort_values(ascending = False).head(1)


# In[59]:
answers['24'] = 'Four By Two Productions' #+


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[60]:
# Используем серию "production_companies" из прошлого вопроса
# и заменим в ней информацию на среднее количество слов в описании фильма

for production_company in production_companies.index:
    production_companies[production_company] = data[data['production_companies'].str.contains(production_company)]['overview_word_amount'].mean()
    
production_companies.sort_values(ascending = False).head(1)


# In[61]:
answers['25'] = 'Midnight Picture Show' #+


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[62]:
# Для определения 1% лучших по рейтингу фильмов отфильтруем датасет с помощью метода ".quantile" с параметром ".99"
data[data['vote_average'] > data['vote_average'].quantile(.99)][['imdb_id', 'original_title', 'vote_average']].sort_values(by = 'vote_average', ascending = False)


# In[63]:
answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave' #+


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?

# In[64]:
import itertools as it

actors = Counter()
for actors_in_move in data.cast.str.split('|'):
    actors += Counter(it.combinations(actors_in_move, 2))

for couple_actors, count in actors.most_common():
    print(couple_actors, count)


# In[65]:
answers['27'] = 'Daniel Radcliffe & Rupert Grint' #+


# # Submission

# In[70]:
# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[67]:
# и убедиться что ни чего не пропустил)
len(answers)

