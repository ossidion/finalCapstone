# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}
    
    

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    # print(task_components)
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    # Updated the below line to keep consistency with True and False until "Yes" / "No is required in the 'vm' section.
    curr_t['completed'] = True if task_components[5] == "True" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password
    
logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


def reg_user():
    '''Add a new user to the user.txt file'''
    # Request input of a new username. If a username has already been 
    # taken, the user is prompted to choose another.
    new_username = input("New Username: ")
    while new_username in username_password.keys():
        new_username = input("This username has been taken, please choose another: ")
        continue
        
    else:
        print("Username: added.")
    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
            
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")



# Functions are below. There is a specific ordering of the functions so that 'def view_mine'
# function directly preceeds the menu. This gives the user the option to return to the
# main menu at multiple points form within the 'def view_mine' function. 

def add_task():

    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
         - A username of the person whom the task is assigned to,
         - A title of a task,
         - A description of the task and 
         - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    # The below line checks whether the user exists.
    while task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        task_username = input("Name of person assigned to task: ")
        continue
    
    # The below block requests information regarinding the task. 
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    # If the date format isn't correct, the user will be prompted to enter it in the correct format. 
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    # Write to 'tasks.txt'
    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "True" if t['completed'] else "False"
            ]


            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")



def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def generate_reports():

    '''Generates two reports, 'task_overview.txt' and 'user_overview.txt'.
        These reports output data in a user-friendly, easy to read manner
        using the logic contained within this function. 
    '''

    # Task_overview.txt

    # Total tasks

    total_tasks = (len(task_list))


    # Total number of completed and incomplete tasks.

    completed_tasks = 0
    incomplete_tasks = 0

    # Counters to count how many tasks are complete and incomplete. 
    for t in task_list:
        if t['completed'] == False:
            incomplete_tasks += 1
        elif t['completed'] == True:
            completed_tasks += 1
        else:
            pass

    # Total number of incomplete tasks which are overdue.

    
    # Getting current date in required format and then converting to string. 
    current_date = datetime.now().strftime(DATETIME_STRING_FORMAT)
    current_date = datetime.strptime(current_date, DATETIME_STRING_FORMAT)
    
    incomplete_due_dates = []

    # Accumulating tasks which are incomplete. 
    for t in task_list:
        if t['completed'] == False:
            incomplete_due_dates.append(t['due_date'])

    # Accumulating the incomplete tasks which are overdue. 
    overdue_counter = 0 
    for t in incomplete_due_dates:
        if t <= current_date:
            overdue_counter += 1

    
    # Percentage of tasks which are incomplete.

    # Getting percentage of incomplete tasks.
    sum_of_incomplete = overdue_counter
    try:
        sum_of_incomplete = sum_of_incomplete / total_tasks * 100

    # If there are no tasks, the answer is set to 0 to avoid error. 
    except ZeroDivisionError:
        sum_of_incomplete = 0

    
    # Percentage of tasks which are overdue.

    # Getting percentage of tasks which are overdue.
    sum_of_overdue = len(incomplete_due_dates)
    try:
        percentage_overdue = sum_of_overdue / total_tasks * 100
    
    # If there are no tasks, the answer is set to 0 to avoid error. 
    except ZeroDivisionError:
        percentage_overdue = 0



    # user_overview.txt


    # Total Users

    total_users = (len(user_data))


    # The total number of tasks assigned to each user. 

    # Creating a copy of the "username_password" dictionary to work with.
    user_task_count = username_password.copy()

    # Setting the values of each user to 0.
    for i, j in user_task_count.items():
        user_task_count[i] = int(0) 

    # Iterating over tasks and assigning tasks to corresponding users.    
    for user in user_task_count.keys():
        for task in task_list:
            if task['username'] == user:
                user_task_count[user] +=1

    user_task_count_keys = []
    user_task_count_values = []

    # Spliting data into separate dictionaries for flexibility later on.
    for user in user_task_count:
        user_task_count_keys.append(user)
        user_task_count_values.append(user_task_count[user])
    

    user_task_count_dict = {}
    # Adjoining keys and values into a new dictionary (for flexibility
    # when doing math and building output f string later on)
    for key in user_task_count_keys:
        for value in user_task_count_values:
            user_task_count_dict[key] = value
    

    # Dictionary containing users and number of assigned tasks.
    for user in user_task_count_dict.keys():
        for task in task_list:
            if task['username'] == user:
                user_task_count_dict[user] +=1


