from .manager import TaskManager
from .constants import GREEN, RED, YELLOW, BOLD, RESET, STATUS_IN_PROGRESS, STATUS_DONE

# Lógica de la interfaz (Mensajes, colores, prints)
# Inicializamos el TaskManager para usarlo en los comandos
manager = TaskManager()


# Función para manejar el comando "add" y agregar una nueva tarea usando el TaskManager
def run_add(args):
    # Verificamos que se haya proporcionado una descripción para la tarea, ya que es un argumento requerido
    # Si no se proporciona una descripción, mostramos un mensaje de error y salimos de la función
    if not args.description:
        print(
            f"{RED}✗{RESET} {BOLD}Error: Description is required to add a task.{RESET}"
        )
        return

    # Agregamos la tarea usando el método add_task del TaskManager, que retorna el ID de la nueva tarea
    task_id = manager.add_task(args.description)

    # Si el ID retornado es None o falso, significa que hubo un error al agregar la tarea, por lo que mostramos un mensaje de error
    if not task_id:
        print(f"{RED}✗{RESET} {BOLD}Error: Failed to add task.{RESET}")
        return

    # Si la tarea se agregó exitosamente, mostramos un mensaje de éxito con el ID de la nueva tarea
    print(f"{GREEN}✓{RESET} {BOLD}Task added successfully{RESET} (ID: {task_id})")

    # Retornamos el ID de la nueva tarea para confirmación o uso posterior
    return task_id


# Función para manejar el comando "list" y listar las tareas usando el TaskManager, con opción de filtrar por estado
def run_list(args):
    # Obtenemos la lista de tareas usando el método list_tasks del TaskManager, pasando el estado como argumento para filtrar si se especifica
    tasks = manager.list_tasks(args.status)
    task_count = len(tasks)

    # Mostramos un mensaje con el número total de tareas listadas, usando colores para resaltar la información
    print(f"{YELLOW}{BOLD}Listing tasks{RESET} ({task_count} total){RESET}")
    print(f"{YELLOW}-----------------------{RESET}")

    # Si no hay tareas, mostramos un mensaje indicando que no se encontraron tareas, de lo contrario mostramos la lista de tareas con su ID, descripción y estado
    if task_count == 0:
        print(f"{YELLOW}No tasks found.{RESET}")
        return

    # Si hay tareas, mostramos un encabezado para la lista de tareas y luego iteramos sobre cada tarea para mostrar su ID, descripción y estado formateados
    print(f"{BOLD}ID - Description: (Status){RESET}")
    print(f"{BOLD}-----------------------{RESET}")

    # Iteramos sobre cada tarea en la lista de tareas y mostramos su ID, descripción y estado formateados
    for task in tasks:
        print(f"{task['id']} - {task['description']}: ({task['status']})")

    # Retornamos la lista de tareas para uso posterior o confirmación
    return tasks


# Función para manejar el comando "update" y actualizar una tarea existente usando el TaskManager, con opción de actualizar la descripción y/o el estado
def run_update(args):
    # Verificamos que se haya proporcionado un ID para la tarea a actualizar, ya que es un argumento requerido
    # Si no se proporciona un ID, mostramos un mensaje de error y salimos de la función
    if not args.id:
        print(f"{RED}✗{RESET} {BOLD}Error: ID is required to update a task.{RESET}")
        return

    # Verificamos que se haya proporcionado al menos una nueva descripción o un nuevo estado para actualizar, ya que ambos son opcionales pero al menos uno debe ser proporcionado
    # Si no se proporciona ni una nueva descripción ni un nuevo estado, mostramos un mensaje de error y salimos de la función
    if not args.description and not args.status:
        print(
            f"{RED}✗{RESET} {BOLD}Error: At least a new description or a new status is required to update a task.{RESET}"
        )
        return

    # Intentamos actualizar la tarea usando el método update_task del TaskManager, pasando el ID de la tarea a actualizar, la nueva descripción y el nuevo estado como argumentos
    success = manager.update_task(
        args.id, description=args.description, status=args.status
    )

    # Si la actualización no fue exitosa (por ejemplo, si no se encontró la tarea con el ID especificado), mostramos un mensaje de error indicando que no se pudo actualizar la tarea
    if not success:
        print(
            f"{RED}✗{RESET} {BOLD}Error: Failed to update task. Check if the ID exists and if you provided a new description or status.{RESET}"
        )
        return

    # Si la tarea se actualizó exitosamente, mostramos un mensaje de éxito con el ID de la tarea actualizada
    print(f"{GREEN}✓{RESET} {BOLD}Task updated successfully{RESET} (ID: {args.id})")
    return True


