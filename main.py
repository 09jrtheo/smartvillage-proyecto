# main.py - Proyecto SmartVillage
# DÍA 2: Registro mejorado y listado de habitantes

import os
from collections import Counter

# === LISTA PARA GUARDAR HABITANTES ===
habitantes = []

def limpiar_pantalla():
    """Limpia la consola (opcional)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print(" 🌱 SMARTVILLAGE - Pueblo Conectado 🌱".center(50))
    print("="*50)
    print("1. Registrar nuevo habitante")
    print("2. Ver lista de habitantes")
    print("3. Simular impacto tecnológico (Próximamente)")
    print("4. Mostrar gráficas (Próximamente)")
    print("5. Guardar y Salir")
    print("="*50)

def registrar_habitante():
    """Registro de habitantes con más datos"""
    print("\n--- 📝 REGISTRO DE HABITANTE ---")
    
    # Límite de habitantes
    if len(habitantes) >= 10:
        print("❌ El pueblo ya tiene 10 habitantes. No podemos registrar más.")
        input("Presiona Enter para continuar...")
        return
    
    # === DATOS BÁSICOS ===
    nombre = input("Nombre completo: ").strip()
    if not nombre:
        print("❌ El nombre es obligatorio.")
        input("Presiona Enter para continuar...")
        return
    
    # Edad con validación
    try:
        edad = int(input("Edad: ").strip())
        if edad < 0 or edad > 120:
            print("❌ Edad no válida (debe ser entre 0 y 120).")
            input("Presiona Enter para continuar...")
            return
    except ValueError:
        print("❌ La edad debe ser un número.")
        input("Presiona Enter para continuar...")
        return
    
    ocupacion = input("Ocupación (ej. agricultor, profesor, etc.): ").strip()
    if not ocupacion:
        ocupacion = "No especificada"
    
    # === GÉNERO ===
    print("\nGénero:")
    print("1. Masculino")
    print("2. Femenino")
    print("3. Otro")
    print("4. Prefiero no decir")
    opcion_genero = input("Selecciona una opción (1-4): ").strip()
    
    generos = {
        '1': 'Masculino',
        '2': 'Femenino',
        '3': 'Otro',
        '4': 'No especificado'
    }
    genero = generos.get(opcion_genero, 'No especificado')
    
    # === NIVEL DE ESTUDIOS ===
    print("\nNivel de estudios:")
    print("1. Sin estudios")
    print("2. Primaria")
    print("3. Secundaria")
    print("4. Preparatoria / Bachillerato")
    print("5. Universidad")
    print("6. Posgrado")
    opcion_estudios = input("Selecciona una opción (1-6): ").strip()
    
    estudios = {
        '1': 'Sin estudios',
        '2': 'Primaria',
        '3': 'Secundaria',
        '4': 'Preparatoria',
        '5': 'Universidad',
        '6': 'Posgrado'
    }
    nivel_estudios = estudios.get(opcion_estudios, 'No especificado')
    
    # === TECNOLOGÍAS ===
    print("\nTecnologías que posee (puedes elegir varias, separadas por coma):")
    print("1. Teléfono inteligente")
    print("2. Computadora")
    print("3. Tablet")
    print("4. Panel solar")
    print("5. Sensor de riego")
    print("6. Báscula digital")
    print("7. Ninguna")
    
    opciones_tec = input("Ejemplo: 1,3,5 (o 7 si no tiene): ").strip()
    
    tecnologias_dict = {
        '1': 'Teléfono inteligente',
        '2': 'Computadora',
        '3': 'Tablet',
        '4': 'Panel solar',
        '5': 'Sensor de riego',
        '6': 'Báscula digital',
        '7': 'Ninguna'
    }
    
    if opciones_tec == '7':
        tecnologias_lista = ['Ninguna']
    else:
        seleccionadas = [tec.strip() for tec in opciones_tec.split(',') if tec.strip()]
        tecnologias_lista = []
        for tec in seleccionadas:
            if tec in tecnologias_dict:
                tecnologias_lista.append(tecnologias_dict[tec])
        if not tecnologias_lista:
            tecnologias_lista = ['No especificado']
    
    # === ACCESO A INTERNET ===
    print("\n¿Tiene acceso a internet?")
    print("1. Sí, por datos móviles")
    print("2. Sí, por WiFi en casa")
    print("3. Sí, por ambos")
    print("4. No tiene acceso")
    opcion_internet = input("Selecciona una opción (1-4): ").strip()
    
    internet = {
        '1': 'Datos móviles',
        '2': 'WiFi en casa',
        '3': 'Ambos',
        '4': 'Sin acceso'
    }
    acceso_internet = internet.get(opcion_internet, 'No especificado')
    
    # === INGRESO ===
    try:
        ingreso = float(input("\nIngreso mensual aproximado (en Dolares, solo números): ").strip() or "0")
        if ingreso < 0:
            ingreso = 0
    except ValueError:
        ingreso = 0
        print("  (Ingreso no válido, se asignó 0)")
    
    # === CREAR DICCIONARIO ===
    nuevo_habitante = {
        'id': len(habitantes) + 1,
        'nombre': nombre,
        'edad': edad,
        'genero': genero,
        'ocupacion': ocupacion,
        'estudios': nivel_estudios,
        'tecnologias': tecnologias_lista,
        'internet': acceso_internet,
        'ingreso': ingreso,
        'productividad_base': 50
    }
    
    # Agregar a la lista
    habitantes.append(nuevo_habitante)
    
    print(f"\n✅ ¡Habitante {nombre} registrado con éxito!")
    print(f"ID asignado: {nuevo_habitante['id']}")
    print(f"Tecnologías: {', '.join(tecnologias_lista)}")
    input("\nPresiona Enter para continuar...")

def listar_habitantes():
    """Muestra la lista de habitantes"""
    print("\n" + "="*60)
    print(" 📋 LISTA DE HABITANTES DEL PUEBLO 📋".center(60))
    print("="*60)
    
    if not habitantes:
        print("\n❌ No hay habitantes registrados aún.")
        input("\nPresiona Enter para continuar...")
        return
    
    # Cabecera
    print(f"\n{'ID':<4} {'NOMBRE':<20} {'EDAD':<5} {'OCUPACIÓN':<15} {'INTERNET':<15}")
    print("-"*70)
    
    # Mostrar cada habitante
    for h in habitantes:
        print(f"{h['id']:<4} {h['nombre'][:19]:<20} {h['edad']:<5} {h['ocupacion'][:14]:<15} {h['internet'][:14]:<15}")
    
    # Resumen
    print("\n📊 RESUMEN DEL PUEBLO:")
    print(f"  • Total de habitantes: {len(habitantes)}")
    
    input("\nPresiona Enter para continuar...")

def main():
    """Función principal"""
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        opcion = input("\n👉 Selecciona una opción (1-5): ")
        
        if opcion == '1':
            registrar_habitante()
        elif opcion == '2':
            listar_habitantes()
        elif opcion == '3':
            print("\n⏳ Simulador en construcción...")
            input("Presiona Enter para continuar...")
        elif opcion == '4':
            print("\n⏳ Gráficas en construcción...")
            input("Presiona Enter para continuar...")
        elif opcion == '5':
            print("\n👋 ¡Hasta pronto!")
            break
        else:
            print("\n❌ Opción no válida")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    print("🚀 Iniciando SmartVillage - Día 2")
    main()