# The percentage of the total number of tasks that
# have been assigned to users.
        
    user_task_percentage_dict = {}

    # Getting percenatge of the total number of tasks that
    # have been assigned to users.
    for key in user_task_count_dict:
        try:
            user_task_percentage_dict[key] = user_task_count_dict[key]/total_tasks*100
        # If there are no tasks for the user, or there is a 0 div error, the answer is set to 0 to avoid error. 
        except ZeroDivisionError:
            user_task_percentage_dict[key] = 0


# The percentage of the tasks assigned to that user that have been completed.    

    count_completed_dict = {}
    count_inocmplete_dict = {}

    # Creating dictionary with 0 values to eventually store
    # count of completed tasks for each user.
    for key in user_task_count_keys:
        for value in user_task_count_values:
            count_completed_dict[key] = value

    # Iterating over users and building a dictionary of count of
    # completed tasks for each user.
    for i in task_list:
        if i['completed'] == True:
            count_completed_dict[i['username']] += 1


    # Getting percenatge of tasks assigned to that user that have been completed.
    for key in user_task_count_dict:
        try:
            count_completed_dict[key] = count_completed_dict[key]/user_task_count_dict[key]*100
        # If there are no tasks for the user, or there is a 0 div error, the answer is set to 0 to avoid error. 
        except ZeroDivisionError:
            count_completed_dict[key] = count_completed_dict[key]


