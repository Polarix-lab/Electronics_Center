import os
from flask import Flask, render_template

app = Flask(__name__)

# Base de datos simulada en memoria (puedes cambiarla o ampliarla fácilmente)
CATALOGO_PIEZAS = [
    {
        "id": 1,
        "nombre": "Protoboard 830 Puntos",
        "precio": 40.00,
        "stock": 10,
        "imagen": "protoboard830.jpg"
    },
    {
        "id": 2,
        "nombre": "Resistencias, todos los valores",
        "precio": 0.50,
        "stock": 200,
        "imagen": "resistencia.jpg"
    },
    {
        "id": 3,
        "nombre": "Leds, 5 colores",
        "precio": 0.50,
        "stock": 200,
        "imagen": "leds.jpg"
    },
    {
        "id": 4,
        "nombre": "Cable Awg 22 por metro",
        "precio": 5.00,
        "stock": 100,
        "imagen": "cable_awg22.jpg"
    }
]

@app.route('/')
def home():
    # Renderiza la plantilla HTML y le pasa la lista de piezas
    return render_template('index.html', piezas=CATALOGO_PIEZAS)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
