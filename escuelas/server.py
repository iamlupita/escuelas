from flask import Flask, render_template
from flask_mysqldb import MySQL
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'WCqgiEsLy3'
app.config['MYSQL_PASSWORD'] = 'I9yyxDyDIJ'
app.config['MYSQL_DB'] = 'WCqgiEsLy3'
app.config['MYSQL_HOST'] = 'remotemysql.com'

mysql = MySQL(app)

nom=Nominatim()

def do_geocode(address):
    try:
        return nom.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)

@app.route('/')
def verMapa():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT `nom_escuela`,`domicilio`, `municipio` FROM `primaria`")
    resultsPrimaria = cursor.fetchall()
    for primaria in resultsPrimaria:
        address=primaria[1]+" "+primaria[2]
        """coordPrim=do_geocode(address)
        if(coordPrim):
            print(coordPrim.latitude,coordPrim.longitude)"""
    cursor.execute("SELECT `nombre`,`domicilio`, `municipio` FROM `secundaria`")
    resultsSecundaria = cursor.fetchall()
    for secundaria in resultsSecundaria:
        address=secundaria[1]+" "+secundaria[2]
        """coordSec=do_geocode(address)
        if(coordSec):
            print(coordSec.latitude,coordSec.longitude)"""
    cursor.execute("SELECT `nombre_escuela`,`domicilio`, `municipio` FROM `preparatoria`")
    resultsPreparatoria = cursor.fetchall()
    for preparatoria in resultsPreparatoria:
        address=preparatoria[1]+" "+preparatoria[2]
        """coordPrep=do_geocode(address)
        if(coordSec):
            print(coordPrep.latitude,coordPrep.longitude)"""
    return render_template("mapa.html",primarias=resultsPrimaria, secundarias=resultsSecundaria, preparatorias=resultsPreparatoria)

if __name__ == "__main__":
    app.run()
    
