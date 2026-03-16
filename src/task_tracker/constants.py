# Aquí guardamos colores, rutas y de mas datos para evitar errores de codigo

# Códigos de escape ANSI para colores
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Configuraciones de la App
DB_FILE = "tasks.json"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Estados válidos (para evitar errores de dedo en el código)
STATUS_TODO = "todo"
STATUS_IN_PROGRESS = "in-progress"
STATUS_DONE = "done"

# Campos de tarea
ID = "id"
DESCRIPTION = "description"
STATUS = "status"
CREATED_AT = "created_at"
UPDATE_AT = "updated_at"

# Comando del CRUD
ADD = "add"
LIST = "list"
UPDATE = "update"
DELETE = "delete"
