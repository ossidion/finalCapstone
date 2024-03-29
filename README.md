# **Final Capstone Project (T17) - Lists, Functions, and String Handling: Task List**

## **Table of Contents**
- Project Description
- Installation Instructions
- Usage (How to Use this Project)

## **Project Description**

This project has been created in order to manage tasks associated with a range of users. The program allows for:
 - Registering a user
 - Adding a task
 - Viewing all tasks
 - Viewing my tasks
 - Generation of reports
 - Displaying statistics.

This project initially works by requesting admin to login. Once logged in, the admin is able to register new users
and assign them unique passwords. These users and passwords are then stored in a txt. file so when the program
is next run, one of those users will be able to sign in. 

The program allows for the adding and viewing of tasks. Information regarding each task includes:
 - Username assigned to task.
 - Title of task.
 - Description of task.
 - Due date of task.
 - Date assignment date; and
 - Completion status of the task.

The program includes a report generation feature which outputs information regarding the users and tasks
into dedicated txt. files. Statistacal display functionality is also included which displays program statistics
to the console. 

Those who would benefit from this project include anyone who would like a task management system to organise
their work and the work load of their team. This program would also benefit those who would like to learn
more about Python and how to create programs like this. 

The goal of this project is to provide organisation to anyone who uses it and to help others learn Python.

## **Installation Instructions**

Download the file 'task_manager.py' and open in your IDE. Run the program and enter the username: 'admin' with
the password: 'password' to begin. 

**Usage (How to Use this Project)**

Once you are logged in as 'admin', you can access any of the functionality described in the **Project Description**
and listed below within this usage guide.

 - Registering a user
   Press 'r' to register a user then add the information you would like. An example is below:
   ![image](https://github.com/ossidion/finalCapstone/assets/151433415/70f906c0-e2dd-4275-94e8-ee3901bdcce8)

   In order to prevent duplicate usernames, the program includes a while loop which iterates through the    
   existing
   usernames. An example is below:
   ![image](https://github.com/ossidion/finalCapstone/assets/151433415/0227d94d-0297-4f86-8496-5863d1731e48)
 

 - Adding a task
   Press 'a' to add a task then add the information you would like. An example is below:
   ![image](https://github.com/ossidion/finalCapstone/assets/151433415/aa87c52d-c3cd-4c35-8326-735cefb28fda)

   New tasks are appended to the existing list of tasks which is re-written to the 'tasks.txt' output file as
   shown below:
   ![image](https://github.com/ossidion/finalCapstone/assets/151433415/b5079a27-aebb-43e7-9236-d1e7eed93039)

 - Viewing all tasks
   In order to view tasks, type 'va' at the menu. An example of the out put is below:
   ![image](https://github.com/ossidion/finalCapstone/assets/151433415/5993ebe6-e0d5-47ec-a825-93cb0b4d810d)

   This functionality is achieved by iterating through the task list and printing as an f string, as shown
   below:
   ![image](https://github.com/ossidion/finalCapstone/assets/151433415/5c648fc3-594d-455f-b02d-f892dbb3f579)

 - Viewing my tasks
   The current user who is logged in can view their own tasks, as shown below:
   ![image](https://github.com/ossidion/finalCapstone/assets/151433415/ff3718ab-280d-415b-a98c-d1db94a36ff1)

   The enumerate function is used so that the user can select a task number and edit it as shown below:
   ![image](https://github.com/ossidion/finalCapstone/assets/151433415/bee46ef8-9fbf-43ee-90e6-ff3e0a8ee5ae)

 - generation of reports
   Reports are generated by pressing 'gr' with the output shown below:
   ![image](https://github.com/ossidion/finalCapstone/assets/151433415/3d16aabf-a517-4f37-b2e0-aeb864a96b55)

 - Displaying statistics.
   Statistics are generated by pressing 'ds' with the output shown below:
   ![image](https://github.com/ossidion/finalCapstone/assets/151433415/72bc1d08-7d2a-43eb-8c82-b14b578cf8b2)


## **Credits**

Alexander Graham

Hyperion Dev

CoGrammar

Lecturers and BYB staff who have helped me (Alex) get to where I am. 
