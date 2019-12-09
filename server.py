from flask import Flask, render_template
from flask_mysqldb import MySQL
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'WCqgiEsLy3'
app.config['MYSQL_PASSWORD'] = 'I9yyxDyDIJ'
app.config['MYSQL_DB'] = 'WCqgiEsLy3'
app.config['MYSQL_HOST'] = 'remotemysql.com'

mysql = MySQL(app)

matrizMunic = [["Guadalajara",0,0,0,20.6720375,-103.3383962,0],
        ["Zapopan",0,0,0,20.7032055,-103.4261243,0],
        ["San Pedro Tlaquepaque",0,0,0,20.5925775,-103.3388803,0],
        ["Tonalá",0,0,0,20.6185208,-103.2227359,0],
        ["Tlajomulco de Zúñiga",0,0,0,20.4737273,-103.4469713,0],
        ["El Salto",0,0,0,20.5391001,-103.2403775,0],
        ["Ixtlahuacán de los Membrillos",0,0,0,20.348165,-103.195463,0],
        ["Juanacatlán",0,0,0,20.507090,-103.170622,0]]

@app.route('/')
def verMapa():
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

        municipio[6]=municipio[1]+municipio[2]+municipio[3]
    return render_template("mapa.html",municipios=matrizMunic)

@app.route('/primarias')
def verPri():
    munic = ["Guadalajara","Zapopan","San Pedro Tlaquepaque","Tonalá","Tlajomulco de Zúñiga","El Salto","Ixtlahuacán de los Membrillos","Juanacatlán"]
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
    munic = ["Guadalajara","Zapopan","San Pedro Tlaquepaque","Tonalá","Tlajomulco de Zúñiga","El Salto","Ixtlahuacán de los Membrillos","Juanacatlán"]
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
    munic = ["Guadalajara","Zapopan","San Pedro Tlaquepaque","Tonalá","Tlajomulco de Zúñiga","El Salto","Ixtlahuacán de los Membrillos","Juanacatlán"]
    prepa = []
    cursor = mysql.connection.cursor()
    for municipio in munic:
        query = 'SELECT * FROM `preparatoria` WHERE `municipio` = "' + municipio + '"'
        cursor.execute(query)
        results = cursor.fetchall()
        for element in results:
            prepa.append(element)
    return render_template("pre.html",prepara=prepa)

@app.route('/pie')
def pie():
    #Pastel
    #datos
    labels = 'Guadalajara', 'Zapopan', 'San Pedro Tlaquepaque', 'Tonalá', 'Tlajomulco de Zúñiga', 'El Salto', 'Ixtlahuacán', 'Juanacatlán'
    colors = ['red','orange','gold','green','blue','purple','lightcoral','aqua']
    sizes = [matrizMunic[0][6],matrizMunic[1][6],matrizMunic[2][6],matrizMunic[3][6],matrizMunic[4][6],matrizMunic[5][6],matrizMunic[6][6],matrizMunic[7][6]]
    patches, texts = plt.pie(sizes, colors=colors)
    #funciones
    plt.legend(patches, labels, loc="best")
    plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()

@app.route('/histograma')
def histograma():
    #Histograma
    label = ['Primaria', 'Secundaria', 'Preparatoria']
    guad = []
    zap = []
    tlaq = []
    ton = []
    tlaj = []
    salt = []
    ixtl = []
    juan = []
    i = 1
    while i < 4:
        guad.append(matrizMunic[0][i])
        zap.append(matrizMunic[1][i])
        tlaq.append(matrizMunic[2][i])
        ton.append(matrizMunic[3][i])
        tlaj.append(matrizMunic[4][i])
        salt.append(matrizMunic[5][i])
        ixtl.append(matrizMunic[6][i])
        juan.append(matrizMunic[7][i])
        i+=1
    xpos = xpos = np.arange(len(label))
    plt.bar(xpos-0.5,guad, label="Guadalajara", width = 0.25)
    plt.bar(xpos-0.4,zap, label="Zapopan", width = 0.25)
    plt.bar(xpos-0.3,tlaq, label="San Pedro Tlaquepaque", width = 0.25)
    plt.bar(xpos-0.2,ton, label="Tonalá", width = 0.25)
    plt.bar(xpos-0.1,tlaj, label="Tlajomulco de Zuñigá", width = 0.25)
    plt.bar(xpos,salt, label="El Salto", width = 0.25)
    plt.bar(xpos+0.1,ixtl, label="Ixtlahuacán de los Membrillos", width = 0.25)
    plt.bar(xpos+0.2,juan, label="Juanacatlán", width = 0.25)
    plt.xticks(xpos,label)
    plt.ylabel("Número escuelas ")
    plt.title('Histograma Escuelas')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    app.run()
