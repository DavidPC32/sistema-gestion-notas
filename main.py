ESTUDIANTES_DB = [] 

def buscar_estudiante(nombre_buscado):
    """
    Función auxiliar (reutilizable) para encontrar un estudiante.
    Utiliza un ciclo 'for' para recorrer la lista de diccionarios.
    """
    for estudiante in ESTUDIANTES_DB:
        if estudiante['nombre'].lower() == nombre_buscado.lower():
            return estudiante
    return None # Retorna None si el ciclo 'for' termina sin encontrar nada

def registrar_estudiante():
    """Registra un nuevo estudiante con su diccionario base."""
    nombre = input("Ingrese nombre del estudiante: ")
    
    if buscar_estudiante(nombre):
        print("Error: Este estudiante ya está registrado.")
        return

    nuevo_estudiante = {
        "nombre": nombre, 
        "notas": [],       # Lista vacía para agregar notas después
        "promedio": 0.0    # Valor inicial (será calculado en otra rama)
    }
    ESTUDIANTES_DB.append(nuevo_estudiante)
    print(f"✅ Estudiante '{nombre}' registrado con éxito.")

def registrar_nota():
    """Busca un estudiante y agrega una nota a su lista interna."""
    nombre = input("Ingrese nombre del estudiante para registrar nota: ")
    estudiante = buscar_estudiante(nombre)
    
    if estudiante:
        try:
            nota = float(input(f"Ingrese nota para {nombre} (1.0 - 5.0): "))
            
            if 1.0 <= nota <= 5.0:
                estudiante['notas'].append(nota)
                print(f"✅ Nota {nota:.1f} registrada.")
            else:
                print("Error: La nota debe estar entre 1.0 y 5.0.")
        except ValueError:
            print("Error: La nota debe ser un número válido.")
    else:
        print("Estudiante no encontrado.")
        
def ver_promedio_y_estado():
    print("Funcionalidad de cálculo de promedio pendiente (se implementará en feature/aprueba).")
    # ... (El código de esta función será agregado en la siguiente rama) ...

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE NOTAS ---")
    print("1. Registrar Estudiante")
    print("2. Registrar Nota")
    print("3. Ver Promedio y Estado")
    print("4. Salir")
    print("------------------------------------")

def main():
    while True: # El ciclo while que mantiene la aplicación viva
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            registrar_estudiante() # Llama a la función de la rama feature/notas
        elif opcion == "2":
            registrar_nota()       # Llama a la función de la rama feature/notas
        elif opcion == "3":
            ver_promedio_y_estado()
        elif opcion == "4":
            print("👋 Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()