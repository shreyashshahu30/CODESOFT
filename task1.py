todo_list = []

def add_task():
    task = input("\nEnter a new task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not todo_list:
        print("\n📭 No tasks in your to-do list.")
        return
    print("\n📝 Your To-Do List:")
    for i, t in enumerate(todo_list, start=1):
        status = "✅" if t["completed"] else "❌"
        print(f"{i}. {t['task']} [{status}]")

def mark_completed():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to mark as completed: "))
        if 1 <= task_no <= len(todo_list):
            todo_list[task_no - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def update_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to update: "))
        if 1 <= task_no <= len(todo_list):
            new_task = input("Enter the updated task: ")
            todo_list[task_no - 1]["task"] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to delete: "))
        if 1 <= task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Task '{removed['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n====== 📌 TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            update_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 6.")

# Run the To-Do List app
main()

