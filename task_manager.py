#=====importing libraries===========
from datetime import date
from datetime import datetime
s = " " # defining a space to easily adjust amount of white space between words

#=============DEFINE ALL FUNCTIONS=====================

#==============REGISTER A USER=================

# define a function to register a user
def reg_user():
    print("\n--- REGISTERING A USER ---\n")
    # the user enters a username
    # repeats until entering a username that is not already listed
    while True:
        new_username = input("Enter new username : ")
        if new_username in user_dict:
            # error message if username is in dictionary
            print("\nThis username is already registered. Please try another username.\n") 
        else:
            break

    # the user enters a password and confirms password, repeats until both are the same
    while True:
        new_password = input("\nEnter new password : ")
        test_password = input("Confirm password : ")
                
        if new_password == test_password:
            break
        else:
            print("\nThese passwords do not match. Please try again:")
            
    # the username and password are written to user.txt in required format 
    # opened with mode 'a' as do not want to overwrite text file, instead add to it
    with open("user.txt", "a") as users1:
        users1.write(f"\n{new_username}, {new_password}")
            
    # add new user to dictionary as well, as use this for adding tasks etc later on
    user_dict[new_username] = new_password
            
    print(f"\nSUCCESS - You have registered a new user: {new_username}.")





#==============ADDING A TASK=================

# define a function to add a task
def add_task():
    print("\n--- ADDING A TASK ---")
    # presents list of usernames
    # the user enters the username of the person the task is assigned to
    # repeats until user enters a valid username
    print("\nWhich of the following users is the task assigned to?")
    for usernames in user_dict:
        print(f"{10*s}- {usernames}")
    while True:
        which_user = input("\n: ")
        if which_user not in user_dict:
            print("\nError - this username is not listed. Please try again.")
        else:
            break

    # the user enters relevant data about the task
    task_title = input("\nTitle of task : ").capitalize()
    task_descript = input("\nDescription of task : ")

    # user enters due date
    # repeat until user enters date in specified format
    while True:
        due_date_string = input("\nDue date (dd/mm/yyyy) : ")
        try:
            due_date = datetime.strptime(due_date_string, "%d/%m/%Y")               
        except:
            print("\nInvalid input. Please enter the date in the specified format.")
            continue
        break

    # get the current date from datetime library
    today = date.today()
        
    # the data is written to tasks.txt in the correct format
    with open("tasks.txt", "a") as tasks1:
        tasks1.write(f"\n{which_user}, {task_title}, {task_descript}, {today.strftime('%d %b %Y')}, {due_date.strftime('%d %b %Y')}, No")
        
    print(f"\nSUCCESS - You have added a new task: {task_title}.")





#==============VIEW ALL TASKS=================

# define a function to view all tasks
def view_all():
    print("\n--- VIEW ALL TASKS ---")
    # read the tasks.txt file
    with open("tasks.txt", "r") as tasks2:
        # create number variable to label each task
        num = 1
        # loop through each line in tasks.txt
        # split each line into a list, separating at each ", " 
        for line in tasks2:
            line_list = line.split(", ") 
                
            # printing information in easy-to-read format
            print(f"\nTASK {num})")
            print(f"{9*s}Task:{20*s}{line_list[1]}")
            print(f"{9*s}Assigned to:{13*s}{line_list[0]}")
            print(f"{9*s}Date assigned:{11*s}{line_list[3]}")
            print(f"{9*s}Due date:{16*s}{line_list[4]}")
            print(f"{9*s}Completed?{15*s}{line_list[5]}".strip("\n"))
            print(f"""{9*s}Description of task:
            {line_list[2]}""")
            print(120*"_")

            num += 1 # add 1 to number variable





#==============EDITING OR COMPLETING A TASK=================

