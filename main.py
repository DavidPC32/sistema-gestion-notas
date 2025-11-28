# Estructura de datos global: Lista de diccionarios
# Ejemplo: [{'nombre': 'Ana', 'notas': [4.5, 3.2], 'promedio': 3.85}]
ESTUDIANTES_DB = []

def buscar_estudiante(nombre_buscado):
    """Busca y devuelve el diccionario del estudiante por nombre."""
    for estudiante in ESTUDIANTES_DB:

        if estudiante['nombre'].lower() == nombre_buscado.lower():
            return estudiante
    return None

def registrar_estudiante():
    """Registra un nuevo estudiante con su diccionario base."""
    nombre = input("Ingrese nombre del estudiante: ")
    if buscar_estudiante(nombre):
        print("❌ Error: Este estudiante ya está registrado.")
        return
    nuevo_estudiante = {
        "nombre": nombre, 
        "notas": [],
        "promedio": 0.0
    }
    ESTUDIANTES_DB.append(nuevo_estudiante)
    print(f"✅ Estudiante '{nombre}' registrado con éxito.")

def registrar_nota():
    """Busca un estudiante y agrega una nota a su lista."""
    nombre = input("Ingrese nombre del estudiante para registrar nota: ")
    estudiante = buscar_estudiante(nombre)
    if estudiante:
        try:

            nota = float(input(f"Ingrese nota para {nombre} (1.0 - 5.0): "))
            if 1.0 <= nota <= 5.0:
                estudiante['notas'].append(nota)
                print(f"✅ Nota {nota:.1f} registrada.")
            else:
                print("❌ Error: La nota debe estar entre 1.0 y 5.0.")
        except ValueError:
            print("❌ Error: La nota debe ser un número.")
    else:
        print("❌ Estudiante no encontrado.")

def ver_promedio_y_estado():
    """Calcula el promedio, actualiza el estado y lo muestra."""
    nombre = input("Ingrese nombre del estudiante para ver reporte: ")
    estudiante = buscar_estudiante(nombre)

    if estudiante:
        notas = estudiante['notas']
        
        if len(notas) == 0:
            print("⚠️ El estudiante no tiene notas registradas.")
            return

        # Cálculo de Promedio
        suma_notas = sum(notas)
        promedio = suma_notas / len(notas)
        
        estudiante['promedio'] = promedio 
        
        # Lógica de aprobación (usando 3.0 como mínimo)
        estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
        
        print("\n--- REPORTE ACADÉMICO ---")
        print(f"Estudiante: {estudiante['nombre']}")
        print(f"Notas registradas: {notas}")
        print(f"Promedio Final: {promedio:.2f}")
        print(f"Estado: {estado}")
    else:
        print("❌ Estudiante no encontrado.")


def mostrar_menu():
    """Imprime el menú interactivo."""
    print("\n--- SISTEMA DE GESTIÓN DE NOTAS ---")
    print("1. Registrar Estudiante")
    print("2. Registrar Nota")
    print("3. Ver Promedio y Estado")
    print("4. Salir")
    print("------------------------------------")


def main():
    """Función principal que ejecuta el ciclo while."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            registrar_nota()
        elif opcion == "3":
            ver_promedio_y_estado()
        elif opcion == "4":
            print("👋 Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()