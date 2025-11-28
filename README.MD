# 📚 Sistema de Gestión de Notas Académicas

Este proyecto es una aplicación de consola desarrollada en Python 3 que simula un sistema básico de gestión académica. Fue creado como parte de un ejercicio para aplicar conceptos fundamentales de **Control de Flujo (Ciclos)**, **Organización de Datos (Listas y Diccionarios)** y **Modularidad (Funciones)**, siguiendo un flujo de trabajo profesional con **Git Flow**.

---

## 🎯 Requisitos Funcionales Implementados

El sistema permite a los usuarios interactuar a través de un menú, implementando las siguientes acciones a través de funciones separadas:

1.  **Registrar Estudiante:** Crea un nuevo registro usando un **Diccionario**.
2.  **Registrar Nota:** Agrega valores a la **Lista** de notas dentro del Diccionario del estudiante.
3.  **Ver Promedio y Estado:** Calcula la media de las notas y determina si el estudiante está "APROBADO" o "REPROBADO".
4.  **Salir:** Utiliza un ciclo `while` para mantener la aplicación activa hasta que el usuario decida salir.

---

## 🌳 Propósito del Versionamiento (Git Branching)

El proyecto se desarrolló utilizando un flujo de trabajo de ramas para separar las responsabilidades y asegurar un historial de commits limpio, demostrando la capacidad de trabajar con diferentes funcionalidades de forma aislada.

| Rama | Propósito Principal | Funcionalidades | Estado |
| :--- | :--- | :--- | :--- |
| **`main`** | **Producción/Estable** | Contiene la versión final, estable y funcional del sistema. | ✅ Fusionada |
| **`feature/notas`** | **Registro de Datos** | Desarrollo de las funciones `registrar_estudiante` y `registrar_nota`. | ✅ Fusionada |
| **`feature/aprueba`** | **Lógica de Negocio** | Desarrollo de la función `ver_promedio_y_estado` (cálculo y condición). | ✅ Fusionada |
| **`dev`**| Rama de proteccion del main `Proteccion del main`. | ✅ Proteccion |

---

## 🚀 Cómo Ejecutar el Proyecto

1.  **Clonar el repositorio:**
    ```bash
    git clone [TU_URL_DEL_REPOSITORIO]
    cd sistema-gestion-notas-py 
    ```
2.  **Ejecutar la aplicación:**
    ```bash
    python main.py
    ```