# define a function to edit a task or mark it as complete
# the argument tells the function which row the task is in the text file
def edit_task(row_num):
    # read the text file
    with open("tasks.txt", "r") as tasks3:
        # use readlines to read each line as an element in a list
        # use row_num as index to find the specific task
        rows = tasks3.readlines() 
        task_to_edit = rows[row_num].split(", ")
        
        print(f"\nYou have selected {task_to_edit[1]}.")

        # present the user with their options
        print(f'''\nWhat would you like to do?
{6*s}c - mark the task as complete
{6*s}ed - edit the task''')
        
        # loop until user enters valid option
        while True:
            action1 = input(": ").lower()
            if action1 not in ["c", "ed"]:
                print("\nInvalid answer. Please enter 'c' or 'ed'.") 
            else:
                break
        
        # if user wants to mark task as complete
        # if task is already complete - tell the user
        # if task is not complete - change from no to yes
        if action1 == "c":
            if task_to_edit[5] == "Yes":
                print("\nThis task is already complete.")
            else:
                task_to_edit[5] = "Yes"
                print("\nSUCCESS. This task has been marked as complete.")

        # if the user wants to edit the task
        # if task is already complete - tell the user they cannot edit it
        # if not, ask what they would like to edit
        elif action1 == "ed":
            if task_to_edit[5] == "Yes":
                print("\nThis task is already complete. You cannot edit it.")
            else:
                print(f'''\nWhat would you like to edit?
{6*s}u - which user the task is assigned to
{6*s}d - due date of task.''')

                # loop until the user enters a valid option
                while True:
                    action2 = input(": ").lower()
                    if action2 not in ["u", "d"]:
                        print("\nInvalid answer. Please enter 'u' or 'd'.") 
                    else:
                        break
                        
                # if the user wants to edit the user
                if action2 == "u":
                    print("\nWhich of the following users would you like the task to be assigned to?")
                    for usernames in user_dict:
                        print(f"{10*s}- {usernames}")
                    
                    # loop until the user enters a valid username
                    while True:
                        user_edit = input("\n: ")
                        if user_edit not in user_dict:
                            print("\nError - this username is not listed. Please try again.")
                        else:
                            break
                    
                    # change data in list
                    task_to_edit[0] = user_edit
                
                # else if the user wants to edit the due date
                elif action2 == "d":
                    # repeat until user enters date in specified format
                    while True:
                        due_date_edit = input("\nWhat is the new due date? (dd/mm/yyyy) : ")
                        try:
                            due_date_edit = datetime.strptime(due_date_edit, "%d/%m/%Y")               
                        except:
                            print("\nInvalid input. Please enter the date in the specified format.")
                            continue
                        break
                
                    # change data in list
                    task_to_edit[4] = due_date_edit.strftime('%d %b %Y')
                    
                print("\nSUCCESS. This task has been edited.")
        
        # for either option, now join the task back into a single string
        replacement_line = ", ".join(task_to_edit)
        
        # replace the relevant line with the replacement line
        # write the data (with the relevant changes) to the text file
        # overwriting the old text
        rows[row_num] = replacement_line    
        with open("tasks.txt", "w") as tasks4:
            tasks4.writelines(rows)  





#==============VIEWING USERS INDIVIDUAL TASKS=================

# define function to show user their individual tasks
def view_mine(user_to_show):
    print("\n--- VIEW MY TASKS ---")
    # read the tasks.txt file
    with open("tasks.txt", "r") as tasks5:
    # in a similar way to in view_all() function, print task information
    # but this time only print tasks assigned to the user

        num = 0 # define a variable to keep track of each task for the specific user
        row = -1 # define a variable to keep track of each row
        index_dict = {} # create an empty dictionary

        # loop through each line in text file
        for line in tasks5:
            line_list = line.split(", ")
            row += 1 # each line add 1 to row variable
            
            # check if task is assigned to the user
            if line_list[0] == user_to_show:
                num += 1 # add 1 to num variable
                print(f"\nTASK {num})")
                print(f"{9*s}Task:{20*s}{line_list[1]}")
                print(f"{9*s}Assigned to:{13*s}{line_list[0]}")
                print(f"{9*s}Date assigned:{11*s}{line_list[3]}")
                print(f"{9*s}Due date:{16*s}{line_list[4]}")
                print(f"{9*s}Completed?{15*s}{(line_list[5]).strip()}")
                print(f"""{9*s}Description of task:
                {line_list[2]}""")
                print(120*"_")

                # create a dict entry with num of task as key, and row in file as value
                index_dict[num] = row
                
    # selecting a specific task
    print("\n--- MARK AS COMPLETE OR EDIT A TASK ---")

    # user inputs which task they want to edit/mark as complete
    # repeat until enters a valid integer (either -1 or the num of one of their tasks)
    # if user enters -1 return to main menu
    # if user enters valid task num, call edit_task() function with the relevant row num as argument
    while True:
        task_choice = int(input('''\nSelect specific task:
        (or enter -1 to return to main menu)
    : '''))
        if (task_choice > num) or (task_choice < -1) or (task_choice == 0):
            print("\nInvalid option. Please try again")
        elif task_choice == -1:
            break
        else:
            edit_task(index_dict[task_choice])
            break





