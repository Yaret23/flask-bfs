from flask import Flask, request, render_template
import sys
import os

# Asegurar que encuentre BFS
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from BFS import buscar_solucion_BFS

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    inicial = "4,2,3,1"
    solucion = "1,2,3,4"
    error = None
    resultado = None
    no_solucion = False
    pasos = 0

    if request.method == 'POST':
        inicial = request.form.get('inicial', '')
        solucion = request.form.get('solucion', '')

        try:
            inicial_list = [int(x.strip()) for x in inicial.split(',')]
            solucion_list = [int(x.strip()) for x in solucion.split(',')]

            if len(inicial_list) != 4 or len(solucion_list) != 4:
                error = "Ambos estados deben tener exactamente 4 elementos."
            else:
                nodo_solucion = buscar_solucion_BFS(inicial_list, solucion_list)

                if nodo_solucion is None:
                    no_solucion = True
                else:
                    resultado = []
                    nodo = nodo_solucion

                    while nodo.get_padre() is not None:
                        resultado.append(nodo.get_datos())
                        nodo = nodo.get_padre()

                    resultado.append(inicial_list)
                    resultado.reverse()
                    pasos = len(resultado) - 1

        except ValueError:
            error = "Entrada inválida. Usa números separados por comas."

    return render_template(
        'index2.html',
        inicial=inicial,
        solucion=solucion,
        error=error,
        resultado=resultado,
        no_solucion=no_solucion,
        pasos=pasos
    )

# 🔥 IMPORTANTE PARA RENDER
if __name__ == "__main__":
    app.run()