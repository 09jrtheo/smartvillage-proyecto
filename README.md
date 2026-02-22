# 🌾 SmartVillage - Proyecto Integrador


- **Nombre del Proyecto:** El impacto de las nuevas tecnologías en la sociedad: SmartVillage
- **Asignatura:** Logica de programacion
- **Integrantes:** 
  -Mateo Fernando Amangano Quishpe 
  
- **Fecha de entrega:** 01/03/2026
- **Repositorio:** https://github.com/09jrtheo/smartvillage-proyecto

---

## 🎯 OBJETIVO DEL PROGRAMA
Simular y visualizar cómo la implementación de tecnologías accesibles (sensores, internet, herramientas digitales) puede impactar positivamente la vida cotidiana, la economía y la comunicación en una comunidad rural pequeña. El programa permite reflexionar sobre un futuro tecnológico inclusivo y sostenible.

---

## 📚 INTEGRACIÓN DE LAS 4 UNIDADES

### UNIDAD 1: INTRODUCCIÓN A LA PROGRAMACIÓN
- ✅ **Variables:** Uso de variables para almacenar datos de habitantes (`nombre`, `edad`, `oficio`)
- ✅ **Condicionales:** `if/else` para validar opciones del menú y determinar si tiene tecnología
- ✅ **Ciclos:** `while` para mantener el menú activo y `for` para recorrer la lista de habitantes

### UNIDAD 2: ESTRUCTURAS DE DATOS Y FUNCIONES
- ✅ **Programación Funcional:** Creación de funciones específicas (`registrar_habitante()`, `simular_impacto()`, `generar_grafica()`)
- ✅ **Listas:** `lista_habitantes` para almacenar múltiples registros
- ✅ **Diccionarios:** Cada habitante es un diccionario con `nombre`, `edad`, `oficio`, `tecnologia`
- ✅ **Enumeración:** Uso de `enumerate()` para mostrar listas numeradas

### UNIDAD 3: MANEJO DE ARCHIVOS (PERSISTENCIA)
- ✅ **Archivos CSV:** Guardado automático de resultados en `datos.csv`
- ✅ **Lectura/Escritura:** Uso de `with open()` y el módulo `csv` para guardar datos
- ✅ **Verificación:** Comprobación de existencia de archivos con `os.path.isfile()`
- ✅ **Historial:** Cada simulación agrega una nueva fila al archivo sin borrar las anteriores

### UNIDAD 4: LIBRERÍAS EXTERNAS Y VISUALIZACIÓN
- ✅ **Matplotlib:** Instalación y uso de `matplotlib.pyplot` para generar gráficas
- ✅ **Gráfica de barras:** Comparación entre producción actual y producción potencial
- ✅ **Guardado de imágenes:** Exportación automática a `grafica_impacto.png`
- ✅ **Módulo datetime:** Uso de `datetime.now()` para marcar la fecha de cada simulación

---

## 🚀 PRINCIPALES FUNCIONALIDADES

| Opción | Función | Descripción |
|:------:|:--------|:------------|
| **1** | `registrar_habitante()` | Da de alta un nuevo habitante con nombre, edad, oficio y si tiene tecnología |
| **2** | `listar_habitantes()` | Muestra todos los habitantes registrados con su estado tecnológico |
| **3** | `simular_impacto()` | Calcula la producción actual y potencial, y guarda en CSV |
| **4** | `ver_ultima_simulacion()` | Muestra los resultados de la simulación más reciente |
| **5** | Ver CSV | Muestra en pantalla el contenido de `datos.csv` |
| **6** | `generar_grafica()` | Crea y guarda una gráfica comparativa en `grafica_impacto.png` |
| **7** | Salir | Termina la ejecución del programa |

---

## 📊 EJEMPLO DE FUNCIONAMIENTO

### Registro de habitante:
