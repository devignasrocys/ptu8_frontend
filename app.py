from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/destytojas/')
def destytojas():
    return render_template("destytojas.html")

@app.route('/gridukas/')
def gridukas():
    return render_template("gridukas.html")

@app.route('/daiva/')
def daiva():
    return render_template('daiva.html')

@app.route('/dovydas/')
def dovydas():
    return render_template("dovydas.html")

@app.route('/monika/')
def monika():
    return render_template("monika.html")

@app.route('/studentas/')
def studentas():
    return render_template("studentas.html")

@app.route('/airida/')
def airida():
    return render_template("airida.html")

@app.route('/gisora/')
def gisora():
    return render_template('gisora.html')

@app.route('/edvard_p/')
def edvard_p():
    return render_template("edvard_p.html")
    
@app.route('/egle/')
def egle():
    return render_template("egle.html")

    


if __name__ == "__main__":
    app.run(debug=True)
