# ============================================
# DÍA CLAVE - SEMANA 4: SIMULACIÓN DE IMPACTO
# ============================================

# ---------------------
# 1. DATOS GLOBALES
# ---------------------
lista_habitantes = []  # Aquí guardamos los registros

# Variables para guardar los resultados de la simulación
resultado_simulacion = {
    "fecha": "Simulación Día 3",
    "produccion_total_sin_tecnologia": 0,
    "produccion_total_con_tecnologia": 0,
    "mejora_porcentaje": 0,
    "detalle_por_habitante": []
}


# ---------------------
# 2. FUNCIONES DE REGISTRO
# ---------------------
def registrar_habitante():
    """Registra un nuevo habitante."""
    print("\n--- REGISTRO DE NUEVO HABITANTE ---")
    nombre = input("Nombre del habitante: ")
    edad = input("Edad: ")
    oficio = input("Oficio (agricultor, ganadero, artesano, etc.): ")
    
    print("¿Tiene acceso a tecnología? (si/no)")
    tecnologia = input("=> ").lower()
    
    habitante = {
        "nombre": nombre,
        "edad": edad,
        "oficio": oficio,
        "tecnologia": tecnologia == "si"
    }
    
    lista_habitantes.append(habitante)
    print(f"✅ {nombre} ha sido registrado exitosamente!")
    return habitante


def listar_habitantes():
    """Muestra todos los habitantes."""
    print("\n--- LISTA DE HABITANTES ---")
    if len(lista_habitantes) == 0:
        print("❌ No hay habitantes registrados.")
        return
    
    for i, h in enumerate(lista_habitantes, 1):
        tech = "📱 Tiene tecnología" if h['tecnologia'] else "📡 Sin tecnología"
        print(f"{i}. {h['nombre']} - {h['oficio']} - {tech}")


# ---------------------
# 3. FUNCIÓN CLAVE: SIMULACIÓN DE IMPACTO
# ---------------------
def simular_impacto():
    """
    🚀 FUNCIÓN MÁS IMPORTANTE DEL DÍA
    Simula cómo la tecnología mejora la productividad del pueblo.
    """
    print("\n" + "="*50)
    print("🔮 SIMULACIÓN DE IMPACTO TECNOLÓGICO")
    print("="*50)
    
    # Validar que haya habitantes
    if len(lista_habitantes) == 0:
        print("❌ No hay habitantes para simular. Registra primero.")
        return
    
    # Variables para guardar resultados
    produccion_sin_tech = 0
    produccion_con_tech = 0
    detalles = []
    
    print("\n📊 ANALIZANDO CADA HABITANTE...\n")
    
    # Recorrer cada habitante
    for habitante in lista_habitantes:
        nombre = habitante['nombre']
        oficio = habitante['oficio']
        tiene_tech = habitante['tecnologia']
        
        # ASIGNAR PRODUCTIVIDAD BASE SEGÚN EL OFICIO
        if oficio.lower() == "agricultor":
            base = 100  # kilos de maíz
        elif oficio.lower() == "ganadero":
            base = 80   # litros de leche
        elif oficio.lower() == "artesano":
            base = 60   # piezas artesanales
        else:
            base = 50   # oficio genérico
        
        # CALCULAR PRODUCCIÓN CON Y SIN TECNOLOGÍA
        produccion_actual = base
        produccion_mejorada = base * 1.5  # 50% más con tecnología
        
        # Si ya tiene tecnología, su producción actual ya es la mejorada
        if tiene_tech:
            produccion_actual = produccion_mejorada
        
        # Acumular totales
        produccion_sin_tech += base
        produccion_con_tech += produccion_mejorada
        
        # Guardar detalle individual
        detalle = {
            "nombre": nombre,
            "oficio": oficio,
            "tiene_tecnologia": tiene_tech,
            "produccion_actual": produccion_actual,
            "produccion_potencial": produccion_mejorada
        }
        detalles.append(detalle)
        
        # Mostrar en pantalla
        print(f"👤 {nombre}:")
        print(f"   - Producción actual: {produccion_actual:.0f} unidades")
        print(f"   - Producción potencial (con tecnología): {produccion_mejorada:.0f} unidades")
        if not tiene_tech:
            print(f"   ⚡ Podría aumentar {produccion_mejorada - produccion_actual:.0f} unidades con tecnología")
        print()
    
    # CALCULAR MEJORA TOTAL
    mejora_total = produccion_con_tech - produccion_sin_tech
    porcentaje_mejora = (mejora_total / produccion_sin_tech) * 100 if produccion_sin_tech > 0 else 0
    
    # GUARDAR RESULTADOS EN VARIABLES GLOBALES
    global resultado_simulacion
    resultado_simulacion = {
        "fecha": "Simulación Día 3 - Clave",
        "produccion_total_sin_tecnologia": produccion_sin_tech,
        "produccion_total_con_tecnologia": produccion_con_tech,
        "mejora_porcentaje": porcentaje_mejora,
        "detalle_por_habitante": detalles
    }
    
    # MOSTRAR RESUMEN FINAL
    print("="*50)
    print("📈 RESULTADOS DE LA SIMULACIÓN")
    print("="*50)
    print(f"🌾 Producción sin tecnología: {produccion_sin_tech:.0f} unidades")
    print(f"🚀 Producción con tecnología:  {produccion_con_tech:.0f} unidades")
    print(f"📈 Mejora total: +{mejora_total:.0f} unidades")
    print(f"🔥 Porcentaje de mejora: +{porcentaje_mejora:.1f}%")
    print("="*50)
    
    return resultado_simulacion


def ver_ultima_simulacion():
    """Muestra los resultados guardados de la última simulación."""
    print("\n--- ÚLTIMA SIMULACIÓN GUARDADA ---")
    if resultado_simulacion["produccion_total_sin_tecnologia"] == 0:
        print("❌ Aún no has corrido ninguna simulación.")
        return
    
    print(f"📅 {resultado_simulacion['fecha']}")
    print(f"🌾 Producción sin tecnología: {resultado_simulacion['produccion_total_sin_tecnologia']:.0f}")
    print(f"🚀 Producción con tecnología: {resultado_simulacion['produccion_total_con_tecnologia']:.0f}")
    print(f"📈 Mejora: +{resultado_simulacion['mejora_porcentaje']:.1f}%")
    
    print("\nDetalle por habitante:")
    for detalle in resultado_simulacion["detalle_por_habitante"]:
        tech = "✅ Tiene tech" if detalle['tiene_tecnologia'] else "❌ Sin tech"
        print(f"   - {detalle['nombre']}: {detalle['produccion_actual']:.0f} unid. {tech}")


# ---------------------
# 4. MENÚ PRINCIPAL ACTUALIZADO
# ---------------------
def menu_principal():
    while True:
        print("\n" + "="*40)
        print("      S M A R T  V I L L A G E")
        print("="*40)
        print("1. Registrar nuevo habitante")
        print("2. Ver lista de habitantes")
        print("3. 🔮 SIMULAR IMPACTO (DÍA CLAVE)")
        print("4. Ver última simulación")
        print("5. Salir")
        print("="*40)
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == "1":
            registrar_habitante()
        elif opcion == "2":
            listar_habitantes()
        elif opcion == "3":
            simular_impacto()  # ⚡ LA FUNCIÓN NUEVA
        elif opcion == "4":
            ver_ultima_simulacion()
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")


# ---------------------
# 5. PUNTO DE ENTRADA
# ---------------------
if __name__ == "__main__":
    menu_principal()
