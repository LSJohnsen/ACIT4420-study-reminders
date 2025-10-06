import datetime

'''
Module for logging different events in the automation process:
'''

# logs whenever a study reminder is sent to a student at their preferred time
def log_reminder(student, reminder):
    with open("reminder_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {student['name']}: {reminder}\n")

# logs if there occurs any error when attempting to send a study reminder to students
def log_reminder_error(student):
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Error sending reminder to {student['name']}\n")

# logs whever a study reminder is first generated with the time it should be sent out eveyr day
def log_reminder_generation(student, reminder):
    with open("generated_reminders_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Reminder for {student['name']} for {student['preferred_time']} was generated: {reminder} \n")
