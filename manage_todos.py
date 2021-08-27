import protos.todos_pb2 as todosproto
from google.protobuf.timestamp_pb2 import Timestamp
import time
import random

def main():
    todo_list = get_todos()
    initialize_todo(todo_list.todos.add(), *collect_user_input())
    write_todos(todo_list)

def collect_user_input() -> tuple[str, int, int]:

    description = input('Please enter a todo description: ')
    
    while True:
        try:
            days_due_from_now = int(input('How many days do you need for this todo? Please provide an integer: '))
            due_date = int(time.time() + (24 * 60 * days_due_from_now))
            break
        except TypeError:
            continue

    while True:
        try:
            priority = int(input('What is the priority level of this todo? '
                             'Enter one of the following numbers:\n\n'
                             '1: High\n2: Medium\n3: Low\n\nYour choice:'))
            break
        except TypeError:
            continue

    return description, due_date, priority

def initialize_todo(todo, description='', due_date=0, priority=3) -> None:

    todo.id = random.randint(0, 1000000000)
    todo.description = description
    todo.due_date = Timestamp(seconds=due_date)

    if priority == 1:
        todo.priority = todosproto.TodoPriority.HIGH
    elif priority == 2:
        todo.priority = todosproto.TodoPriority.MEDIUM
    elif priority == 3:
        todo.priority = todosproto.TodoPriority.LOW

def get_todos() -> todosproto.Todos:

    todo_list = todosproto.Todos()
    with open('todos.txt', 'rb') as f:
        todo_list.ParseFromString(f.read())
    return todo_list

def write_todos(todos: todosproto.Todos) -> None:

    with open('todos.txt', 'w') as f:
        f.write(todos)

if __name__ == '__main__':
    main()