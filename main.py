while True:
    user_action = (input("Type add, show, edit, complete or exit: ").strip())
    if 'add' in user_action:
        todo = user_action[4:]
        with open("todos.txt", 'a+') as file:
            file.writelines(todo)

    elif 'show' in user_action:
        with open("todos.txt", 'r') as file:
            # Index starts at 1 when using notation (file, 1)
            for index, item in enumerate(file, 1):
                print(f"{index}-{item.rstrip()}")

    elif 'edit' in user_action:
        num = int(user_action[5:])
        todo = (input("What would you like to change it to? ") + "\n")
        with open("todos.txt", 'r+') as file:
            todos = file.readlines()
            todos[num] = todo
            file.seek(0)
            file.writelines(todos)

    elif 'complete' in user_action:
        num = int(user_action[9:])

        with open("todos.txt", 'r+') as file:
            todos = file.readlines()
            todos.pop(num)
            # Seek moves the cursor back to the start of the file then truncate removes all the lines till the end
            file.seek(0)
            file.truncate()
            # The updated todos in copied into the existing file
            file.writelines(todos)

    elif 'exit' in user_action:
        break
    else:
        print("You haven't entered a valid command")

print("Bye!")