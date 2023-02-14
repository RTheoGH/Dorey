from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

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