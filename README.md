
# Study Reminders

Python package for automating personalized study reminders for students by their email, favorite course, and preferred study time.
Allows for managing student info, generating reminders, as well as automatic daily email reminders. 

## Features 
- Add, remove, and list students by their preferred study times.
- Automatically generate personalized study reminders.
- Send reminders via email using a reminder sender (currently a logged event).
- Log all reminder events (generation, sending, and errors).

## Installation
  - local:
       pip install dist/studyreminders-1.0.1-py3-none-any.whl
  - git install:
       pip install git+https://github.com/LSJohnsen/ACIT4420-study-reminders.git

  
    
## Application
  Run to studyreminders and choose option from menu:
  
```
Choose an option to:
1) clear the JSON file containing ALL student info
2) add new students to the file
3) remove students from file
4) display the current list of students
5) initialize automatic study reminders
q) quit

```