# The percentage of the tasks assigned to that user that
# have not been completed.
    
    # Creating dictionary with 0 values to eventually store
    # count of incomplete tasks for each user.
    for key in user_task_count_keys:
        for value in user_task_count_values:
            count_inocmplete_dict[key] = value

    # Iterating over users and building a dictionary of
    # count of incomplete tasks for each user.
    for i in task_list:
        if i['completed'] == False:
            count_inocmplete_dict[i['username']] += 1

    # Getting percenatge of tasks assigned to that user that are incomplete.
    for key in user_task_count_dict:
        try:
            count_inocmplete_dict[key] = count_inocmplete_dict[key]/user_task_count_dict[key]*100
        # If there are no tasks for the user, or there is a 0 div error, the answer is set to 0 to avoid error. 
        except ZeroDivisionError:
            count_inocmplete_dict[key] = count_inocmplete_dict[key]

    
    # The percentage of the tasks assigned to that user that
    # have not yet been completed and are overdue

    tasks_incomplete_overdue_dict = {}

    # Creating dictionary with 0 values to eventually store
    # count of incomplete tasks for each user which are overdue.    
    for key in user_task_count_keys:
        for value in user_task_count_values:
            tasks_incomplete_overdue_dict[key] = value
    # print(f"tasks_incomplete_overdue_dict HERE = {tasks_incomplete_overdue_dict}")
    
    # Iterating over users and building a dictionary of count of
    # incomplete tasks which are overdue for each user.
    for i in task_list:
        if i['completed'] == False and i['due_date'] <= current_date:
            tasks_incomplete_overdue_dict[i['username']] += 1

    # Getting percenatge of tasks assigned to that user that are incomplete and overdue.
    for key in tasks_incomplete_overdue_dict:
        try:
            tasks_incomplete_overdue_dict[key] = tasks_incomplete_overdue_dict[key]/user_task_count_dict[key]*100
        # If there are no tasks for the user, or there is a 0 div error the answer is set to 0 to avoid error. 
        except ZeroDivisionError:
            tasks_incomplete_overdue_dict[key] = tasks_incomplete_overdue_dict[key]
    
    

    # If 'task_overview.txt' doesn't exist, it is created. The output for the below f string is stored in 'task_overview.txt'.
    if not os.path.exists("task_overview.txt"):
        with open("task_overview.txt", "w") as task_overview_file:
            task_overview_file.write(f"====================== TASK OVERVIEW - PREPARED DATE: {current_date} ======================\n\n"
                    +f"Total number of tasks: {total_tasks}\n"
                    +f"Total number of completed tasks: {completed_tasks}\n"
                    +f"Total number of incomplete tasks: {incomplete_tasks}\n"
                    +f"Total number of overdue tasks to be completed: {overdue_counter}\n"
                    +f"Percentage of tasks which are incomplete: {sum_of_incomplete}%\n"
                    +f"Percentage of incomplete tasks which are overdue: {percentage_overdue}%\n\n"
                    +"============================================================================================")
    
    # If 'task_overview.txt' exists, it is overwritten. The output for the below f string is stored in 'task_overview.txt'.
    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write(f"====================== TASK OVERVIEW - PREPARED DATE: {current_date} ======================\n\n"
                    +f"Total number of tasks: {total_tasks}\n"
                    +f"Total number of completed tasks: {completed_tasks}\n"
                    +f"Total number of incomplete tasks: {incomplete_tasks}\n"
                    +f"Total number of overdue tasks to be completed: {overdue_counter}\n"
                    +f"Percentage of tasks which are incomplete: {sum_of_incomplete}%\n"
                    +f"Percentage of incomplete tasks which are overdue: {percentage_overdue}%\n\n"
                    +"============================================================================================")
    

    # If 'user_overview.txt' doesn't exist, it is created. The output for the below f string is stored in 'user_overview.txt'.
    if not os.path.exists("user_overview.txt"):
        with open("user_overview.txt", "w") as user_overview_file:
            user_overview_file.write(f"====================== USER OVERVIEW - PREPARED DATE: {current_date} ======================\n\n"
                    +f"Total number of users: {total_users}\n"
                    +f"Total number of tasks: {total_tasks}\n\n"
                    +"============================================================================================")
            
            # The below f string is iterated for each user. 
            for user in user_task_count_dict:
                user_overview_file.write(f"============================== OVERVIEW FOR USER {user} ==============================\n\n"
                                        +f"Assigned number of tasks: {user_task_count_dict[user]}\n"
                                        +f"Percentage of total number of tasks: {user_task_percentage_dict[user]}\n"
                                        +f"The percentage of tasks which are completed: {count_completed_dict[user]}%\n"
                                        +f"The percentage of tasks which are incomplete: {count_inocmplete_dict[user]}%\n"
                                        +f"The percentage of incomplete tasks overdue: {tasks_incomplete_overdue_dict[user]}%\n\n"
                                        )

    # If 'user_overview.txt' exists, it is overwritten. The output for the below f string is stored in 'user_overview.txt'.
    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write(f"====================== USER OVERVIEW - PREPARED DATE: {current_date} ======================\n\n"
                    +f"Total number of users: {total_users}\n"
                    +f"Total number of tasks: {total_tasks}\n\n")
        
        # The below f string is iterated for each user. 
        for user in user_task_count_dict:
            user_overview_file.write(f"--------------------------- OVERVIEW FOR USER {user} --------------------------------\n"
                                        +f"Assigned number of tasks: {user_task_count_dict[user]}\n"
                                        +f"Percentage of total number of tasks: {user_task_percentage_dict[user]}\n"
                                        +f"The percentage of tasks which are completed: {count_completed_dict[user]}%\n"
                                        +f"The percentage of tasks which are incomplete: {count_inocmplete_dict[user]}%\n"
                                        +f"The percentage of incomplete tasks overdue: {tasks_incomplete_overdue_dict[user]}%\n\n\n"
                                        )            




