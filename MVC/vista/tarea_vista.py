def renderizar_tareas(tareas):
    html = "<h1>Tareas</h1><ul>"
    for tarea in tareas:
        html += f"<li><strong>{tarea['titulo']}</strong>: {tarea['descripcion']}</li>"
    html += "</ul><br><a href='/agregar_tarea'>Agregar Tarea</a>"
    return html
                                                                                        