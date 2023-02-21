from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projet.db'
db.init_app(app)

class Tableau(db.Model):
    idT = db.Column(db.Integer,primary_key=True)
    imageT = db.Column(db.String(30))
    nomT = db.Column(db.String(50))
    descT = db.Column(db.String(200))
    dateT = db.Column(db.String(10))

    def __repr__(t):
        return 'Tableau %r'% t.idT

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add(Tableau(idT=1,imageT="static/tableaux/Australia.jpg",nomT="Australia",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=2,imageT="static/tableaux/Bohemienne.jpg",nomT="Bohemienne",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=3,imageT="static/tableaux/Cabaret.jpg",nomT="Cabaret",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=4,imageT="static/tableaux/Colorado.jpg",nomT="Colorado",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=5,imageT="static/tableaux/DroleDeZebre.jpg",nomT="Drôle de Zebres",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=6,imageT="static/tableaux/EnvoléeChampetre.jpg",nomT="Envolée Champetre",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=7,imageT="static/tableaux/FlamincoParty.jpg",nomT="Flaminco Party",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=8,imageT="static/tableaux/Manga.jpg",nomT="Manga",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=9,imageT="static/tableaux/Martin-Pecheur.jpg",nomT="Martin-Pecheur",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=10,imageT="static/tableaux/RockNRoll.jpg",nomT="Rock'n Roll",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=11,imageT="static/tableaux/RoséeFlorale.jpg",nomT="Rosée Florale",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=12,imageT="static/tableaux/Salagou.jpg",nomT="Salagou",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=13,imageT="static/tableaux/Symbiose.jpg",nomT="Symbiose",descT="Description du tableau",dateT="01/01/2020"))
    db.session.add(Tableau(idT=14,imageT="static/tableaux/Vinyl.jpg",nomT="Vinyl",descT="Description du tableau",dateT="01/01/2020"))
    db.session.commit()

@app.route("/")
def index():
    title='Accueil'
    return render_template("index.html",title=title,page=title)

@app.route("/listeTableaux")
def listeTableaux():
    title='Gallerie'
    tableaux=db.session.query(Tableau).all()
    print(tableaux)
    return render_template("lTab.html",title=title,page=title,tab=tableaux)

@app.route("/tableau/<int:id>")
def tableau(id):
    title='Gallerie'
    tabSelect=db.session.query(Tableau).filter(Tableau.idT==id).first()
    return render_template("tableau.html",title=title,page=title,tabS=tabSelect)

@app.route("/contact")
def contact():
    title='Contact'
    return render_template("contact.html",title=title,page=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)