#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:34:03 2020

@author: Q
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Added comments for refactoring

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    global city
    city =str(input("Please enter a City name:")).lower()
    while city not in CITY_DATA:
            print('Are you sure you have enter the right city name? Please enter Washington,  New York City or Chicago ')
            city =str(input("Please enter a City name again:")).lower()
    
            print('You have entered: ', city)
    

    # get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    month =str(input("Please enter a Month or ALL if you want to select all months:")).lower()
    while month not in months:
            print('Are you sure you have enter the right Month?')
            month =str(input("Please enter Month again:")).lower()
            print('You have entered: ', month)
    
       

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday','thursday','friday', 'sunday']  
    day =str(input("Please enter a weekdat or ALL if you want to select all weekdays:")).lower()
    while day not in days:
            print('Are you sure you have enter the right weekday?')
            day =str(input("Please enter a weekday again:")).lower()
            print('You have entered: ', day)

    print('-'*40)
    return city, month, day



#Function: load data

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    
        return df 


"Function:  Time statistics "



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common month:', common_month)
    
   
    # display the most common day of week
    
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week :', common_day)
 
    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_station_start = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_station_start )
   

    # display most commonly used end station
    common_station_end = df['End Station'].mode()[0]
    print('Most commonly used End station:', common_station_end )
    

    # display most frequent combination of start station and end station trip
    df['StartEndSations'] = df['End Station'] +" And "+ df['Start Station']
    common_stations = df['StartEndSations'].mode()[0]
    print('Most commonly used  Start and End station:', common_stations )
  


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['time_delta']= df['End Time'] - df['Start Time']


    # display total travel time
    
    print ('The the total trip duration is ' + str(df['time_delta'].sum()))
    
    # display mean travel time

    print ('The average average trip duration is ' + str(df['time_delta'].mean()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#Gender and Birth date are missing from Washington Data set, we need to handle this issue
def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if city != 'washington':
          # Display counts of user types
         user_types = df['User Type'].value_counts()
         print(user_types)

         # Display counts of gender
         gender = df['Gender'].value_counts()
         print(gender)


         # Display earliest, most recent, and most common year of birth
         min_bday = df['Birth Year'].min()
         max_bday = df['Birth Year'].max()
         common_bday = df['Birth Year'].mode()[0] 

         print('The most common Birth year is: '+ str(common_bday).strip(".0"))
         print('The most recent Birth year is: '+ str(max_bday).strip(".0"))
         print('The earliest Birth year is: '+ str(min_bday).strip(".0"))
    else: 
         print("Gender and Birth date are missing from Washington Data set")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