#==============GENERATING TASK REPORT=================

# define function to generate task report
def generate_task_report():
    # read tasks text file
    with open("tasks.txt", "r") as tasks6:

        # create variables to count the following
        num_tasks = 0
        num_complete = 0
        num_overdue = 0

        # loop through each line
        for line in tasks6:
            line_list = line.split(", ")
            # for each line, add 1 to num tasks variable
            num_tasks += 1

            # if the task is complete
            # add 1 to num complete variable
            if line_list[5].strip("\n") == "Yes":
                num_complete += 1
            
            # if task is incomplete
            # check if overdue
            else:
                # create date object for due date and todays date
                due_date = datetime.strptime(line_list[4], "%d %b %Y") 
                today = datetime.today()
                # check if due date was before today
                # if yes, add 1 to num overdue variable
                if today > due_date:
                    num_overdue += 1
        
        # calculate num of incomplete tasks
        num_incomplete = num_tasks - num_complete

        # calculate percentage of incomplete and overdue tasks
        percentage_incomplete = round(((num_incomplete/num_tasks)*100),1)
        percentage_overdue = round(((num_overdue/num_tasks)*100),1)

        # create a string to store all of this information
        task_overview_string = f'''total number of tasks, {num_tasks}
total number of complete tasks, {num_complete}
total number of incomplete tasks, {num_incomplete}
total number of overdue tasks, {num_overdue}
percentage incomplete, {percentage_incomplete}%
percentage overdue, {percentage_overdue}%'''

        # then write this string to a text file
        # overwriting any existing data
        # creating the file if it does not already exist
        with open("task_overview.txt", "w") as taskoverview1:
            taskoverview1.write(task_overview_string)
        
        print("\nSUCCESS - reports have been generated.")




#==============GENERATING USER REPORT=================

# define function to generate user report
def generate_user_report():
    # set total num of users equal to length of user dictionary
    total_users = len(user_dict)

    # count the total num of tasks by reading tasks.txt
    total_tasks = 0
    with open("tasks.txt", "r") as tasks7:
        for line in tasks7:
            total_tasks += 1

    # store this information in a string
    user_overview_string = f"General, total number of users, {total_users}"
    user_overview_string += f"\nGeneral, total number of tasks, {total_tasks}"
    
    # loop through each user
    # calculating all the relevant data as in generate_task_report() function
    # but this time check if each task is assigned to the user
    for user in user_dict:
        with open("tasks.txt", "r") as tasks8:
            num_tasks = 0
            num_complete = 0
            num_overdue = 0

            for line in tasks8:
                line_list = line.split(", ")

                if line_list[0] == user:
                    num_tasks += 1

                    if line_list[5].strip("\n") == "Yes":
                        num_complete += 1
                    else:
                        due_date = datetime.strptime(line_list[4], "%d %b %Y") 
                        today = datetime.today()
                        if today > due_date:
                            num_overdue += 1
            
        # calculate num incomplete tasks for each user
        num_incomplete = num_tasks - num_complete
        
        # if total_num_tasks not zero, calculate percentages for each user
        # otherwise set percentages equal to zero
        if num_tasks != 0:
            percentage_incomplete = round(((num_incomplete/num_tasks)*100),1)
            percentage_overdue = round(((num_overdue/num_tasks)*100),1)
        else:
            percentage_incomplete = 0
            percentage_overdue = 0

        # add all of this information to the string
        user_overview_string += f'''\n{user}, total number of tasks, {num_tasks}
{user}, number of complete tasks, {num_complete}
{user}, number of incomplete tasks, {num_incomplete}
{user}, number of overdue tasks, {num_overdue}
{user}, percentage incomplete, {percentage_incomplete}%
{user}, percentage overdue, {percentage_overdue}%'''

    # then write this string to a text file
    # overwriting any existing data
    # creating the file if it does not already exist
    with open("user_overview.txt", "w") as user_overview1:
        user_overview1.write(user_overview_string)





