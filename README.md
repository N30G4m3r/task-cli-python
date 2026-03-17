# 📝 Task Tracker CLI

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Una herramienta de línea de comandos (CLI) potente y ligera para la gestión de tareas. Este proyecto ha sido desarrollado como una solución técnica al reto de **roadmap.sh**, aplicando principios de **Clean Code**, **Arquitectura en Capas** y **Test-Driven Development (TDD)**.

---

## ✨ Características Principales

* ✅ **Cero Dependencias:** Construido exclusivamente con la biblioteca estándar de Python.
* 🎨 **UX Colorida:** Retroalimentación visual en terminal mediante códigos ANSI.
* 🛡️ **Resiliencia:** Manejo robusto de archivos JSON corruptos o inexistentes.
* 📅 **Trazabilidad:** Registro automático de marcas de tiempo (`createdAt`, `updatedAt`).
* 🧪 **Test Coverage:** Suite completa de pruebas unitarias e integración.

---

## 🛠️ Estructura del Proyecto



El proyecto sigue una separación clara de responsabilidades:

| Módulo | Responsabilidad |
| :--- | :--- |
| `main.py` | Punto de entrada y configuración de `argparse`. |
| `commands.py` | Handlers de la CLI y formateo de mensajes (Output). |
| `manager.py` | Lógica de negocio y reglas de validación. |
| `storage.py` | Capa de persistencia (Lectura/Escritura JSON). |
| `constants.py` | Configuración global, colores y estados. |

---

## 🚀 Instalación y Uso

### Requisitos
* Python 3.8 o superior.
* [uv](https://github.com/astral-sh/uv) (recomendado) o `pip`.

### Configuración
```bash
# Clonar el repositorio
git clone [https://github.com/tu-usuario/task-tracker-cli.git](https://github.com/tu-usuario/task-tracker-cli.git)
cd task-tracker-cli

# Ejecutar sin instalar (usando el módulo)
python -m src.task_tracker.main --help
```
---

## 🧪 Testing Profesional

La calidad del software se garantiza mediante una suite de pruebas exhaustiva utilizando el módulo nativo `unittest`.

### Niveles de Prueba:
1.  **Unit Tests (`Manager`):** Validación de creación de tareas, edición y reglas de autoincremento.
2.  **Storage Tests:** Pruebas de resiliencia ante archivos JSON corruptos, vacíos o inexistentes.
3.  **Integration Tests:** Simulación de flujos completos de un usuario real (Añadir -> Listar -> Actualizar -> Borrar).
4.  **Date Validation:** Verificación de que `updatedAt` cambie tras una edición mientras `createdAt` permanece inmutable.

**Para ejecutar los tests:**
```bash
python -m unittest discover tests
```
---

## 📐 Decisiones Técnicas

* **Sin Dependencias:** Todo el proyecto funciona exclusivamente con la librería estándar de Python para asegurar la máxima portabilidad y ligereza.
* **Validación de Entradas:** Se implementó una lógica de limpieza (`strip()`) para evitar la creación de tareas con espacios en blanco o descripciones vacías, devolviendo `False` o `None` según corresponda.
* **Manejo Graceful de Errores:** En lugar de lanzar *tracebacks* técnicos de Python, el sistema captura excepciones de lectura (como archivos corruptos) y muestra mensajes amigables y coloridos al usuario.
* **Inyección de Dependencias Ligera:** Las funciones de carga y guardado aceptan rutas de archivos opcionales. Esto permite que los tests utilicen archivos temporales sin riesgo de modificar o borrar tus tareas reales.
* **Patrón Dispatcher:** Se sustituyó la cadena de `if/elif` en el `main` por un diccionario de comandos, lo que facilita añadir nuevas funcionalidades sin ensuciar el flujo principal.---

---

## 🤖 Reconocimientos y Herramientas

Este proyecto fue desarrollado con el apoyo de **Gemini (Google AI)** para:
* El diseño de la arquitectura modular y estructura de archivos.
* La implementación de la suite de pruebas unitarias e integración.
* La redacción y formateo profesional de esta documentación.

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT**. Esto significa que puedes usar, copiar y modificar el código libremente, siempre que mantengas la nota de derechos de autor. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 🤝 Contribuciones

¡Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar increíble para aprender, inspirar y crear! Cualquier aporte que hagas será **muy apreciado**.

### Cómo colaborar:
1. **Haz un Fork** del proyecto.
2. **Crea una Rama** para tu funcionalidad (`git checkout -b feature/NuevaFuncionalidad`).
3. **Realiza tus cambios** y asegúrate de que todos los tests sigan pasando (`python -m unittest discover tests`).
4. **Haz un Commit** de tus cambios (`git commit -m 'feat: agrega una nueva funcionalidad'`).
5. **Haz un Push** a la rama (`git push origin feature/NuevaFuncionalidad`).
6. **Abre un Pull Request**.

### Ideas para contribuir:
* Agregar una opción para exportar tareas a formato CSV o PDF.
* Implementar prioridades (Baja, Media, Alta) con colores distintos.
* Crear una funcionalidad de "búsqueda" por palabra clave en la descripción.
* Traducir los mensajes de la interfaz a otros idiomas.

---

### 👨‍💻 Autor
Desarrollado por **[Leonardo Montilla]** como parte del reto de proyectos de [roadmap.sh](https://roadmap.sh/projects/task-tracker).

> "La simplicidad es la máxima sofisticación." — Leonardo da Vinci

