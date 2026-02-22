# ============================================
# DÍA 4 - GUARDADO EN ARCHIVO Y GRÁFICA
# ============================================

import matplotlib.pyplot as plt
import csv
import os
from datetime import datetime

# ---------------------
# 1. DATOS GLOBALES
# ---------------------
lista_habitantes = []
resultado_simulacion = {
    "fecha": "",
    "produccion_total_sin_tecnologia": 0,
    "produccion_total_con_tecnologia": 0,
    "mejora_porcentaje": 0,
    "detalle_por_habitante": []
}


# ---------------------
# 2. FUNCIONES DE REGISTRO
# ---------------------
def registrar_habitante():
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


def listar_habitantes():
    print("\n--- LISTA DE HABITANTES ---")
    if len(lista_habitantes) == 0:
        print("❌ No hay habitantes registrados.")
        return
    
    for i, h in enumerate(lista_habitantes, 1):
        tech = "📱 Tiene tecnología" if h['tecnologia'] else "📡 Sin tecnología"
        print(f"{i}. {h['nombre']} - {h['oficio']} - {tech}")


# ---------------------
# 3. FUNCIÓN DE SIMULACIÓN (ACTUALIZADA)
# ---------------------
def simular_impacto():
    print("\n" + "="*50)
    print("🔮 SIMULACIÓN DE IMPACTO TECNOLÓGICO")
    print("="*50)
    
    if len(lista_habitantes) == 0:
        print("❌ No hay habitantes para simular. Registra primero.")
        return
    
    produccion_sin_tech = 0
    produccion_con_tech = 0
    detalles = []
    
    print("\n📊 ANALIZANDO CADA HABITANTE...\n")
    
    for habitante in lista_habitantes:
        nombre = habitante['nombre']
        oficio = habitante['oficio']
        tiene_tech = habitante['tecnologia']
        
        # Asignar productividad base
        if oficio.lower() == "agricultor":
            base = 100
        elif oficio.lower() == "ganadero":
            base = 80
        elif oficio.lower() == "artesano":
            base = 60
        else:
            base = 50
        
        produccion_actual = base * 1.5 if tiene_tech else base
        produccion_mejorada = base * 1.5
        
        produccion_sin_tech += base
        produccion_con_tech += produccion_mejorada
        
        detalle = {
            "nombre": nombre,
            "oficio": oficio,
            "tiene_tecnologia": tiene_tech,
            "produccion_actual": produccion_actual,
            "produccion_potencial": produccion_mejorada
        }
        detalles.append(detalle)
        
        print(f"👤 {nombre}:")
        print(f"   - Producción actual: {produccion_actual:.0f} unidades")
        if not tiene_tech:
            print(f"   ⚡ Podría aumentar {produccion_mejorada - produccion_actual:.0f} unidades con tecnología")
        print()
    
    mejora_total = produccion_con_tech - produccion_sin_tech
    porcentaje_mejora = (mejora_total / produccion_sin_tech) * 100 if produccion_sin_tech > 0 else 0
    
    # Guardar resultados
    global resultado_simulacion
    resultado_simulacion = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "produccion_total_sin_tecnologia": produccion_sin_tech,
        "produccion_total_con_tecnologia": produccion_con_tech,
        "mejora_porcentaje": porcentaje_mejora,
        "detalle_por_habitante": detalles
    }
    
    # 📁 GUARDAR EN ARCHIVO CSV (ESTO ES NUEVO)
    guardar_en_csv()
    
    # MOSTRAR RESULTADOS
    print("="*50)
    print("📈 RESULTADOS DE LA SIMULACIÓN")
    print("="*50)
    print(f"🌾 Producción sin tecnología: {produccion_sin_tech:.0f} unidades")
    print(f"🚀 Producción con tecnología:  {produccion_con_tech:.0f} unidades")
    print(f"📈 Mejora total: +{mejora_total:.0f} unidades")
    print(f"🔥 Porcentaje de mejora: +{porcentaje_mejora:.1f}%")
    print("="*50)


