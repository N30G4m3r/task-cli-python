import argparse
from . import commands
from .constants import (
    COMMAND,
    ADD,
    LIST,
    UPDATE,
    DELETE,
    ID,
    DESCRIPTION,
    STATUS,
    STATUS_TODO,
    STATUS_IN_PROGRESS,
    STATUS_DONE,
)


# Punto de entrada (Argparse)
def main():
    parser = argparse.ArgumentParser(description="A simple task CLI in Python")
    subparsers = parser.add_subparsers(dest=COMMAND)

    # Comando para agregar una tarea
    add_parser = subparsers.add_parser(ADD, help="Add a new task")
    # El argumento "description" es un argumento posicional requerido para el comando "add", que especifica la descripción de la tarea a agregar
    add_parser.add_argument(DESCRIPTION, type=str, help="Description of the task")

    # Comando para listar tareas
    list_parser = subparsers.add_parser(LIST, help="List all tasks")
    # El argumento "status" es un argumento opcional para el comando "list", que permite filtrar las tareas por su estado (todo, in-progress, done)
    list_parser.add_argument(
        STATUS,
        nargs="?",
        choices=[STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE],
        help="Filter tasks by status",
    )

    # Comando para actualizar una tarea
    update_parser = subparsers.add_parser(UPDATE, help="Update an existing task")
    update_parser.add_argument(
        ID, type=int, help="ID of the task to update"
    )  # required positional argument to specify which task to update
    update_parser.add_argument(
        f"--{DESCRIPTION}", type=str, help="New description for the task"
    )  # optional argument to update the description
    update_parser.add_argument(
        f"--{STATUS}",
        type=str,
        choices=[STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE],
        help="New status for the task",
    )

    # Comando para eliminar una tarea
    delete_parser = subparsers.add_parser(DELETE, help="Delete a task")
    delete_parser.add_argument(
        ID, type=int, help="ID of the task to delete"
    )  # required positional argument to specify which task to delete

    # Comando para marca una tarea en progreso
    in_progress_parser = subparsers.add_parser(
        STATUS_IN_PROGRESS, help="Mark a task as in-progress"
    )
    in_progress_parser.add_argument(
        ID, type=int, help="ID of the task to mark as in-progress"
    )  # required positional argument to specify which task to mark

    # Comando para marcar una tarea como hecha
    done_parser = subparsers.add_parser(STATUS_DONE, help="Mark a task as done")
    done_parser.add_argument(
        ID, type=int, help="ID of the task to mark as done"
    )  # required positional argument to specify which task to mark

    args = parser.parse_args()

    # Mapa de Comandos
    command_map = {
        ADD: commands.run_add,
        LIST: commands.run_list,
        UPDATE: commands.run_update,
        DELETE: commands.run_delete,
        STATUS_IN_PROGRESS: commands.run_in_progress,
        STATUS_DONE: commands.run_done,
    }

    #
    handler = command_map.get(args.command)

    if handler:
        handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