# Función para manejar el comando "delete" y eliminar una tarea usando el TaskManager, dado su ID
def run_delete(args):
    # Verificamos que se haya proporcionado un ID para la tarea a eliminar, ya que es un argumento requerido
    # Si no se proporciona un ID, mostramos un mensaje de error y salimos de la función
    if not args.id:
        print(f"{RED}✗{RESET} {BOLD}Error: ID is required to delete a task.{RESET}")
        return

    # Intentamos eliminar la tarea usando el método delete_task del TaskManager, pasando el ID de la tarea a eliminar como argumento
    success = manager.delete_task(args.id)

    # Si la eliminación no fue exitosa (por ejemplo, si no se encontró la tarea con el ID especificado), mostramos un mensaje de error indicando que no se pudo eliminar la tarea
    if not success:
        print(
            f"{RED}✗{RESET} {BOLD}Error: Failed to delete task. Check if the ID exists.{RESET}"
        )
        return

    # Si la tarea se eliminó exitosamente, mostramos un mensaje de éxito con el ID de la tarea eliminada
    print(f"{GREEN}✓{RESET} {BOLD}Task deleted successfully{RESET} (ID: {args.id})")
    return True


# Función para manejar el comando "in-progress" y marcar una tarea como en progreso usando el TaskManager, dado su ID
def run_in_progress(args):
    # Verificamos que se haya proporcionado un ID para la tarea a marcar como en progreso, ya que es un argumento requerido
    # Si no se proporciona un ID, mostramos un mensaje de error y salimos de la función
    if not args.id:
        print(
            f"{RED}✗{RESET} {BOLD}Error: ID is required to mark a task as in-progress.{RESET}"
        )
        return

    # Intentamos actualizar el estado de la tarea a "in-progress" usando el método update_task del TaskManager, pasando el ID de la tarea a actualizar y el nuevo estado como argumentos
    success = manager.update_task(args.id, status=STATUS_IN_PROGRESS)

    # Si la actualización no fue exitosa (por ejemplo, si no se encontró la tarea con el ID especificado), mostramos un mensaje de error indicando que no se pudo marcar la tarea como en progreso
    if not success:
        print(
            f"{RED}✗{RESET} {BOLD}Error: Failed to mark task as in-progress. Check if the ID exists.{RESET}"
        )
        return

    # Si la tarea se marcó como en progreso exitosamente, mostramos un mensaje de éxito con el ID de la tarea actualizada
    print(
        f"{GREEN}✓{RESET} {BOLD}Task marked as in-progress successfully{RESET} (ID: {args.id})"
    )
    return True


# Función para manejar el comando "done" y marcar una tarea como hecha usando el TaskManager, dado su ID
def run_done(args):
    # Verificamos que se haya proporcionado un ID para la tarea a marcar como hecha, ya que es un argumento requerido
    # Si no se proporciona un ID, mostramos un mensaje de error y salimos de la función
    if not args.id:
        print(
            f"{RED}✗{RESET} {BOLD}Error: ID is required to mark a task as done.{RESET}"
        )
        return

    # Intentamos actualizar el estado de la tarea a "done" usando el método update_task del TaskManager, pasando el ID de la tarea a actualizar y el nuevo estado como argumentos
    success = manager.update_task(args.id, status=STATUS_DONE)

    # Si la actualización no fue exitosa (por ejemplo, si no se encontró la tarea con el ID especificado), mostramos un mensaje de error indicando que no se pudo marcar la tarea como hecha
    if not success:
        print(
            f"{RED}✗{RESET} {BOLD}Error: Failed to mark task as done. Check if the ID exists.{RESET}"
        )
        return

    # Si la tarea se marcó como hecha exitosamente, mostramos un mensaje de éxito con el ID de la tarea actualizada
    print(
        f"{GREEN}✓{RESET} {BOLD}Task marked as done successfully{RESET} (ID: {args.id})"
    )
    return True
