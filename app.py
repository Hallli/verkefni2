from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/a-hluti')
def ahluti():
    return render_template('kennitala.html')

@app.route('/ktsida/<kt>')
def ktsum(kt):
    summa = 0
    for item in kt:
        summa = summa + int(item)
    return render_template('ktsum.html', kt=kt, summa=summa)

# Bhluti

# listi (dictionary)

frettir =  [
     # ID #Title #Innihald #Höfundur
    ["0", "Frétt 1", "1", "Höfundur 1"],
    ["1", "Frétt 2", "2", "Höfundur 2"],
    ["2", "Frétt 3", "3", "Höfundur 3"],
    ["3", "Frétt 4", "4", "Höfundur 4"],
    ["4", "Frétt 5", "5", "Höfundur 5"]
]

@app.route('/b-hluti')
def bhluti():                              #Inni haldið úr Dict
    return render_template('frettir.html', frettir = frettir)

@app.route('/frett/<int:id>')
def news(id):
    return render_template('frett.html', news = frettir[id], nr = id)

# Stöðul villuskilabop

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("pagenotfound.html"), 404

@app.errorhandler(500)
def servererror(error):
    return render_template("servererror.html"), 500

if __name__ == '__main__':
    #app.run()
    app.run(debug=True, use_reloader=True)