'''For each user, this function displays all tasks in a manner that is easy to read. Each task is displayed
     with a corresponding number header (in bold, above each task) that can be used to identify the task. Users can select specific
     tasks or return to the main menu. Users can mark specific tasks complete and the completion status is shown to
     users with 'Yes' or 'No'. If a user chooses to edit a task, they can edit the username of the person to whom
     the task is assigned or the due date of the task. If the task is marked as complete, the user will not be able
     to edit the assigned user or due date (until the task is marked incomplete).
    '''
def view_mine():
     
        
    new_list = []
   
    # Changing 'completed' True and False statuses to 'Yes' and 'No' respectiviely.
    for t in task_list:
        if t['completed'] == True:
            t['completed'] = 'Yes'
        elif t['completed'] == False:
            t['completed'] = 'No'
    
    # Creating list of tasks for current user.
    for t in task_list:
        if t['username'] == curr_user:
            new_list.append(t)

    # Numbering the list of tasks for current user and printing to console.
    for i, task in enumerate(new_list, 1):
        print(f"\n\033[1mTask {i}\033[0m\nUser:\t\t\t{task['username']}\nTitle:\t\t\t{task['title']}\n"
              + f"Description:\t\t{task['description']}\n"
              + f"Due Date:\t\t{task['due_date']}\n"
              + f"Date Assigned:\t\t{task['assigned_date']}\n"
              + f"Completion Status:\t{task['completed']}\n")


    # User can select '-1' to return to main menu or select a task. The user_choice is -1 to account for
    # Python iterating from 0.    
    while True:        
        user_choice = input("Please select a task by entering the task number. "
                            +"If you would like to return to the main menu, please enter '-1': ")
        if user_choice == "-1":
            break
        elif user_choice.isnumeric():
            user_choice = int(user_choice)
            if user_choice <= (len(new_list)):
                if user_choice > 0:
                    user_choice = user_choice-1

                    # User can select '-1' to return to main menu, change completion status or edit the task.
                    while True: 
                        task_choice = input("\nWould you like to:\n\n1. Change task completion status; or\n"
                                            +"2. Edit the assigned user or due date of the task? "
                                            +"Please note, the task can only be edited if it has not been "
                                            +"marked as complete.\n-1. Return to main menu.\n\nPlease enter a number': ")
                        if task_choice == "-1":
                            break
                        elif task_choice.isnumeric():
                            task_choice = int(task_choice)
                            if task_choice == 1:
                                
                                # User can select '-1' to return to main menu or mark task as complete.
                                while True: 
                                    completion_status = input("\nWould you like to:\n"
                                                            +"1. Mark this task as complete\n"
                                                            +"2. Mark this task as incomplete?\n"
                                                            +"-1. Retun to main menu\n"
                                                            +"Please enter a number': ")                                
                                    if completion_status == "-1":
                                        break
                                    elif completion_status.isnumeric():
                                        completion_status = int(completion_status)
                                        if completion_status == 1 or 2:
                                            if completion_status == 1:
                                                user_task = new_list[user_choice]
                                                user_task['completed'] = True
                                                print("\nThis task has been marked as complete.")
                                                input("\nPress enter to continue: ")
                                                break              
                                            elif completion_status == 2:
                                                user_task = new_list[user_choice]
                                                user_task['completed'] = False
                                                print("\nThis task has been marked as incomplete.")
                                                input("\nPress enter to continue: ")
                                                break 
                                            else:
                                                print("\nInvalid entry.")
                                                continue
                                        break
                                    else:
                                        print("\nInvalid entry.")
                                        continue
                                    
                                break
                            # User can select '-1' to return to main menu. The user can edit the assigned user of the
                            # task or change the due date but only if the task is marked as incomplete.
                            elif task_choice == 2:
                                user_task = new_list[user_choice]
                                if user_task['completed'] == 'No':
                                    while True:
                                        edit_task_choice = input("Would you like to:\n"
                                            "1. Edit the assigned user of this task\n"
                                            "2. Edit the due date of this task?; or \n"
                                            "-1. Return to main menu\n"
                                            "Please select the number accordingly: ")
                                        if edit_task_choice == "-1":
                                                break
                                        elif edit_task_choice.isnumeric():
                                            edit_task_choice = int(edit_task_choice)
                                            if edit_task_choice == 1:
                                                # User will only be able to change task allocation to a saved user.
                                                while True:
                                                    updated_user = input("Enter user: ")
                                                    if updated_user in username_password.keys():
                                                        user_task = new_list[user_choice]
                                                        user_task['username'] = updated_user
                                                        print(f"The user of this task has been updated to {updated_user}")
                                                        input("\nPress enter to continue: ")
                                                        break 
                                                    else:
                                                        print("User is not recognised, please enter an existing user: \n")
                                                        continue
                                            # User will be prompted if date formating is incorrect. 
                                            elif edit_task_choice == 2:
                                                while True:
                                                    try:
                                                        updated_date = input("Due date of task (YYYY-MM-DD): ")
                                                        updated_due_date_time = datetime.strptime(updated_date, DATETIME_STRING_FORMAT)
                                                        user_task = new_list[user_choice]
                                                        user_task['due_date'] = updated_due_date_time
                                                        print(f"The due date of this task has been updated to {updated_due_date_time}")
                                                        input("\nPress enter to continue: ")
                                                        break 

                                                    except ValueError:
                                                        print("Invalid datetime format. Please use the format specified")    
                                           
                                            else:
                                                print("\nInvalid entry.\n")
                                                continue
                                            
                                        else:
                                            print("\nInvalid entry.\n")
                                            continue               
                                
                                else:
                                    print("\nTask completion status is complete and therefore, the assigened user"
                                          +"and completion date cannot be edited at this time.\n")
                                    input("Press enter to continue: ")
                                    continue
                                
                            else:
                                print("\nInvalid entry.\n")
                                continue
                            break
                        else:
                            print("\nInvalid entry.\n")
                            continue

                    break
                else: 
                    print("\nInvalid entry.\n")
                continue   

            else: 
                print("\nTask does not exist.\n")
                continue
        elif user_choice.isalpha():
            print("\nInvalid entry.\n")
            continue
        else:
            break
        
    
    # In order to extinguish any inconsistenies throughout the rest of the program, 'completed' 'Yes' and 'No' 
    # statuses are set back to True and False respectiviely as the 'Yes' and 'No' is required for the 'view mine()'
    # function only.  
    for t in task_list:
        if t['completed'] == 'Yes':
            t['completed'] = True
        elif t['completed'] == 'No':
            t['completed'] = False

    # Overwriting changes to "tasks.txt"
    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(f"{task['username']};"
                       +f"{task['title']};"
                       +f"{task['description']};"
                       +f"{task['due_date'].strftime(DATETIME_STRING_FORMAT)};"
                       +f"{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};"
                       +f"{task['completed']}\n")
                 
                       



while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()


    elif menu == 'a':
        add_task()


    elif menu == 'va':
        view_all()


    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        generate_reports()

                  
    
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
        and tasks.'''
        # As specified in the task brief, admin is able to display statistics so that
        # information is read from 'tasks.txt' and 'user.txt' and displayed
        # on the screen in a user-friendly manner. 'tasks.txt' and 'user.txt'
        # are created upon program start up. 
        with open("tasks.txt", 'r') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t for t in task_data if t != ""]
            num_tasks = len(task_data)
        with open("user.txt", 'r') as user_file:
            user_data = user_file.read().split("\n")
            user_data = [t for t in user_data if t != ""]
            num_users = len(user_data)

            print("-----------------------------------")
            print(f"Number of users: \t\t {num_users}")
            print(f"Number of tasks: \t\t {num_tasks}")
            print("-----------------------------------")    

            input("Press enter to continue: ")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")