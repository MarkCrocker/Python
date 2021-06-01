# Our friend Roy is a recent surgical patient, and has many medications
# to keep track of. Each medication has different 
# requirements of when you're supposed to take it, 
# and how many hours later you're supposed to take
# the next one.
# This can be a lot to keep track of, especially when 
# you're feeling unwell. Let's write a program to 
# help Joey out. 
# Your program should take in the following as input: 
# A medication name as a string
import datetime

med = input("Input the medication name: ")

# how long ago in minutes that the medication was taken (as an integer)


# and how often in minutes it should be taken (as an integer).
time_taken = 0
when_to_take = 0

take = int(input("how often should this be taken?: "))
when_minutes = int(input("how long ago did you take this?:  "))

current_time = datetime.datetime.now()
time_taken = current_time - datetime.timedelta(minutes=when_minutes)

when_to_take = time_taken + datetime.timedelta(minutes = take)
print(f"You have taken {med} at:{time_taken}")
print(f"You need to take {med} again at {when_to_take}")

# After this, your program should write all the input
# information to a file.

# f = open("medication.txt", "a")
# f.write()


# It should also calculate the 
# actual time that the medication was last taken,

# current_time = datetime.now()
# time_taken = current_time - datetime.timedelta(minutes = when_minutes)




# as well as the time it should next be taken.
# Note, we can use the datetime library to do this.
# To do this, we would want to use datetime.now() 
# to get the current time, then we'd want to use 
# timedeltas to add or subtract a number of minutes.
# For example, let's say that the medication was taken 20 
# minutes ago, we could do the following:
# current_time = datetime.now()
# medication_taken_time = current_time - datetime.timedelta(minutes=20)
# Likewise, if we knew that medication had to be taken 
# 90 minutes after it was taken the first time, we could do:
# medication_next_time = medication_taken_time + datetime.timedelta(minutes=90)
# Of course, in our actual program, the number of minutes 
# before and after will be an input given by the user, so
# we'd pass that variable instead of a literal number
# like 20 or 90.
# Once you've calculated these values, write the current
# time, the time that the medication was taken, and
# the next time the medication should be taken to a file.
# Remember, we can write datetime objects out to files,
# just by using the variables themsevels. For example:
# current_time = datetime.datetime.now()
# f.write("The current time is: {}".format(current_time))
# The same is true of medication_taken_time, or medication_next_time
# from the examples above, they can be written to a file in exactly
# the same way.
# Your program should repeatedly prompt for the medication 
# inputs described above in a loop, asking the user if 
# they're finished each time, and only ending once the 
# user indicates that they're done.
# When the loop is done, have it write the total number of
# medications entered to the end of the file, and then
# have it write a friendly message like, 
# "We hope you get well soon!"
# Note, that the file should be opened in append mode,
# so as to keep a record of all the medications used by
# the patient.