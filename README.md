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