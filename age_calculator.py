from datetime import date, datetime

char_list = ['/', '-', '.']
linebreak = ("") # for visibility

def is_valid_date(user_birthday):
    if len(user_birthday) == 10:  # maximum character length is 10
        # Check if the format and characters are correct
        if (user_birthday[0:2].isdigit() and user_birthday[3:5].isdigit() and 
            user_birthday[6:10].isdigit() and user_birthday[2] in char_list and 
            user_birthday[5] in char_list):

            # Check if the month, day, and year are in valid ranges
            if (1 <= int(user_birthday[0:2]) <= 31 and 
                1 <= int(user_birthday[3:5]) <= 12 and 
                int(user_birthday[6:10]) <= date.today().year):
                return True

            elif int(user_birthday[6:10]) > date.today().year:  # Future year validation
                print(linebreak)
                print("ERROR: You entered a future year")

            elif int(user_birthday[3:5]) > 12:  # Month should be between 1 and 12
                print(linebreak)
                print("ERROR: Month should be between 1 and 12")

            elif int(user_birthday[0:2]) > 31:  # Day should be between 1 and 31
                print(linebreak)
                print("ERROR: Day should be between 1 and 31")

    return False

# Print the title at the start of this program
print(linebreak)
print(" Age Calculator by Buddhika ".center(50, "="))  # Centered title with borders for visibility

while True:
    print(linebreak)
    print("Please ensure the format is DD/MM/YYYY") 
    print(linebreak)
    user_birthday = input("When is your birthday? ").strip()  # Get the input without spaces from the user
    
    if is_valid_date(user_birthday):  # Validate the input
        corrected_date = user_birthday.replace('-', '/').replace('.', '/')

        try:
            # Try to convert the corrected date to a datetime object to catch invalid dates (e.g., 31st February)
            birthdate = datetime.strptime(corrected_date, "%d/%m/%Y").date()

            today = date.today()
            
            # Calculate age
            age = today.year - birthdate.year
            if (today.month, today.day) < (birthdate.month, birthdate.day):
                age = age - 1

            # Calculate remaining days until the next birthday
            next_birthday = birthdate.replace(year=today.year)
            if next_birthday < today:
                next_birthday = birthdate.replace(year=today.year + 1)

            days_remaining = (next_birthday - today).days

            # Print results
            print(linebreak)
            print("> You are", age, "years old")
            print(linebreak)
            print("> There are", days_remaining, "days remaining until your next birthday.")
            print(linebreak)

            # Ask if the user wants to continue
            continue_choice = input("Do you want to continue? (yes/no): ").strip().lower() # Get the input without spaces and convert to lowercase
            if continue_choice not in ["yes", "y", 1]:
                print(linebreak)
                print("Thank you for using the Age Calculator. Goodbye!")
                print(linebreak)
                break # Exit the loop if the user doesn't want to continue

        except ValueError:  # Handle invalid dates
            print(linebreak)
            print("ERROR: Invalid date. Please enter a valid date.")
    else:
        print(linebreak)
        print("Invalid Input. Let's try again.")
