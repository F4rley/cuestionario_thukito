from flask import Flask, render_template, request, url_for
import psycopg2


app = Flask(__name__)

#Definir una funcipon para introducir los datos en la db
def save_dbloggin(fullname, type_user, email_user, telephone):
    conn = psycopg2.connect(
        dbname="question_prueba", 
        user="postgres",
        password="_70472143",
        host="localhost",
        port="5432"
    )
    #Abrir un cursos, donde nos permitira poner datos desde python
    cursor = conn.cursor()
    query = '''INSERT INTO loggin(full_name, type_user, email_user, telephone) VALUES (%s, %s, %s, %s)'''
    cursor.execute(query, (fullname, type_user, email_user, telephone))
    print("Continuemos")
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/registrar', methods = ("GET","POST"))
def registrar():
    if request.method == "POST":
        full_name = request.form.get("txtfullname")
        type_user = request.form.get("txttypeuser")
        email_user = request.form.get("txtemailuser")
        telephone = request.form.get("numtelephone")
    
        save_dbloggin(full_name, type_user, email_user, telephone)      
        return render_template("encuesta.html")
    
    return index()

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
