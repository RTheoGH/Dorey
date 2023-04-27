from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
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

class Utilisateur(db.Model):
    mail = db.Column(db.String(40),primary_key=True)
    nom = db.Column(db.String(30))
    prenom = db.Column(db.String(30))
    mdp = db.Column(db.String(30))
    pdp = db.Column(db.String(200))

    def __repr__(t):
        return 'Utilisateur %r'% t.idU

class Liste(db.Model):
    cleUtilisateur = db.Column(db.String(40),db.ForeignKey(Utilisateur.mail),primary_key=True)
    cleTableau = db.Column(db.Integer,db.ForeignKey(Tableau.idT),primary_key=True)

# with app.app_context():
#     db.drop_all()
#     db.create_all()
#     db.session.add(Tableau(idT=1,imageT="static/tableaux/Australia.jpg",nomT="Australia",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=2,imageT="static/tableaux/Bohemienne.jpg",nomT="Bohemienne",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=3,imageT="static/tableaux/Cabaret.jpg",nomT="Cabaret",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=4,imageT="static/tableaux/Colorado.jpg",nomT="Colorado",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=5,imageT="static/tableaux/DroleDeZebre.jpg",nomT="Drôle de Zebres",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=6,imageT="static/tableaux/EnvoléeChampetre.jpg",nomT="Envolée Champetre",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=7,imageT="static/tableaux/FlamincoParty.jpg",nomT="Flaminco Party",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=8,imageT="static/tableaux/Manga.jpg",nomT="Manga",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=9,imageT="static/tableaux/Martin-Pecheur.jpg",nomT="Martin-Pecheur",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=10,imageT="static/tableaux/RockNRoll.jpg",nomT="Rock'n Roll",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=11,imageT="static/tableaux/RoséeFlorale.jpg",nomT="Rosée Florale",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=12,imageT="static/tableaux/Salagou.jpg",nomT="Salagou",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=13,imageT="static/tableaux/Symbiose.jpg",nomT="Symbiose",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.add(Tableau(idT=14,imageT="static/tableaux/Vinyl.jpg",nomT="Vinyl",descT="Description du tableau",dateT="01/01/2020"))
#     db.session.commit()

@app.route("/")
def index():
    title='Accueil'
    return render_template("index.html",title=title,page=title)

@app.route("/connexion", methods=['GET','POST'])
def connexion():
    title='Connexion'

    if request.method == 'POST':
        connexion_utilisateur = db.session.query(Utilisateur).filter(Utilisateur.mail == request.form['mail']).first()
        if connexion_utilisateur is None:
            flash('Adresse mail invalide')
            return redirect("/connexion")
            check_password_hash(connexion_utilisateur.mdp,request.form['mdp'])
        if check_password_hash(connexion_utilisateur.mdp,request.form['mdp']):
            session['mail'] = request.form['mail']
            session['nom'] = connexion_utilisateur.nom
            session['prenom'] = connexion_utilisateur.prenom
            session['image'] = connexion_utilisateur.pdp
            print("hein")
        else:
            flash('Mot de passe incorrect')          
            return redirect('/connexion') 
        print("uwu ?")
        return redirect('/')              
    else:
        return render_template("connexion.html",title=title,page=title)

@app.route("/deconnexion")
def deconnexion():
    if 'mail' not in session :
        flash("Connectez vous pour accéder à cette page")
        return redirect("/connexion")
    session.pop('mail',None)
    return redirect('/')

@app.route("/inscription", methods=['GET','POST'])
def inscription():
    title="Inscription"

    if request.method == 'POST':
        mail = request.form['mail']
        nom = request.form['nom']
        prenom = request.form['prenom']
        mdp = request.form['mdp']
        pdp = request.form['pp']
        print(pdp)
        # print(mail,nom,prenom,mdp)
        nouveau_utilisateur = Utilisateur(mail=mail,\
            nom=nom,\
            prenom=prenom,\
            mdp=generate_password_hash(mdp, method='pbkdf2:sha256', salt_length=16),\
            pdp=pdp)

        try:
            db.session.add(nouveau_utilisateur)
            db.session.commit()
            print("L'utilisateur a été ajouté avec succès")
            return redirect("/")
        except:
            return 'Erreur lors de l\'ajout de l\'utilisateur'
    else:
        return render_template("inscription.html",title=title,page=title)

