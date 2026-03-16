import argparse
from .manager import TaskManager
# from . import __version__

# Códigos de color ANSI
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Punto de entrada (Argparse)
def main():
    manager = TaskManager()
    parser = argparse.ArgumentParser(description="A simple task CLI in Python")
    subparsers = parser.add_subparsers(dest="command")

    # Comando para agregar una tarea
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Description of the task")
    
    # Comando para listar tareas
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--status", type=str, choices=["todo", "in-progress", "done"], help="Filter tasks by status")

    # Comando para actualizar una tarea
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", type=int, help="ID of the task to update")
    update_parser.add_argument("--description", type=str, help="New description for the task")
    # update_parser.add_argument("--status", type=str, choices=["todo", "in-progress", "done"], help="New status for the task")

    # Comando para eliminar una tarea
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if args.command == "add":
        if not args.description.strip():
            print("Description is required to add a task.")
            return
        task_id = manager.add_task(args.description)
        print(f"{GREEN}✓{RESET} {BOLD}Task added successfully{RESET} (ID: {task_id})")
    elif args.command == "list":
        tasks = manager.list_tasks()
        if len(tasks) > 0:
            print(f"{BOLD}ID - Description: (Status){RESET}")
        else:
            print("No tasks found.")
        for task in manager.list_tasks():
            print(f"{task['id']} - {task['description']}: ({task['status']})")
    elif args.command == "update":
        success = manager.update_task(
            task_id=args.id,
            description=args.description,
            status=args.status
        )
        if  success:
            print(f"{GREEN}✓{RESET} {BOLD}Task updated successfully{RESET} (ID: {args.id})")
        else:
            print(f"{RED}✗{RESET} {BOLD}Error: Task with ID {args.id} not found.{RESET}") 
    elif args.command == "delete":
        success = manager.delete_task(args.id)
        if success:
            print(f"{GREEN}✓{RESET} {BOLD}Task deleted successfully{RESET} (ID: {args.id})")
        else:
            print(f"{RED}✗{RESET} {BOLD}Error: Task with ID {args.id} not found.{RESET}")
    else:
        print("Invalid command. Use 'add', 'list', or 'update'.")

if __name__ == "__main__":
    main()
