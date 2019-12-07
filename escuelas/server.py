from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'WCqgiEsLy3'
app.config['MYSQL_PASSWORD'] = 'I9yyxDyDIJ'
app.config['MYSQL_DB'] = 'WCqgiEsLy3'
app.config['MYSQL_HOST'] = 'remotemysql.com'

mysql = MySQL(app)

@app.route('/')
def inicia():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT `domicilio`, `municipio` FROM `primaria`")
    resultsPrimaria = cursor.fetchall()
    print(resultsPrimaria)
    cursor.execute("SELECT `domicilio`, `municipio` FROM `secundaria`")
    resultsSecundaria = cursor.fetchall()
    print(resultsSecundaria)
    cursor.execute("SELECT `domicilio`, `municipio` FROM `preparatoria`")
    resultsPreparatoria = cursor.fetchall()
    print(resultsPreparatoria)
    return 'Done!'

@app.route('/mapa')
def verMapa():
    return render_template("mapa.html")

if __name__ == "__main__":
    app.run()
    