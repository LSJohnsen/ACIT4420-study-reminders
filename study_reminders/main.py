
from study_reminders.utils.logger import log_reminder
from study_reminders.utils.reminder_sender import send_reminder
from study_reminders.utils.reminder_generator import generate_reminder
from study_reminders.utils.scheduler import schedule_reminder
from study_reminders.utils.student_manager import StudentsManager

def main():
    """
    Main module:
    Initializes the StudentsManager class where methods can be used to add/remove students etc.
    schedule_reminder is called with the studentmanager object containing student list to initialize the scheduler for study reminders
    """
    manager = StudentsManager()

    # Choice of mode allows for manual testing as well as initializing automatic study reminders
    while True:
        mode = str(input("\nChoose an option to:\n" \
    "1) clear the JSON file containing ALL student info\n" \
    "2) add new students to the file\n" \
    "3) remove students from file\n" \
    "4) display the current list of students\n" \
    "5) initialize automatic study reminders\n" \
    "q) quit\n\n")).strip()

        if mode == '1':
            manager.students = []
            manager.save_students()

        elif mode == '2':
            name = str(input("\nEnter the student name: ")).strip()
            email = str(input("\nEnter the student email address: ")).strip().replace(" ", "")
            course = str(input("\nEnter the student's favorite course: ")).strip().replace(" ", "")
            time = str(input("\nEnter the preferred study time (AM/PM or military time): ")).strip().replace(" ", "")
            manager.add_students(name, email, course, time)
            manager.save_students()
            print(f"\n--- Adding student:  {name}---")

        elif mode == '3':
            name = str(input("\nWhich student do you wish to remove from the file: ")).strip()
            manager.remove_students(name)
            manager.save_students()

        elif mode == '4':   
            print("\nCurrent list of students:\n")
            manager.list_students()

        elif mode == '5': 
            print("Automatic study reminders initialized, Ctrl+C to return to menu")
            schedule_reminder(manager, 
                      generate_reminder,
                      send_reminder,
                      log_reminder)
            
        elif mode.lower() == 'q':
            print("\nQuitting")
            break
            
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()