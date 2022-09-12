# the initial draft

from datetime import datetime, timedelta
import os
import pickle
import random
import sys


def get_birthdays_per_week(users: list):
    """
    The function displays users with birthdays one week ahead of the current day.
    users =[{'name':'name1', 'birthday':datetime1},{'name':'name2', 'birthday':datetime2}, 
    ..., {'name':'nameN', 'birthday':datetimeN}]

    incoming: users - list of dictionaries with keys: "name" and "birthday"
    return: None
    """
    happy_users = ['Monday: ', 'Tuesday: ',
                   'Wednesday: ', 'Thursday: ', 'Friday: ']
    current_datetime = datetime.now().date()

    # current_datetime.weekday()  # 0,1,2...6
    start_date = current_datetime + \
        timedelta(days=int(5-current_datetime.weekday())
                  )  # from next(current) Saturday
    finish_date = start_date + timedelta(days=6)  # including both
    for user in users:
        hot_date = user.get("birthday")
        delta_next_year = 0
        if hot_date.month == (finish_date.year-start_date.year):
            delta_next_year = 1
        hot_date = datetime(year=current_datetime.year + delta_next_year,
                            month=hot_date.month, day=hot_date.day)
        if start_date <= hot_date.date() <= finish_date:
            # if hot_date.weekday() == 5 or hot_date.weekday() == 6:
            if hot_date.weekday() == 0:
                happy_users.insert(0, happy_users.pop(0) +
                                   user.get("name")+", ")
            if hot_date.weekday() == 1:
                happy_users.insert(1, happy_users.pop(1) +
                                   user.get("name")+", ")
            if hot_date.weekday() == 2:
                happy_users.insert(2, happy_users.pop(2) +
                                   user.get("name")+", ")
            if hot_date.weekday() == 3:
                happy_users.insert(3, happy_users.pop(3) +
                                   user.get("name")+", ")
            if hot_date.weekday() == 4:
                happy_users.insert(4, happy_users.pop(4) +
                                   user.get("name")+", ")
            if hot_date.weekday() == 5:
                happy_users.insert(0, happy_users.pop(0) +
                                   user.get("name")+"(Saturday), ")
            if hot_date.weekday() == 6:
                happy_users.insert(0, happy_users.pop(0) +
                                   user.get("name")+"(Sunday), ")
    for i in happy_users:
        if i[-2] != ":":
            print(i+'\n')
    pass

    # print(happy_users)


def load_users_list():
    """
    for load users list from file... "users.data" (to enter a parameter?)

    incoming: users - list of dictionaries with keys: "name" and "birthday"
    return: users - list from file...
    """
    if os.path.isfile(os.path.join(os.path.abspath(os.path.dirname(__file__)), "users.data")):
        users = []
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "users.data"), 'rb') as fh:
            try:
                users = pickle.load(fh)
            except:  # ? !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! test and...
                print('The File is corrupted, my apologies')
                # create_users_data()
        if users == []:  # or len(users) < 1
            print('There no data in File!')
            # create_users_data()
    else:
        print('Sorry, but there is no File next to the py-file')
        users = []
        # create_users_data()

    return users


def save_users_list(users: list):
    """
    for save users list in file... "users.data" (to enter a parameter?)

    incoming: users - list of dictionaries with keys: "name" and "birthday"
    return: None
    """
    if users != []:
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "users.data"), 'wb') as fh:
            try:
                pickle.dump(users, fh)
            except:  # ! concretize? too many...
                print(
                    'Something went wrong while trying to write the file, you can try again')
    else:
        print("No data to save!")


def manual_data_entry(users: list):
    """
    for manual data entry: users

    incoming: users - list of dictionaries with keys: "name" and "birthday"
    return: users - list of dictionaries with keys: "name" and "birthday"
    """
    if users == []:  # or len(users) < 1 ??? remove this if...!!!!!!!!!!
        # there is no verification of the entered data yet...!!!!!!!!!!!!!!!!!!!!!!!!
        print('Be very careful when entering the data! ')
        answ_finish_input = ''
        while answ_finish_input != 'y' or answ_finish_input != 'Y':
            user_name = input('Name of person: ')  # user name
            birthday_data = input('Enter Birthday (YYYY-MM-DD): ')
            birthday_data = birthday_data.split('-')
            birthday_data = datetime(
                year=int(birthday_data[0]), month=int(birthday_data[1]), day=int(birthday_data[2]))
            users.append({'name': user_name, 'birthday': birthday_data})
            answ_finish_input = input(
                'Finish entering data? y=Yes, or No?: ')
            if answ_finish_input == 'y' or answ_finish_input == 'Y':
                break
    # save_users_list(users)

    return users


def create_users_data(users=[]):
    """
    Create a test list of users and fill it yourself.
    The function allows you to create a list of users with
    birthdays OR/AND save this data in the file "users.data"
    next to the program, OR load this data from the file
    into the variable "users" - list of dictionaries with keys: "name" and "birthday"

    incoming: users - list of dictionaries with keys: "name" and "birthday"
    return: users - list of dictionaries with keys: "name" and "birthday"
    """
    print('Now need create users list or load from file...')
    answ = '0'
    while True:
        answ = input(
            '1 - Try load from file "users.data"\n2 - Manual data entry\n3 - exit\n')
        try:
            answ = int(answ)
            if answ == 1 or answ == 2 or answ == 3:
                break
        except:  # ! concretize? too many...
            print('Invalid input, please try again ')
    if answ == 3:
        exit()
    if answ == 2:
        users = manual_data_entry(users)
    if answ == 1:
        users = load_users_list()

    return users


def random_date(start_month=1, end_month=12, start_day=1, end_day=31, max_year=datetime.now().year-1):
    """
    For generate random date in datetime object.

    incoming: start parameters - limits of generator
    return: datetime object with random date
    """
    if max_year < 1922:
        max_year = datetime.now().year - 1
    Year = random.randint(1922, max_year)   # 2022, 2072
    month = random.randint(start_month, end_month)  # 1, 12
    day = random.randint(start_day, end_day)  # 1, 31  # 30/29/28
    while True:
        try:
            datetime(year=Year, month=month, day=day)
            break
        except ValueError:
            day = random.randint(start_day, end_day)

    return datetime(year=Year, month=month, day=day)


def generator_virtual_persons():
    """
    For create a test list of users from 144 to 288 (only for test)

    return: users - list of dictionaries with keys: "name" and "birthday"
    """
    users = []
    persons_limit = (random.randint(144, 288) // 12) * 12
    for num in range(persons_limit):
        current_month = 1 + num // (persons_limit // 12)
        start_day = 1 + 7 * (num % 4)
        end_day = start_day + 7  # 7? ! 30+31? -> 8 ) 32 )))
        users.append(
            {'name': 'Name_' + str(num), 'birthday': random_date(current_month, current_month, start_day, end_day)})

    return users


def main():
    """
    Basic function to display user birthdays per week.
    The function displays users with birthdays one week ahead of the current day.
    1 - automatically form a list of users with random date and numbered names
    0 - manually create a list of users or load from file
    """
    if len(sys.argv) < 2:
        print('No startup parameter entered, must be 1 or 0')
        users = load_users_list()  # time to test!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        for i in users:
            print(i)
        get_birthdays_per_week(users)
        exit()
    if sys.argv[1] == "1":
        users = generator_virtual_persons()
        save_users_list(users)
    elif sys.argv[1] == "0":
        users = create_users_data()
        save_users_list(users)
    else:
        input("Incorrect input start parameters! ")
        exit()

    get_birthdays_per_week(users)


if __name__ == "__main__":
    exit(main())
