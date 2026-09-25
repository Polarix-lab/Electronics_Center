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
        "nombre": "Resistencias<br>Todos los valores",
        "precio": 0.50,
        "stock": 200,
        "imagen": "resistencia.jpg"
    },
    {
        "id": 3,
        "nombre": "Arduino Uno con cable",
        "precio": 119.00,
        "stock": 10,
        "imagen": "arduino_uno_cable.jpg"
    },
    {
        "id": 4,
        "nombre": "Cable Awg 22<br>Por metro",
        "precio": 5.00,
        "stock": 100,
        "imagen": "cable_awg22.jpg"
    },
    {
        "id": 5,
        "nombre": "Jumpers 10cm 20cm 30cm<br>M-M H-H M-H",
        "precio": 0.50,
        "stock": 360,
        "imagen": "jumpers.jpg"
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
        "nombre": "Pila de 9V",
        "precio": 35.00,
        "stock": 30,
        "imagen": "pila_9v.jpg"
    },
    {
        "id": 8,
        "nombre": "Combo de Pila 9V y Broche",
        "precio": 39.00,
        "stock": 30,
        "imagen": "pila_9v_con_broche.jpg"
    },
    {
        "id": 9,
        "nombre": "Servo motor sg90",
        "precio": 30.00,
        "stock": 25,
        "imagen": "servomotor_sg90.jpg"
    },
    {
        "id": 10,
        "nombre": "Boton Pulsador",
        "precio": 1.00,
        "stock": 200,
        "imagen": "boton_pulsador.jpg"
    },
    {
        "id": 11,
        "nombre": "Leds<br>5 Colores",
        "precio": 0.50,
        "stock": 1000,
        "imagen": "leds.jpg"
    },
    {
        "id": 12,
        "nombre": "Buzzer activo",
        "precio": 20.00,
        "stock": 10,
        "imagen": "buzzer.jpg"
    },
    {
        "id": 13,
        "nombre": "Capacitores Ceramicos<br>Todos los Valores",
        "precio": 3.00,
        "stock": 1000,
        "imagen": "capacitores_ceramicos.jpg"
    },
    {
        "id": 14,
        "nombre": "Par de Cables Caimán-Caimán",
        "precio": 10.00,
        "stock": 50,
        "imagen": "cables_caiman.jpg"
    },
    {
        "id": 15,
        "nombre": "Capacitores Electrolíticos<br>Todos los Valores",
        "precio": 3.00,
        "stock": 100,
        "imagen": "capacitores_electroliticos.jpg"
    },
    {
        "id": 16,
        "nombre": "Compuertas lógicas<br>Todos los Valores",
        "precio": 10.00,
        "stock": 10,
        "imagen": "compuertas_logicas.jpg"
    },
    {
        "id": 17,
        "nombre": "Potenciómetros<br>Todos los Valores",
        "precio": 8.00,
        "stock": 30,
        "imagen": "potenciometro.jpg"
    },
    {
        "id": 18,
        "nombre": "Puentes H L298n",
        "precio": 60.00,
        "stock": 10,
        "imagen": "puenteH_L298n.jpg"
    },
    {
        "id": 19,
        "nombre": "Sensor de Fuerza",
        "precio": 150.00,
        "stock": 5,
        "imagen": "sensor_de_fuerza.jpg"
    },
    {
        "id": 20,
        "nombre": "Diodos Rectificadores<br>Todos los valores",
        "precio": 2.00,
        "stock": 200,
        "imagen": "diodo_rectificador.jpg"
    },
    {
        "id": 21,
        "nombre": "Transistores<br>Todos los valores",
        "precio": 4.00,
        "stock": 100,
        "imagen": "transistores.jpg"
    },
    {
        "id": 22,
        "nombre": "Display de 7 Segmentos",
        "precio": 8.00,
        "stock": 50,
        "imagen": "display_7_segmentos.jpg"
    },
    {
        "id": 23,
        "nombre": "Arduino Uno R3<br>Sin Cable",
        "precio": 99.00,
        "stock": 10,
        "imagen": "arduino_uno_r3.jpg"
    },
    {
        "id": 24,
        "nombre": "Cable para arduino",
        "precio": 25.00,
        "stock": 10,
        "imagen": "cable_arduino.jpg"
    },
    {
        "id": 25,
        "nombre": "Sensor de temperatura Lm35",
        "precio": 50.00,
        "stock": 10,
        "imagen": "sensor_Lm35.jpg"
    }
    
]

@app.route('/')
def home():
    # Renderiza la plantilla HTML y le pasa la lista de piezas
    return render_template('index.html', piezas=CATALOGO_PIEZAS)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
