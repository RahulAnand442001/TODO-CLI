from sys import argv
from datetime import datetime

DATE_iso_8601_format = datetime.now().isoformat()[0:10]

usage = '''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''


def todo_count():
    """ This method returns the number of TODOs in the file.
        Parameters Accepted : 0. Return 0 if empty else return
        Length of TODOs list"""
    count = 0
    try:
        with open('todo.txt') as todo_file:
            todo_list = todo_file.readlines()
    except FileNotFoundError:
        pass
    else:
        count = len(todo_list)
    return count


def todo_done_count():
    """ This method returns the number of TODOs completed in the file.
            Parameters Accepted : 0. Return 0 if empty else return
            Length of TODOs completed list"""
    done_count = 0
    try:
        with open('done.txt') as done_file:
            done_list = done_file.readlines()
    except FileNotFoundError:
        pass
    else:
        done_count = len(done_list)
    return done_count


def _report():
    """ This method print the number of pending TODOs in
    TODO list and completed TODOs from DONE list"""
    print(f"{DATE_iso_8601_format} Pending : {todo_count()} Completed : {todo_done_count()}")


def _ls():
    """ This method prints all your TODOs"""
    with open('todo.txt') as todo_file:
        todo_list = todo_file.readlines()
        reverse_todo_list = [todo.split('\n')[0] for todo in todo_list[::-1]]
        count = todo_count()
        for todo in reverse_todo_list:
            print(f'[{count}] {todo}')
            count -= 1


def _add(args):
    """ This method adds a new TODO task to the todo list.
        Parameters: argument passed (todo command with todo-title)."""
    todo_title = args
    with open('todo.txt', mode='a') as todo_file:
        todo_file.write(f"{todo_title}\n")
    print(f'Added todo: "{todo_title}"')


def _del(args):
    """ This method delete a specific TODO from todo list.
            Parameters Accepted : argument passed (todo command and todo number) """
    try:
        with open('todo.txt') as todo_file:
            todo_list = todo_file.readlines()
    except FileNotFoundError:
        pass
    else:
        todo_index = int(args)
        if len(todo_list) == 0:
            print(f"Error: todo #{todo_index} does not exist. Nothing deleted.")
            return
        else:
            with open('todo.txt', mode='w') as file:
                if todo_index <= 0 or todo_index > len(todo_list):
                    print(f"Error: todo #{todo_index} does not exist. Nothing deleted.")
                    return
                else:
                    for index in range(0, len(todo_list)):
                        if todo_index != index + 1:
                            file.write(todo_list[index])
                    print(f"Deleted todo #{todo_index}")


def _done(args):
    """ This method marks a TODO as complete and transfer to todo completed list.
             Parameters: argument passed (todo command with todo-number)."""
    todo_index = args
    with open('todo.txt') as todo_file:
        todo_task_list = todo_file.readlines()
    with open('todo.txt', mode='w') as file:
        for index in range(0, len(todo_task_list)):
            if todo_index != index + 1:
                file.write(todo_task_list[index])
            else:
                completed_todo = todo_task_list[index]
                with open('done.txt', mode='a') as done_file:
                    done_file.write(f"x {DATE_iso_8601_format} {completed_todo}")
                print(f"Marked todo #{todo_index} as done.")


def main():
    if len(argv) == 1 and argv[0] == 'todo.py':
        print(usage)
    elif len(argv) == 2 and argv[0] == 'todo.py' and argv[1] == 'help':
        print(usage)
    elif len(argv) == 2 and argv[0] == 'todo.py' and argv[1] == 'report':
        _report()
    elif len(argv) == 2 and argv[0] == 'todo.py' and argv[1] == 'ls':
        if todo_count() == 0:
            print("There are no pending todos!")
        else:
            _ls()
    elif len(argv) == 2 and argv[1] == 'add':
        print("Error: Missing todo string. Nothing added!")
    elif len(argv) == 3 and argv[0] == 'todo.py' and argv[1] == 'add':
        _add(argv[2])
    elif len(argv) == 2 and argv[0] == 'todo.py' and argv[1] == 'del':
        print("Error: Missing NUMBER for deleting todo.")
    elif len(argv) == 3 and argv[0] == 'todo.py' and argv[1] == 'del':
        _del(argv[2])
    elif len(argv) == 2 and argv[0] == 'todo.py' and argv[1] == 'done':
        print("Error: Missing NUMBER for marking todo as done.")
    elif len(argv) == 3 and argv[0] == 'todo.py' and argv[1] == 'done':
        todo_index = int(argv[2])
        if todo_index <= 0 or todo_index > todo_count():
            print(f"Error: todo #{todo_index} does not exist.")
        else:
            _done(todo_index)


# <--------- TODO entry point ---------->
main()
