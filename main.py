from pymodm import connect
import models
import datetime

def add_heart_rate(email, heart_rate, time):
    user = models.User.objects.raw({"_id": "suyash@suyashkumar.com"}).first() # Get the first user where _id=suyash@suyashkumar.com
    user.heart_rate.append(heart_rate) # Append the heart_rate to the user's list of heart rates
    user.heart_rate_times.append(time) # append the current time to the user's list of heart rate times
    user.save() # save the user to the database

def create_user():
    u = models.User("suyash@suyashkumar.com", 24, [], []) # create a new User instance
    u.heart_rate.append(60) # add initial heart rate
    u.heart_rate_times.append(datetime.datetime.now()) # add initial heart rate time
    u.save() # save the user to the database

def print_user(email):
    user = models.User.objects.raw({"_id": "suyash@suyashkumar.com"}).first() # Get the first user where _id=suyash@suyashkumar.com
    print(user.email)
    print(user.heart_rate)
    print(user.heart_rate_times)

if __name__ == "__main__":
    connect("mongodb://localhost:27017/heart_rate_app") # open up connection to db
    # create_user() # we should only do this once, otherwise will overwrite existing user
    add_heart_rate("suyash@suyashkumar.com", 60, datetime.datetime.now())
    print_user("suyash@suyashkumar.com")