# ---------------------
# 4. 🆕 FUNCIÓN NUEVA: GUARDAR EN CSV
# ---------------------
def guardar_en_csv():
    """Guarda los resultados de la simulación en un archivo CSV"""
    archivo = "datos.csv"
    archivo_existe = os.path.isfile(archivo)
    
    with open(archivo, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Si el archivo no existía, escribir encabezados
        if not archivo_existe:
            writer.writerow(["Fecha", "Habitante", "Oficio", "Tiene_Tecnologia", 
                           "Produccion_Actual", "Produccion_Potencial"])
        
        # Guardar cada habitante
        for detalle in resultado_simulacion["detalle_por_habitante"]:
            writer.writerow([
                resultado_simulacion["fecha"],
                detalle["nombre"],
                detalle["oficio"],
                "Sí" if detalle["tiene_tecnologia"] else "No",
                detalle["produccion_actual"],
                detalle["produccion_potencial"]
            ])
    
    print(f"✅ Datos guardados en {archivo}")


# ---------------------
# 5. 🆕 FUNCIÓN NUEVA: GENERAR GRÁFICA
# ---------------------
def generar_grafica():
    """Genera una gráfica comparando producción con y sin tecnología"""
    if len(lista_habitantes) == 0:
        print("❌ No hay datos para graficar. Ejecuta una simulación primero.")
        return
    
    # Preparar datos
    nombres = [h['nombre'] for h in lista_habitantes]
    produccion_actual = []
    produccion_potencial = []
    
    for h in lista_habitantes:
        if h['tecnologia']:
            # Si tiene tecnología, su producción actual ya es la potencial
            base = 100 if h['oficio'].lower() == "agricultor" else 80 if h['oficio'].lower() == "ganadero" else 60 if h['oficio'].lower() == "artesano" else 50
            produccion_actual.append(base * 1.5)
            produccion_potencial.append(base * 1.5)
        else:
            base = 100 if h['oficio'].lower() == "agricultor" else 80 if h['oficio'].lower() == "ganadero" else 60 if h['oficio'].lower() == "artesano" else 50
            produccion_actual.append(base)
            produccion_potencial.append(base * 1.5)
    
    # Crear gráfica
    plt.figure(figsize=(10, 6))
    
    # Barras
    x = range(len(nombres))
    ancho = 0.35
    
    barras_actual = plt.bar([i - ancho/2 for i in x], produccion_actual, 
                           ancho, label='Producción Actual', color='skyblue')
    barras_potencial = plt.bar([i + ancho/2 for i in x], produccion_potencial, 
                              ancho, label='Producción Potencial (con tecnología)', color='orange')
    
    # Personalizar
    plt.xlabel('Habitantes')
    plt.ylabel('Producción (unidades)')
    plt.title('Impacto de la Tecnología en la Producción')
    plt.xticks(x, nombres, rotation=45)
    plt.legend()
    
    # Agregar valores en las barras
    for barra in barras_actual:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., altura,
                f'{int(altura)}', ha='center', va='bottom')
    
    for barra in barras_potencial:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., altura,
                f'{int(altura)}', ha='center', va='bottom')
    
    plt.tight_layout()
    
    # Guardar gráfica
    archivo_grafica = "grafica_impacto.png"
    plt.savefig(archivo_grafica, dpi=150)
    print(f"✅ Gráfica guardada como {archivo_grafica}")
    
    # Mostrar gráfica
    plt.show()


def ver_ultima_simulacion():
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
# 6. MENÚ PRINCIPAL
# ---------------------
def menu_principal():
    while True:
        print("\n" + "="*40)
        print("      S M A R T  V I L L A G E")
        print("="*40)
        print("1. Registrar nuevo habitante")
        print("2. Ver lista de habitantes")
        print("3. 🔮 SIMULAR IMPACTO")
        print("4. Ver última simulación")
        print("5. 📁 VER ARCHIVO CSV (datos.csv)")
        print("6. 📊 GENERAR GRÁFICA")
        print("7. Salir")
        print("="*40)
        
        opcion = input("Elige una opción (1-7): ")
        
        if opcion == "1":
            registrar_habitante()
        elif opcion == "2":
            listar_habitantes()
        elif opcion == "3":
            simular_impacto()
        elif opcion == "4":
            ver_ultima_simulacion()
        elif opcion == "5":
            if os.path.exists("datos.csv"):
                print("\n--- CONTENIDO DE datos.csv ---")
                with open("datos.csv", 'r', encoding='utf-8') as f:
                    print(f.read())
            else:
                print("❌ El archivo datos.csv aún no existe. Ejecuta una simulación primero.")
        elif opcion == "6":
            generar_grafica()
        elif opcion == "7":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    print("🔄 Verificando librerías...")
    try:
        plt.figure()  # Prueba rápida
        plt.close()
    except:
        print("⚠️ matplotlib no está instalado. Ejecuta: pip install matplotlib")
    menu_principal()
