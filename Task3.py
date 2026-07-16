
tasks = []
task_id_counter = 1

def create_task():
    global task_id_counter
    title = input("Enter task title: ")
    desc = input("Enter task description: ")
    
    new_task = {
        "id": task_id_counter,
        "title": title,
        "description": desc
    }
    tasks.append(new_task)
    task_id_counter += 1
    print("Task added successfully!\n")

def read_tasks():
    if not tasks:
        print("No tasks found.\n")
        return
    print("\n--- Your Tasks ---")
    for task in tasks:
        print(f"ID: {task['id']} | Title: {task['title']} | Desc: {task['description']}")
    print("\n")

def update_task():
    read_tasks() 
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        for task in tasks:
            if task['id'] == task_id:
                task['title'] = input("Enter new title: ")
                task['description'] = input("Enter new description: ")
                print("Task updated successfully!\n")
                return
        print("Task ID not found.\n")
    except ValueError:
        print("Invalid ID format.\n")

def delete_task():
    read_tasks()
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
        for i, task in enumerate(tasks):
            if task['id'] == task_id:
                tasks.pop(i)
                print("Task deleted successfully!\n")
                return
        print("Task ID not found.\n")
    except ValueError:
        print("Invalid ID format.\n")

def menu():
    while True:
        print("===== CRUD MENU =====")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()