import sqlite3
import random
conn = sqlite3.connect("StudentRecords.db")
cur = conn.cursor()

#Deletes StudentRecords table if it exists, then creates it.
cur.execute("DROP TABLE IF EXISTS StudentRecords")
cur.execute("""
    CREATE TABLE StudentRecords
    (  id     INT          NOT NULL,
       name   VARCHAR(40)  NOT NULL,
       age    INT,
       major  VARCHAR(20)  NOT NULL,
       PRIMARY KEY (id) )
""")
#Intial list of students
students = [
    (14806, 'Chad Broski', 25, 'Business'),
    (69572, 'Robin Banks', 26, 'Wallet Inspection'),
    (94583, 'Kris Falkner', 20, 'Computer Science'),
    (74030, 'Alice The Destroyer Of Worlds', 9999, 'Liberal Arts'),
    (55176, 'Mr. Least', 30, 'Communications'),
]
cur.executemany("INSERT INTO StudentRecords VALUES(?, ?, ?, ?)", students)
conn.commit()

#Prints all current students (excluding ID).
print("List of current students:")
cur.execute("SELECT name, age, major FROM StudentRecords")
for row in cur.fetchall():
    print(row)

#Prompts the user for a valid input. If is_number is True, input must be all numbers.
def get_User_Input(prompt, is_number):
    user_input = input(prompt)
    while True:
        if not is_number and user_input != "": #If is_number is False, it only insures the string isn't empty.
            return user_input
        elif is_number and user_input.isdigit():
            return int(user_input) #Returns int if is_number is True
        else: #Asks again if input was invalid.
            user_input = input("Invalid input, please try again: ")

#Prompts the user to answer a yes or no question. Returns True if the answer is yes or y, and returns False if the answer is no or n.
def y_or_n(prompt):
    user_input = input(prompt).lower() #Uses .lower() to make input case insensitive.
    while True:
        if user_input in ['yes', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else: #Asks again if input was invalid.
            user_input = input("Invalid input, please try again: ").lower()

#Asks the user if they want to add a new student.
if y_or_n("\nDo you want to add a new student? (yes/no): "):
#If the user says yes:
    name = get_User_Input("Please enter the student's name: ", False)
    age = get_User_Input("Please enter the student's age: ", True)
    major = get_User_Input("Please enter the student's major: ", False)
    #Gets a list of all IDs in use and stores it in used_ids.
    cur.execute("SELECT id FROM StudentRecords")
    used_ids = cur.fetchall()
    #Generates random numbers until it finds one that isn't in use. It should be very unlikely this loops even once.
    while True:
        new_id = random.randint(10000, 99999)
        if new_id not in used_ids:
            break
    #Adds the new student and their information to the table.
    cur.execute("INSERT INTO StudentRecords VALUES(?, ?, ?, ?)", (new_id, name, age, major,))
    print(f"Added {name} to the student records.")
else:
    #If they say no:
    print("Fine then. Be that way.")

#Saves changes and closes the connection.
conn.commit()
conn.close()
