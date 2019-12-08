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
    matrizPrim = [["Guadalajara",0,20.6720375,-823.3383962],
            ["Zapopan",0,20.7032055,-823.4261243],
            ["SAN PEDRO TLAQUEPAQUE",0,20.5925775,-823.3388803],
            ["Tonalá",0,20.6185208,-823.2227359],
            ["Tlajomulco de Zúñiga",0,20.4737273,-823.4469713],
            ["El Salto",0,20.5391001,-823.2403775],
            ["Ixtlahuacán de los Membrillos",0,20.4030274,-823.2050488],
            ["Juanacatlán",0,20.485749,-823.1507254]]
    matrizSec = [["Guadalajara",0,20.6720,-103.3383],
            ["Zapopan",0,20.7032,-103.4261],
            ["SAN PEDRO TLAQUEPAQUE",0,20.5925,-103.3388],
            ["Tonalá",0,20.6185,-103.2227],
            ["Tlajomulco de Zúñiga",0,20.4737,-103.4469],
            ["El Salto",0,20.5391,-103.2403],
            ["Ixtlahuacán de los Membrillos",0,20.4030,-103.2050],
            ["Juanacatlán",0,20.485,-103.1507]]
    matrizPrep = [["Guadalajara",0,20.672,-103.3383962],
            ["Zapopan",0,20.703,-103.4261243],
            ["SAN PEDRO TLAQUEPAQUE",0,20.592,-103.3388803],
            ["Tonalá",0,20.618,-103.2227359],
            ["Tlajomulco de Zúñiga",0,20.473,-103.4469713],
            ["El Salto",0,20.539,-103.2403775],
            ["Ixtlahuacán de los Membrillos",0,20.403,-103.2050488],
            ["Juanacatlán",0,20.48,-103.1507254]]
    cursor = mysql.connection.cursor()
    for municipio in matrizPrim:
        query = 'SELECT COUNT(*) FROM `primaria` WHERE `municipio` = "' + municipio[0] + '"'
        cursor.execute(query)
        resultsPrimaria = cursor.fetchall()
        municipio[1]=resultsPrimaria[0][0]
    for municipio in matrizSec:
        query = 'SELECT COUNT(*) FROM `secundaria` WHERE `municipio` = "' + municipio[0] + '"'
        cursor.execute(query)
        resultsSecundaria = cursor.fetchall()
        municipio[1]=resultsSecundaria[0][0]
    for municipio in matrizPrep:
        query = 'SELECT COUNT(*) FROM `preparatoria` WHERE `municipio` = "' + municipio[0] + '"'
        cursor.execute(query)
        resultsPreparatoria = cursor.fetchall()
        municipio[1]=resultsPreparatoria[0][0]
    return render_template("mapa.html",primarias=matrizPrim, secundarias=matrizSec, preparatorias=matrizPrep)

if __name__ == "__main__":
    app.run()
    
