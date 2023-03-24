usuarios = []
id_usuario = 0

def agregar_usuario():
    global id_usuario
    nombre = input("Ingresar Nombre: ")
    edad = int(input("Ingresar edad: "))
    usuarios.append({"id": id_usuario, "nombre": nombre, "edad": edad})
    id_usuario += 1
    
def listar_usuarios():
    for usuario in usuarios:
        print("usuario: ", usuario)

def buscar_usuario_por_id(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    return None

def actualizar_usuario():
    id = int(input("Ingresar ID del usuario a actualizar: "))
    usuario = buscar_usuario_por_id(id)
    if usuario is None:
        print("ID inválido")
        return
    nombre = input("Ingresa nuevo nombre: ")
    edad = int(input("Ingresa nueva edad: "))
    usuario["nombre"] = nombre
    usuario["edad"] = edad

def eliminar_usuario():
    id = int(input("Ingresar ID del usuario a eliminar: "))
    usuario = buscar_usuario_por_id(id)
    if usuario is None:
        print("ID inválido")
        return
    usuarios.remove(usuario)

while True:
    print("1. Agregar")
    print("2. Listar")
    print("3. Modiicar")
    print("4. Eliminar")
    print("5. Salir")
    opcion = int(input("Elección: "))
    if opcion == 1:
        agregar_usuario()
    elif opcion == 2:
        listar_usuarios()
    elif opcion == 3:
        actualizar_usuario()
    elif opcion == 4:
        eliminar_usuario()
    elif opcion == 5:
        break