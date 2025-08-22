# Imports
import json

# Classes

class TaskManager:


    def __init__(self):
        
        self.tasks = {}

        self.frequency_key = {
            1: 'Daily',
            2: 'Weekly',
            3: 'Biweekly',
            4: 'Monthly'
        }

    def run(self):
        
        # Main Program Loop

        # Initial Print Statement
        print_bar()
        print("| Please Choose Option                                         |")
        print_bar()
        print()
        print_bar()
        print("| [1] Display Tasks                                            |")
        print("| [2] Add New Task                                             |")
        print("| [3] Update Task                                              |")
        print("| [4] Delete Task                                              |")
        print("| [X] Exit                                                     |")
        print_bar()
        print()

        # Wait for User Input
        user_input = input()

        if user_input == 'X':
            return False
        
        choice = int(user_input)
        
        match choice:
            case 1:
                self.read_task()
            case 2:
                self.create_task()
            case 3:
                self.update_task()
            case 4:
                self.delete_task()

            
        return True

    def import_save(self):
        
        try:
            # Attempt to open save file
            with open("saves/user_data.json", "r", encoding='utf-8') as save_file:

                # Save File Found -> Read save file data
                self.tasks = json.load(save_file)
        except OSError:
            # Occurs if save file does not exist
            with open("saves/user_data.json", 'x') as save_file:
                json.dump({}, save_file)

    def save_data(self):

        try:
            # Attempt to write to save file
            with open("saves/user_data.json", "w", encoding="utf-8") as save_file:
                json.dump(self.tasks, save_file)
        except OSError:
            print("Error Saving Data ...")

    def create_task(self):

        # Create Task Print Statement
        print()
        print_bar()
        print_line("Please Enter A Name For Your New Task")
        print_bar()
        print()

        user_name_input = input()

        print()
        print_bar()
        print_line("Please Choose One Of The Following Task Frequencies")
        print_bar()
        print()
        print_bar()
        print_line("[1] Daily")
        print_line("[2] Weekly")
        print_line("[3] Biweekly")
        print_line("[4] Monthly")
        print_bar()
        print()

        user_frequency_input = input()
        frequency = int(user_frequency_input)

        if user_name_input in self.tasks:
            print_bar()
            print_line("ERROR : TASK ALREADY EXISTS")
            print_bar()
            stall()
        else:
            self.tasks[user_name_input] = frequency
            print_bar()
            print_line("Task Successfully Created")
            print_bar()
            stall()

    def read_task(self):
        
        print()
        print_bar()
        print_line("Tasks")
        print_bar()

        for name, frequency in self.tasks.items():
            task_string = f'{name} -> {self.frequency_key[frequency]}'
            print_line(task_string)
            print_bar()

        stall()

    def update_task(self):

        print()
        print_bar()
        print_line("Please Enter Name Of Task To Update")
        print_bar()

        counter = 1

        for key in self.tasks:
            task_string = f'[{counter}] {key}'
            print_line(task_string)
            print_bar()
            counter += 1

        print()

        user_task_input = input()

        print()
        print_bar()
        print_line("Update Name Or Frequency?")
        print_bar()
        print_line("[1] Update Name")
        print_line("[2] Update Frequency")
        print_bar()
        print()

        user_update_input = input()

        update_choice = int(user_update_input)

        if update_choice == 1:
            print()
            print_bar()
            print_line("Enter New Name")
            print_bar()
            print()

            user_new_name_input = input()

            task_frequency = self.tasks[user_task_input]

            self.tasks.pop(user_task_input)
            self.tasks[user_new_name_input] = task_frequency

            print()
            print_bar()
            print_line("Task Name Updated")
            print_bar()
            stall()
        else:
            print()
            print_bar()
            print_line("Please Choose One Of The Following Task Frequencies")
            print_bar()
            print()
            print_bar()
            print_line("[1] Daily")
            print_line("[2] Weekly")
            print_line("[3] Biweekly")
            print_line("[4] Monthly")
            print_bar()
            print()

            user_frequency_input = input()
            frequency_choice = int(user_frequency_input)

            self.tasks[user_task_input] = frequency_choice

            print()
            print_bar()
            print_line("Task Frequency Updated")
            print_bar()
            stall()

    def delete_task(self):
        print()
        print_bar()
        print_line("Please Enter Name Of Task To Delete")
        print_bar()

        counter = 1

        for key in self.tasks:
            task_string = f'[{counter}] {key}'
            print_line(task_string)
            print_bar()
            counter += 1

        print()

        user_task_input = input()

        self.tasks.pop(user_task_input)

        print()
        print_bar()
        print_line("Task Successfully Deleted")
        print_bar()
        stall()

# Functions

def print_bar():
    print(64*"=")

def print_line(statement):
    prepend = "| "
    append_length = 63 - (len(statement) + len(prepend))
    append = append_length * " " + "|"
    print(prepend, statement, append)

def stall():
    print()
    print("Please Enter Any Key To Continue ...")
    input()
    print()

# Main

def main():
    
    task_manager = TaskManager()

    task_manager.import_save()

    flag = True

    while(flag):

        flag = task_manager.run()

        task_manager.save_data()

    

if __name__ == '__main__':
    main()