@app.route("/test")
def test():
    title='ADMIN'
    tous_les_utilisateurs = db.session.query(Utilisateur).all()
    return render_template("test.html",title=title,page=title,utilisateurs=tous_les_utilisateurs)

@app.route("/listeTableaux")
def listeTableaux():
    title='Gallerie'
    tableaux=db.session.query(Tableau).all()
    print(tableaux)
    return render_template("lTab.html",title=title,page=title,tab=tableaux)

@app.route("/tableau/<int:id>")
def tableau(id):
    title='Tableau'
    tabSelect=db.session.query(Tableau).filter(Tableau.idT==id).first()
    return render_template("tableau.html",title=title,page=title,tabS=tabSelect)

@app.route("/ajoutTableau/<int:id>")
def ajoutTab(id):
    if 'mail' not in session :
        flash("Connectez vous pour accéder à cette page")
        return redirect("/connexion")
    tableau_a_ajouter = db.session.query(Tableau).filter(Tableau.idT == id).first()
    print(tableau_a_ajouter.idT)

    try:
        db.session.add(Liste(cleUtilisateur=session['mail'],cleTableau=tableau_a_ajouter.idT))
        db.session.commit()
        print("wa")
        return redirect("/liste")
    except:
        flash("Tableau déjà dans votre liste")
        return redirect("/tableau/"+str(id))

@app.route("/liste")
def liste():
    if 'mail' not in session :
        flash("Connectez vous pour accéder à cette page")
        return redirect("/connexion")
    title="Ma liste"
    liste_de_utilisateur = db.session.query(Tableau).join(Liste).filter(Liste.cleTableau == Tableau.idT).filter(Liste.cleUtilisateur == session['mail']).all()
    return render_template("liste.html",title=title,page=title,tab=liste_de_utilisateur)

@app.route("/profil")
def profil():
    if 'mail' not in session :
        flash("Connectez vous pour accéder à cette page")
        return redirect("/connexion")
    title="Profil"
    profil = db.session.query(Utilisateur).filter(Utilisateur.mail == session['mail']).first()
    return render_template("profil.html",title=title,page=title,profil=profil)

@app.route("/modifier-profil/<string:id>", methods=['GET','POST'])
def modifierP(id):
    if 'mail' not in session :
        flash("Connectez vous pour accéder à cette page")
        return redirect("/connexion")
    title="ModificationP"

    if request.method == 'POST':
        nouveau_nom = request.form['nom']
        nouveau_prenom = request.form['prenom']
        nouvelle_pdp = request.form['pp']

        modification = Utilisateur.query.get_or_404(id)
        modification.nom = nouveau_nom
        session['nom'] = nouveau_nom
        modification.prenom = nouveau_prenom
        session['prenom'] = nouveau_prenom
        modification.pdp = nouvelle_pdp
        session['image'] = nouvelle_pdp
        db.session.commit()
        flash("Profil modifié")
        return redirect("/profil")
    else:
        utilisateur_a_modifier = db.session.query(Utilisateur).filter(Utilisateur.mail == id).first()
        return render_template("modifierP.html",title=title,page=title,profil=utilisateur_a_modifier)

@app.route("/modifier-mdp/<string:id>", methods=['GET','POST'])
def modifierMDP(id):
    if 'mail' not in session :
        flash("Connectez vous pour accéder à cette page")
        return redirect("/connexion")
    title="ModificationMDP"

    if request.method == 'POST':
        ancien_mdp = request.form['ancien_mdp']
        nouveau_mdp = request.form['nouveau_mdp']

        modification = Utilisateur.query.get_or_404(id)
        if check_password_hash(modification.mdp,ancien_mdp):
            modification.mdp = generate_password_hash(nouveau_mdp, method='pbkdf2:sha256', salt_length=16)
            db.session.commit()
            flash("Mot de passe modifié")
            return redirect("/profil")
        else:
            flash("Mot de passe invalide")
            return redirect("/profil")
    else:
        utilisateur_a_modifier = db.session.query(Utilisateur).filter(Utilisateur.mail == id).first()
        return render_template("modifierMDP.html",title=title,page=title,profil=utilisateur_a_modifier)

@app.route("/contact")
def contact():
    title='Contact'
    return render_template("contact.html",title=title,page=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)