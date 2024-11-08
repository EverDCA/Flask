from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)





#Aritmetica
@app.route('/', methods=['GET', 'POST'])
def aritmetica():
    inserte = ""  # Variable vacía para `inserte` en caso de GET o errores

    if request.method == 'POST':
        # Obtener los valores de n1 y n2 del formulario
        number1 = request.form.get('n1')
        number2 = request.form.get('n2')
        
        # Validar si los valores no están vacíos
        if number1 and number2:
            try:
                # Convertir los valores a float para operaciones aritméticas
                number1 = float(number1)
                number2 = float(number2)

                # Operaciones aritméticas
                suma = number1 + number2
                resta = number1 - number2
                mul = number1 * number2
                div = number1 / number2 if number2 != 0 else "Error: División por cero"

                # Generar el contenido HTML con los resultados
                inserte = f'''
                    <div class="row py-2">
                        <div class="col">
                            <h3>Suma: {suma}</h3>
                            <h3>Resta: {resta}</h3>
                            <h3>Multiplicación: {mul}</h3>
                            <h3>División: {div}</h3>
                        </div>
                    </div>
                '''
            except ValueError:
                inserte = "<p>Error: Los valores ingresados no son números válidos.</p>"
        else:
            inserte = "<p>Error: Por favor ingresa ambos números.</p>"

    # Renderizar la plantilla `index.html` con el contenido generado
    return render_template('index.html', inserte=inserte)








#Divisa
@app.route('/divisa', methods=['GET', 'POST'])
def divisa():
    inserte = "" 
    if request.method == 'POST':
        # Obtener los valores de n1 y n2 del formulario
        number1 = request.form.get('n1')
        
        # Validar si los valores no están vacíos
        if number1:
            try:
                # Convertir los valores a float para operaciones aritméticas
                number1 = float(number1)

                # Operaciones aritméticas
                conver=number1*4.396 #dolar a pesos Cop

                # Generar el contenido HTML con los resultados
                inserte = f'''
                    <div class="row py-2">
                        <div class="col">
                            <h3>Conversion de Dolares(USD) a Pesos Colombianos(COP): {round(conver,3)} </h3>
                        </div>
                    </div>
                '''
            except ValueError:
                inserte = "<p>Error: Los valores ingresados no son números válidos.</p>"
        else:
            inserte = "<p>Error: Por favor ingresa el numero de dolares.</p>"

    # Renderizar la plantilla `index.html` con el contenido generado
    return render_template('divisa.html', inserte=inserte)

if __name__ == '__main__':
    app.run(debug=True)
