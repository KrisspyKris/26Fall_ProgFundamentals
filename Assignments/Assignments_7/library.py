import sqlite3
#List of command descriptions and their associated pre-built sql query if applicable. Entry index corresponds to the number the user inputs to run the command.
#Commands 8 and 9 have no sql query associated with them because they are handled by python in the main loop.
#The command 6 query needs a separate tuple containing a string with the chosen letter plus a % wildcard in order to work. This is handled in queryDatabase().
commands = [
    ("Every book, including id, title, subtitle, author, year, genre, copies, and ratings:", "SELECT * FROM books"), #0
    ("Books printed after 1990:", "SELECT title, author, year FROM books WHERE year > 1990"), #1
    ("Fiction books with more than two copies:", "SELECT title, copies FROM books WHERE genre = 'Fiction' AND copies > 2"), #2
    ("Books rated 5/5 or from before 1900:", "SELECT title, year, rating FROM books WHERE rating = 5 OR year < 1900"), #3
    ("Non-Mystery books:", "SELECT title, genre FROM books WHERE NOT genre = 'Mystery'"), #4
    ("Books in either the History or Science genres:", "SELECT title, genre FROM books WHERE genre IN ('History', 'Science')"), #5
    ("Author names starting with a chosen letter:", "SELECT DISTINCT author FROM books WHERE author LIKE ?"), #6
    ("Books with no rating:", "SELECT title, rating FROM books WHERE rating IS NULL"), #7
    ("Run commands 1-7 in order, then close the program.", None), #8
    ("Close the program", None), #9
]

#Constructs command menu used in the main loop.
command_menu = "\nOptions:"
for x in range(len(commands)):
    command_menu = f"{command_menu}\n{x}: {commands[x][0]}"

command_menu = f"{command_menu}\nPlease select a number 0-9: "

#Prompts the user for a letter from A-Z. Asks again if input is invalid. Always returns the chosen letter capitalized.
def getLetter():
    letter = input("Please select a letter (a-z): ")
    while True:
        if letter.isalpha() and len(letter) == 1: #Checks if input is a single letter.
            return letter.upper()
        else:
            letter = input("Please try again: ")

#Prompts the user for a number from 0-9. Asks again if input in invalid. Used for the main loop's command menu.
def getDigit():
    digit = input(command_menu) #Uses string from earlier as the intro prompt.
    while True:
        if digit.isdigit() and len(digit) == 1: #Checks if the input is a single digit.
            return int(digit)
        else:
            digit = input("Please try again: ")
    
#Fetchs the sql query corresponding to the chosen number from the commands list. Only works if input is between 0-7. 
def queryDataBase(command):
    if command == 6: #Handles command 6 as a special case.
        letter = getLetter()
        cur.execute(commands[6][1], (letter + "%",)) #Changes the placeholder in the original sql query to be a string with the letter plus the % wildcard.
        rows = cur.fetchall()
        if len(rows) != 0:
            print(f"\nAuthor names starting with '{letter}':") #Prints alt description based on letter selected.
            for row in rows:
                 print(row)
        else: #Prints an error if no author starting with the chosen letter is found.
            print(f"\nThere are no authors that start with the letter '{letter}'")
    elif command in range(0, 8): #Handles most cases. Prints the command description and then executes the sql command.
        print(f"\n{commands[command][0]}")
        cur.execute(commands[command][1])
        for row in cur.fetchall():
            print(row)
    else: #Failsafe in case command is not between 0-7. Theoretically, this shouldn't happen.
        return

#SQL connection setup
conn = sqlite3.connect("library.db")
cur = conn.cursor()

#SQL table setup. 
cur.execute("DROP TABLE IF EXISTS books")
cur.execute("""
    CREATE TABLE books
    (   id       INT         NOT NULL,
        title    VARCHAR(40) NOT NULL,
        subtitle VARCHAR(128),
        author   VARCHAR(30) NOT NULL,
        year     INT,
        genre    VARCHAR(20),
        copies   INT         NOT NULL,
        rating   INT,
        PRIMARY KEY (id) )
""")
#Added new subtitle column for IMMERSION AND WORLDBUILDING purposes.

#Adds the first row manually as per assignment instructions. Has no ratings.
cur.execute("""
    INSERT INTO books
    VALUES (0, 'My First Book', 'How I made the very first book in the world frfr no cap.', 'John Book', 0, 'History', 3, NULL)
""")

#Creates list containing the rest of the books.
books = [
    (1, 'My First Scam', 'How I made millions by pretending to write the first book in the world.', 'John Book', 2019, 'History', 3, 4),
    (2, 'A Picture Worth A Million Dollars', 'An accurate retrospective into the grand success of NFT\'s.', 'Albert Griftson', 2024, 'Fiction', 5, 1),
    (3, 'Library Management', 'The mysterious organization that\'s sending me threating letters like \"Notice of Termination\".', 'Li Braryian', 2025, 'Mystery', 1, 4),
    (4, 'Freshwater', None, 'Akwaeke Emezi', 2018, 'Fiction', 1, 5), #This is a real book, from an award-winning non-binary novelist from Nigeria.
    (5, 'Lua 5.4 Reference Manual', None, 'Roberto Ierusalimschy et. al', 2024, 'Science', 1, 4), #Also a real book. There are three authors, which is why I used et. al.
    (6, 'The History of the World\'s Worst Library', None, 'Li Braryian', 2024, 'History', 3, 5),
    (7, 'How to Hold Places', None, 'Kris Falkner', 1970, 'Non-Fiction', (2 ** 16), None), #Has 65536 copies, which is the 16-bit unsigned integer limit. The year refers to the Unix epoch.
    (8, 'TOP 10 BEST NUMBERS IN THE WORLD', '(number 7 will shock you)', 'Chad Broski', 2014, 'Top 10', 10, None),
    (9, 'NOTICE OF TRESPASS WARNING', 'This notice is to inform you, Li Braryian, that you are NO LONGER authorized to be on the library premises following your termin', 'Library Management', 2026, 'Fiction', 1, None), #Desc is cut off intentionally
    (10, 'LAST ONE TO LEAVE THE PAIN CUBE GETS $20', 'BOOK EDITION', 'Mr. Least', 2018, 'Drama', 5, 2),
]
#Adds the rest of the books to the table.
cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?)", books)
conn.commit() # save the changes to the file

#Main Loop. This is for the command menu.
while True:
    command = getDigit()
    if command in range(0, 8): #If the command is 0-7
        queryDataBase(command)
    elif command == 8: #Runs commands 1-7 and then exits if command is 8.
        for x in range(1, 8):
            queryDataBase(x)
        break
    else: #If command is 9 or somehow some other weird thing.
        break

#Closes the connection and prints a closing message.
conn.close()
print("\nDone.")
