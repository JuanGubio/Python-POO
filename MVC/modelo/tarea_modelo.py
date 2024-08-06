
tareas = []

def agregar_tarea(titulo, descripcion):
    tarea = {'titulo': titulo, 'descripcion': descripcion}
    tareas.append(tarea)

def obtener_tareas():
    return tareas
