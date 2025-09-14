import json

def cargar_datos():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_datos(datos):
    with open("data.json", "w") as f:
        json.dump(datos, f, indent=4)

def crear_documento():
    documento = {
        "id": input("ID del documento: "),
        "caja": input("Número de caja: "),
        "hojas": input("Cantidad de hojas: "),
        "paginas": input("Cantidad de páginas: "),
        "estante": input("ID del estante: ")
    }
    datos = cargar_datos()
    datos.append(documento)
    guardar_datos(datos)
    print("Documento guardado correctamente.")

def listar_documentos():
    datos = cargar_datos()
    for doc in datos:
        print(doc)

def actualizar_documento():
    id_buscar = input("ID del documento a actualizar: ")
    datos = cargar_datos()
    for doc in datos:
        if doc["id"] == id_buscar:
            doc["caja"] = input("Nuevo número de caja: ")
            doc["hojas"] = input("Nueva cantidad de hojas: ")
            doc["paginas"] = input("Nueva cantidad de páginas: ")
            doc["estante"] = input("Nuevo ID del estante: ")
            guardar_datos(datos)
            print("Documento actualizado.")
            return
    print("Documento no encontrado.")

def eliminar_documento():
    id_buscar = input("ID del documento a eliminar: ")
    datos = cargar_datos()
    datos = [doc for doc in datos if doc["id"] != id_buscar]
    guardar_datos(datos)
    print("Documento eliminado.")

# Menú
while True:
    print("\n1. Crear\n2. Listar\n3. Actualizar\n4. Eliminar\n5. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        crear_documento()
    elif opcion == "2":
        listar_documentos()
    elif opcion == "3":
        actualizar_documento()
    elif opcion == "4":
        eliminar_documento()
    elif opcion == "5":
        break
