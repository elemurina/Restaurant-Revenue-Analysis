#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# Загрузка данных
df = pd.read_csv('restaurant_data.csv')

# Просмотр первых нескольких строк данных
print(df.head())



# In[5]:


# Общее количество ресторанов
total_restaurants = df['Name'].nunique()
print(f"Общее количество ресторанов: {total_restaurants}")


# In[6]:


# Количество ресторанов в каждом районе
restaurants_by_location = df['Location'].value_counts()
print("Количество ресторанов в каждом районе:")
print(restaurants_by_location)


# In[7]:


# Количество каждого типа ресторанов в каждом районе
restaurants_by_location_and_cuisine = df.groupby(['Location', 'Cuisine']).size().unstack(fill_value=0)
print("Количество каждого типа ресторанов в каждом районе:")
print(restaurants_by_location_and_cuisine)


# In[8]:


# Средняя стоимость блюда по типам ресторанов
average_meal_price_by_cuisine = df.groupby('Cuisine')['Average Meal Price'].mean()
print("Средняя стоимость блюда по типам ресторанов:")
print(average_meal_price_by_cuisine)


# In[9]:


# Минимальные и максимальные цены на блюда в каждом типе ресторанов
meal_price_range_by_cuisine = df.groupby('Cuisine')['Average Meal Price'].agg(['min', 'max'])
print("Минимальные и максимальные цены на блюда в каждом типе ресторанов:")
print(meal_price_range_by_cuisine)


# In[10]:


# Средняя и общая вместимость ресторанов по районам
seating_capacity_by_location = df.groupby('Location')['Seating Capacity'].agg(['mean', 'sum'])
print("Средняя и общая вместимость ресторанов по районам:")
print(seating_capacity_by_location)


# In[11]:


# Средняя и общая вместимость по типам ресторанов
seating_capacity_by_cuisine = df.groupby('Cuisine')['Seating Capacity'].agg(['mean', 'sum'])
print("Средняя и общая вместимость по типам ресторанов:")
print(seating_capacity_by_cuisine)


# In[12]:


# Средний рейтинг ресторанов по районам
average_rating_by_location = df.groupby('Location')['Rating'].mean()
print("Средний рейтинг ресторанов по районам:")
print(average_rating_by_location)


# In[13]:


# Средний рейтинг по типам ресторанов
average_rating_by_cuisine = df.groupby('Cuisine')['Rating'].mean()
print("Средний рейтинг по типам ресторанов:")
print(average_rating_by_cuisine)


# In[14]:


# Распределение рейтингов (гистограмма)
import matplotlib.pyplot as plt
df['Rating'].hist(bins=10)
plt.title('Распределение рейтингов')
plt.xlabel('Рейтинг')
plt.ylabel('Количество ресторанов')
plt.show()


# In[15]:


# Среднее количество подписчиков в социальных сетях по районам
average_followers_by_location = df.groupby('Location')['Social Media Followers'].mean()
print("Среднее количество подписчиков в социальных сетях по районам:")
print(average_followers_by_location)


# In[16]:


# Среднее количество подписчиков по типам ресторанов
average_followers_by_cuisine = df.groupby('Cuisine')['Social Media Followers'].mean()
print("Среднее количество подписчиков по типам ресторанов:")
print(average_followers_by_cuisine)


# In[17]:


# Средний опыт шеф-поваров (в годах) по районам
average_experience_by_location = df.groupby('Location')['Chef Experience Years'].mean()
print("Средний опыт шеф-поваров (в годах) по районам:")
print(average_experience_by_location)


# In[18]:


# Средний опыт шеф-поваров по типам ресторанов
average_experience_by_cuisine = df.groupby('Cuisine')['Chef Experience Years'].mean()
print("Средний опыт шеф-поваров по типам ресторанов:")
print(average_experience_by_cuisine)


# In[19]:


# Среднее количество отзывов по районам
average_reviews_by_location = df.groupby('Location')['Number of Reviews'].mean()
print("Среднее количество отзывов по районам:")
print(average_reviews_by_location)


# In[20]:


# Среднее количество отзывов по типам ресторанов
average_reviews_by_cuisine = df.groupby('Cuisine')['Number of Reviews'].mean()
print("Среднее количество отзывов по типам ресторанов:")
print(average_reviews_by_cuisine)


# In[21]:


# Средняя оценка атмосферы по районам
average_ambience_score_by_location = df.groupby('Location')['Ambience Score'].mean()
print("Средняя оценка атмосферы по районам:")
print(average_ambience_score_by_location)


# In[22]:


# Средняя оценка атмосферы по типам ресторанов
average_ambience_score_by_cuisine = df.groupby('Cuisine')['Ambience Score'].mean()
print("Средняя оценка атмосферы по типам ресторанов:")
print(average_ambience_score_by_cuisine)


# In[23]:


# Средняя оценка качества обслуживания по районам
average_service_quality_score_by_location = df.groupby('Location')['Service Quality Score'].mean()
print("Средняя оценка качества обслуживания по районам:")
print(average_service_quality_score_by_location)


# In[24]:


# Средняя оценка качества обслуживания по типам ресторанов
average_service_quality_score_by_cuisine = df.groupby('Cuisine')['Service Quality Score'].mean()
print("Средняя оценка качества обслуживания по типам ресторанов:")
print(average_service_quality_score_by_cuisine)


# In[25]:


# Количество ресторанов с парковкой и без парковки по районам
parking_availability_by_location = df.groupby(['Location', 'Parking Availability']).size().unstack(fill_value=0)
print("Количество ресторанов с парковкой и без парковки по районам:")
print(parking_availability_by_location)


# In[26]:


# Количество ресторанов с парковкой и без парковки по типам ресторанов
parking_availability_by_cuisine = df.groupby(['Cuisine', 'Parking Availability']).size().unstack(fill_value=0)
print("Количество ресторанов с парковкой и без парковки по типам ресторанов:")
print(parking_availability_by_cuisine)


# In[27]:


# Среднее количество бронирований на выходные по районам
average_weekend_reservations_by_location = df.groupby('Location')['Weekend Reservations'].mean()
print("Среднее количество бронирований на выходные по районам:")
print(average_weekend_reservations_by_location)


# In[28]:


# Среднее количество бронирований на выходные по типам ресторанов
average_weekend_reservations_by_cuisine = df.groupby('Cuisine')['Weekend Reservations'].mean()
print("Среднее количество бронирований на выходные по типам ресторанов:")
print(average_weekend_reservations_by_cuisine)


# In[29]:


# Среднее количество бронирований в будние дни по районам
average_weekday_reservations_by_location = df.groupby('Location')['Weekday Reservations'].mean()
print("Среднее количество бронирований в будние дни по районам:")
print(average_weekday_reservations_by_location)


# In[30]:


# Среднее количество бронирований в будние дни по типам ресторанов
average_weekday_reservations_by_cuisine = df.groupby('Cuisine')['Weekday Reservations'].mean()
print("Среднее количество бронирований в будние дни по типам ресторанов:")
print(average_weekday_reservations_by_cuisine)


# In[ ]:




