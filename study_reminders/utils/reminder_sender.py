
# function for sending reminder - currently just a print statement that is used to log 
def send_reminder(email, reminder):
    if not email:
        raise ValueError("Email address is missing")
    
    print(f"Sending email to {email}: {reminder}")