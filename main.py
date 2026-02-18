# main.py - SmartVillage
print("=== SMARTVILLAGE ===")

habitantes = []  # Aquí guardaremos los datos

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar habitante")
    print("2. Simular impacto tecnológico")
    print("3. Ver estadísticas y gráfica")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        print("\n--- REGISTRO DE HABITANTES ---")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        oficio = input("Oficio (agricultor/ganadero/artesano): ")
        
        habitante = {
            "nombre": nombre,
            "edad": edad,
            "oficio": oficio,
            "productividad": 50  # Valor base
        }
        habitantes.append(habitante)
        print(f"✅ {nombre} registrado con éxito!")
        
    elif opcion == "2":
        print("⏳ Función en desarrollo...")
        
    elif opcion == "3":
        print("⏳ Función en desarrollo...")
        
    elif opcion == "4":
        print("👋 ¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida")