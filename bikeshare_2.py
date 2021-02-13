import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n').lower().strip()
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print('City input incorrect, please choose between three cities above\n')
            

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input('Please enter one of the 1st six months\' name if you wnat to filter by month. Else type all.\n').lower().strip()
        if month in ('all', 'january', 'february', 'april', 'may', 'june'):
            break
        else:
            print('Month input incorrect, please choose one of the 1st six months. Else type all.\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('Please type day\'s name if you want to filter by day. Else type all.\n').lower().strip()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'Saturday', 'sunday'):
            break
        else:
            print('Day input incorrect, please choose retype the day\'s name or type all.\n')
    
    
    print('-'*40)
    return city, month, day


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
    #To load read data from csv file(pd.read_csv)
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month: {}'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('Most common day of week: {}'.format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour     
    print('Most common start hour of day : {}'.format(df['hour'].mode()[0]))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station: {}\n'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('Most commonly used end station: {}\n'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('Most frequent combination of start and end station trip: {}'.format((df['Start Station']+' and '+df['End Station']).mode()[0]))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time = {}\n'.format(df['Trip Duration'].sum()))


    # display mean travel time
    print('Mean travel time = {}\n'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def display_raw_data(df): #Displaying rows from raw data upon user request, until typing 'no'
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`
    """    

    data = 0

    while True:
        if input('Would you like to see 5 lines of raw data? Enter yes or no: \n').lower() == 'yes':
            print(df[data : data+5])
            data += 5
        else:
            break
      
    
def user_stats(df, city):   #Adding arg'city' to handle the difference in  washington's data 
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    

    # Display counts of user types
    print('User types\' counts : \n{}\n'.format(df['User Type'].value_counts()))

    
    if city != 'washington':   #In case user choose washington as a city will not show output data
        # Display counts of gender
        print('Genders\'s counts : \n{}\n'.format(df['Gender'].value_counts()))

        # Display earliest, most recent, and most common year of birth
        print('The Earliest year of birth: {},\nMost recent year of birth: {},\nMost common year of birth: {}\n'.format(int(df['Birth Year'].min()) , int(df['Birth Year'].max()) , int(df['Birth Year'].mode()[0])))
    else:
        print('No data available regarding gender and year of birth for washington city')

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city) #Adding 'city' as argument 
        display_raw_data(df) #Displaying rows from raw data upon user 

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('\nThank you, \nSee you later\n\nCode made by:\nNaif Moh \nYou can find me in Github:\ngithub.com/aboezn')
            break


if __name__ == "__main__":
	main()
