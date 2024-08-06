from flask import Blueprint, request, redirect, url_for
from modelo.tarea_modelo import agregar_tarea, obtener_tareas
from vista.tarea_vista import renderizar_tareas

tarea_bp = Blueprint('tarea', __name__)

@tarea_bp.route('/')

@tarea_bp.route("/")
def display_tasks():
    tasks = get_tasks()
    return render_tasks(tasks)


def get_tasks():
    return obtener_tareas()


def render_tasks(tasks):
    return renderizar_tareas(tasks)
def mostrar_tareas():
    return renderizar_tareas(obtener_tareas())

@tarea_bp.route('/agregar_tarea', methods=['GET', 'POST'])
def agregar_tarea_ruta():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        if titulo:
            agregar_tarea(titulo, descripcion)
            return redirect(url_for('tarea.mostrar_tareas'))
        else:
            return 'El título es obligatorio', 400
    return '''
        <form method="post">
            Título: <input type="text" name="titulo"><br>
            Descripción: <input type="text" name="descripcion"><br>
            <input type="submit" value="Agregar Tarea">
        </form>
    '''
