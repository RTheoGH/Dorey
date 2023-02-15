from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projet.db'
db.init_app(app)

class Tableau(db.Model):
    idT = db.Column(db.Integer,primary_key=True)
    nomT = db.Column(db.String(50))

    def __repr__(t):
        return 'Tableau %r : %r'% t.idT,t.nomT

@app.route("/")
def index():
    title='Accueil'
    return render_template("index.html",title=title)

@app.route("/listeTableaux")
def listeTableaux():
    title='Gallerie'
    return render_template("lTab.html",title=title)

@app.route("/contact")
def contact():
    title='Contact'
    return render_template("contact.html",title=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)