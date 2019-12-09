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
def verMapa():
    matrizMunic = [["Guadalajara",0,0,0,20.6720375,-103.3383962],
            ["Zapopan",0,0,0,20.7032055,-103.4261243],
            ["SAN PEDRO TLAQUEPAQUE",0,0,0,20.5925775,-103.3388803],
            ["Tonalá",0,0,0,20.6185208,-103.2227359],
            ["Tlajomulco de Zúñiga",0,0,0,20.4737273,-103.4469713],
            ["El Salto",0,0,0,20.5391001,-103.2403775],
            ["Ixtlahuacán de los Membrillos",0,0,0,20.348165,-103.195463],
            ["Juanacatlán",0,0,0,20.507090,-103.170622]]
    cursor = mysql.connection.cursor()
    for municipio in matrizMunic:
        query1 = 'SELECT COUNT(*) FROM `primaria` WHERE `municipio` = "' + municipio[0] + '"'
        cursor.execute(query1)
        resultsPrimaria = cursor.fetchall()
        municipio[1]=resultsPrimaria[0][0]

        query2 = 'SELECT COUNT(*) FROM `secundaria` WHERE `municipio` = "' + municipio[0] + '"'
        cursor.execute(query2)
        resultsSecundaria = cursor.fetchall()
        municipio[2]=resultsSecundaria[0][0]

        query3 = 'SELECT COUNT(*) FROM `preparatoria` WHERE `municipio` = "' + municipio[0] + '"'
        cursor.execute(query3)
        resultsPreparatoria = cursor.fetchall()
        municipio[3]=resultsPreparatoria[0][0]
    return render_template("mapa.html",municipios=matrizMunic)

@app.route('/primarias')
def verPri():
    munic = ["Zapopan","SAN PEDRO TLAQUEPAQUE","Tonalá","Tlajomulco de Zúñiga","El Salto","Ixtlahuacán de los Membrillos","Juanacatlán"]
    prima = []
    cursor = mysql.connection.cursor()
    for municipio in munic:
        query = 'SELECT * FROM `primaria` WHERE `municipio` = "' + municipio + '"'
        cursor.execute(query)
        results = cursor.fetchall()
        for element in results:
            prima.append(element)
    return render_template("pri.html",primar=prima)

@app.route('/secundarias')
def verSec():
    munic = ["Zapopan","SAN PEDRO TLAQUEPAQUE","Tonalá","Tlajomulco de Zúñiga","El Salto","Ixtlahuacán de los Membrillos","Juanacatlán"]
    secu = []
    cursor = mysql.connection.cursor()
    for municipio in munic:
        query = 'SELECT * FROM `secundaria` WHERE `municipio` = "' + municipio + '"'
        cursor.execute(query)
        results = cursor.fetchall()
        for element in results:
            secu.append(element)
    return render_template("sec.html",secund=secu)

@app.route('/preparatorias')
def verPre():
    munic = ["Zapopan","SAN PEDRO TLAQUEPAQUE","Tonalá","Tlajomulco de Zúñiga","El Salto","Ixtlahuacán de los Membrillos","Juanacatlán"]
    prepa = []
    cursor = mysql.connection.cursor()
    for municipio in munic:
        query = 'SELECT * FROM `preparatoria` WHERE `municipio` = "' + municipio + '"'
        cursor.execute(query)
        results = cursor.fetchall()
        for element in results:
            prepa.append(element)
    return render_template("pre.html",prepara=prepa)

if __name__ == "__main__":
    app.run()
