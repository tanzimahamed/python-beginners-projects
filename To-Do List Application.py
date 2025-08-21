# To-Do List Application
# This program allows the user to add, view, and delete tasks.

tasks = []                                    # List to store tasks

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(" Task Added!")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):      # Display task with index
            print(f"{i}. {t}")
    elif choice == "3":
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(tasks):
            tasks.pop(task_no - 1)            # Remove task by index
            print(" Task Deleted")
        else:
            print(" Invalid Task Number")
    elif choice == "4":
        print("Goodbye ")
        break
    else:
        print(" Invalid Option")