#==============DISPLAYING STATISTICS=================

# define a function to display statistics
def display_statistics():
    print("\n--- DISPLAY STATISTICS ---")
    # call the following functions to generate reports
    # (even if reports have already been generated, do this again in case any data has been changed since)
    generate_task_report()
    generate_user_report()

    # print all the information from these files in an easy-to-read way
    # first display overview of tasks by reading task_overview.txt
    print("\nOVERVIEW OF TASKS:\n")
    with open("task_overview.txt", "r") as task_overview2:
        for line in task_overview2:
            title = ((line.split(", "))[0]).capitalize()
            value = (line.split(", "))[1]
            print(f"{10*s}{title}{(36-len(title))*s}:{3*s}{value}", end = "")
    
    print("\n")
    print(100*"-")
    # then display overview of users by reading user_overview
    print("\nOVERVIEW OF USERS")
    with open("user_overview.txt", "r") as user_overview2:
        user_test = ""
        for line in user_overview2:
            user = (line.split(", "))[0]
            title = ((line.split(", "))[1]).capitalize()
            value = (line.split(", "))[2]
            # if user changes, print this as a heading
            if user != user_test:
                print(f"\n{user}:")
                user_test = user
            print(f"{10*s}{title}{(30-len(title))*s}:{3*s}{value}", end = "")
    print("\n")





        

#==================RUNNING THE PROGRAMME=====================

#==============LOGIN SECTION=================

print("--- LOGIN ---")

# converting data in user.txt to a dictionary storing usernames and corresponding passwords
user_dict = {}
with open("user.txt", "r") as users2:
    for line in users2: # loop through each line of text
        info_list = line.split(", ") # separate the string at each ", ", hence creating a list with separte username and password 
        user_dict[info_list[0]] = info_list[1].strip("\n") # add username to dictionary as the key, with the password as the value

# the user inputs a username and password until a valid entry is made
while True:
    username = input("\nEnter username : ")
    password = input("Enter password : ")
    if username not in user_dict: # if username not listed
        print("This username is not registered. Please try again.")
    elif user_dict[username] != password: # if valid username but incorrect password
        print("Incorrect password. Please try again.")
    else:
        print(f"\nWelcome {username}!")
        break
    




#==============MENU DISPLAYED=================

while True:
    # this menu is displayed to everyone apart for the admin
    if username != "admin":
        print("\n--- MENU ---")
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
        menu = input('''\nSelect one of the following Options:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    \n: ''').lower()

    # separate menu presented to the admin with option to display statistics and generate reports
    else:
        print("\n--- MENU ---")
        # presenting the menu to the user and 
        # making sure that the user input is coneverted to lower case.
        menu = input('''\nSelect one of the following Options:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    ds - display statistics
    e - Exit
    \n: ''').lower()  


    # check which option the user inputted
    # and carry out the corresponding tasks

    # if user inputs 'r'
    if menu == 'r':
        # only admin can register users
        # if current user is admin, call the function to register a user
        if username == "admin":
            reg_user()
        # if user is not admin, error message is displayed
        else:
            print("\nAccess denied - only the admin can register users.")

    # if user inputs 'a'
    # call function to add a task
    elif menu == 'a':
        add_task()

    # if user inputs 'va'
    # call function to view all tasks
    elif menu == 'va':
        view_all()

    # if user inputs 'vm'
    # call function to view the user's tasks
    elif menu == 'vm':
        view_mine(username)
        
    # if user inputs 'gr'
    # check if user is admin
    # if yes, call function to generate reports
    elif menu == 'gr':
        if username == "admin":
            generate_task_report()
            generate_user_report()

        # if not admin, display error message
        else:
            print("\nAccess denied - only the admin can generate reports.")
    
    # if user inputs 'ds'
    # check if user is admin
    # if yes, call function to display statistics
    elif menu == "ds":
        if username == "admin": 
            display_statistics()
        # if not admin, display error message
        else:
            print("\nAccess denied - only the admin can display statistics.")
        

        

#==============EXIT=================  
    # if user enters 'e', exit the programme
    elif menu == 'e':
        print('Goodbye!!!')
        exit()


    # if the user enters a different letter, go back to menu
    else:
        print("You have made a wrong choice, Please try again.")