from flask import Flask, request, render_template
import sys
import os

# Asegurar ruta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from BFS import buscar_solucion_BFS

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    inicial = "CDMX"
    solucion = "GDL"
    error = None
    resultado = None
    no_solucion = False
    pasos = 0

    if request.method == 'POST':
        inicial = request.form.get('inicial', '')
        solucion = request.form.get('solucion', '')

        try:
            resultado = buscar_solucion_BFS(inicial, solucion)

            if resultado is None:
                no_solucion = True
            else:
                pasos = len(resultado) - 1

        except Exception as e:
            error = str(e)

    return render_template(
        'index2.html',
        inicial=inicial,
        solucion=solucion,
        error=error,
        resultado=resultado,
        no_solucion=no_solucion,
        pasos=pasos
    )

if __name__ == "__main__":
    app.run()