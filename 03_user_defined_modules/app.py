import todo
# print(dir(todo))
print("==== TO-DO LIST ====")
while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        print(todo.add_task(task))

    elif choice == "2":
        todo.show_tasks()

    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        print(todo.remove_task(num))

    elif choice == "4":
        break

    else:
        print("Invalid choice")