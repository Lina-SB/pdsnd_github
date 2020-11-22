import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

day_of_week = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():

    print('Hello!  Are you intersted  in  bikeshare!!  Let\'s dig out  some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('Which city do you want to start covering? Chicago, New York city or Washington? \n> ').lower()
       if city not in CITY_DATA:
            print("\please...try agin!!\n")
            continue

       else:
            print('\n Here we go>>\n')
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
               try:
                 month = input("Which month do you want to know about!").lower()
                 if month in  months:
                         break
                 else:
                    print('\n Try agin please...\just say \'all\' to apply no month filter\n')
               except ValueError:
                    print('"Oops!  \n Don\'t use numbers...  \just say \'all\' to apply no month filter\n')
               else:
                    break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        try:
          day = input("Which day do you want to know about!").lower()
          if day in day_of_week:
               break
          else:
              print('\n Try agin please...\just say \'all\' to apply no day filter\n')

        except ValueError:
             print('"Oops!  \n Don\'t use numbers...  \just say \'all\' to apply no day filter\n')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

  # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

     # filter by month if applicable
    if month != 'all':

        # use the index of the months list to get the corresponding int
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
        # filter by month to create the new dataframe
       df = df[df['month']==month]

      # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print(common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print(common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print(total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print(" no gender information here.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(recent)
        common_birth = df['Birth Year'].mode()[0]
        print(common_birth)
    else:
     print(" no birth year information here.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Display raw data on user request

def display_raw_data(df):
    """ display raw data for user request"""
    raw_data = 0
    while True:
         user_request = input("Do you want to see the raw data? Yes or No\n").lower()
         if user_request not in ['yes', 'no']:
            print(" Please type Yes or No.").lower()
         elif user_request == 'yes':
              raw_data += 5
              print(df.iloc[raw_data : raw_data + 5])
         elif user_request== 'no':
              return
              print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
