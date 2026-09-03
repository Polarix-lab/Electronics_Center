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
        "stock": 1000,
        "imagen": "leds.jpg"
    },
    {
        "id": 4,
        "nombre": "Cable Awg 22 por metro",
        "precio": 5.00,
        "stock": 100,
        "imagen": "cable_awg22.jpg"
    },
    {
        "id": 5,
        "nombre": "Pila de 9V",
        "precio": 35.00,
        "stock": 30,
        "imagen": "pila_9v.jpg"
    },
    {
        "id": 6,
        "nombre": "Broche para pila de 9V",
        "precio": 5.00,
        "stock": 100,
        "imagen": "broche.jpg"
    },
    {
        "id": 7,
        "nombre": "Jumpers 20cm, M-M H-H M-H",
        "precio": 0.50,
        "stock": 360,
        "imagen": "jumpers.jpg"
    },
    {
        "id": 8,
        "nombre": "Servo motor sg90",
        "precio": 30.00,
        "stock": 0,
        "imagen": "servomotor_sg90.jpg"
    },
    {
        "id": 9,
        "nombre": "Combo de Pila 9V y Broche",
        "precio": 39.00,
        "stock": 30,
        "imagen": "pila_9v_con_broche.jpg"
    }
]

@app.route('/')
def home():
    # Renderiza la plantilla HTML y le pasa la lista de piezas
    return render_template('index.html', piezas=CATALOGO_PIEZAS)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
