def main():
    todo_dict = {}

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_dict[len(todo_dict) + 1] = {"task": task, "completed": False}
            print("Task added successfully!")

        elif choice == "2":
            print("\n===== To-Do List =====")
            if not todo_dict:
                print("No tasks in the list.")
            else:
                for task_num, task_info in todo_dict.items():
                    status = "Completed" if task_info["completed"] else "Pending"
                    print(f"{task_num}. [{status}] {task_info['task']}")

        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: "))
            if task_number in todo_dict:
                todo_dict[task_number]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
