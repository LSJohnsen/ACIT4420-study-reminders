import datetime
from pathlib import Path

'''
Module for logging different events in the automation process:
https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve
'''
# logs whenever a study reminder is sent to a student at their preferred time
# Added path to save logs in separate folder

folder_path = Path(__file__).resolve().parent.parent / "logs"

def log_reminder(student, reminder):
    reminder_path = folder_path / "reminder_log.txt"
    with open(reminder_path, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {student['name']}: {reminder}\n")

# logs if there occurs any error when attempting to send a study reminder to students
def log_reminder_error(student):
    error_path = folder_path / "error_log.txt"
    with open(error_path, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Error sending reminder to {student['name']}\n")

# logs whever a study reminder is first generated with the time it should be sent out eveyr day
def log_reminder_generation(student, reminder):
    generation_path = folder_path / "generated_reminders_log.txt"
    with open(generation_path, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Reminder for {student['name']} for {student['preferred_time']} was generated: {reminder} \n")


