import schedule
import time
from datetime import datetime
from modules.logger import log_reminder_error, log_reminder_generation

'''
Schedules daily reminders for students at their preferred study time.
original for loop only registers first student, nested function will initialize every student before loop
Creation of reminders and every subsequent reminder logged in separate files, as well as errors in generation

datetime to apply 12hr to 24 hour conversion in case of AM/PM inputs: 
https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
'''

def schedule_reminder(students_manager, reminder_generator, reminder_sender, logger):
    for student in students_manager.get_students():
        preferred_times = string_to_24hr(student["preferred_time"])
        
        # Initially creates a log with the student, time and personalized reminder if input is valid
        try:
            reminder = reminder_generator(student["name"], student["course"])
            log_reminder_generation(student, reminder)
            
        except Exception as e:
            # If there's an error generating a student reminder it logs the event with the student info
            log_reminder_error(student) 

        # Creates reminder for each student that is repeated every day at the same time
        def student_reminder(s=student):
            try: 
                reminder = reminder_generator(s["name"], s["course"])       
                reminder_sender(s["email"], reminder)
                logger(s, reminder)
        
            except Exception as e:
                log_reminder_error(s, e)

        schedule.every().day.at(preferred_times).do(student_reminder)

        # schedule.every().day.at(string_to_24hr(student["preferred_time"])).do(lambda s=student, r=reminder: (reminder_sender(s["email"], r), logger(s, r)))

    # Keeps running the schedule reminder with checks every 30 secs
    try:
        while True:
            schedule.run_pending()
            time.sleep(30)
    
    except KeyboardInterrupt:
        print("\n\n\nDaily reminder stopped.")

def string_to_24hr(preferred_time): 
    # datetime to return string with 24H time format for preferred time to prevent errors in reminder and logging 
    try:
        time_in = preferred_time.strip().replace(" ","")     # strip spaces before/after and replace spaces 
        time_in = datetime.strptime(time_in, "%I:%M%p")      # %I = 12 hour clock, %p determines am/pm from 12 hour, %M = minutes
        time_out = time_in.strftime("%H:%M")                 # %H 24:%M Min
        return time_out
    except:
        raise ValueError(f"\n\n\nTime: {preferred_time} is an invalid time format!")