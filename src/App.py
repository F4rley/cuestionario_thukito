from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encuesta')
def encuesta():
    return render_template ('encuesta.html')

@app.route('/pregunta_1_2')
def pregunta_1_2():
    return render_template ('pregunta_1_2.html')

@app.route('/ecommerce')
def ecommerce():
    return render_template ('ecommerce.html')

@app.route('/precio')
def precio():
    return render_template ('precio.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/edit')
# def edit_contact():
#     return 'edit contact'
    
# @app.route('/delete')
# def delete_contact():
#     return 'delete contact'

if __name__== '__main__':
    app.run(port = 3000, debug=True)
