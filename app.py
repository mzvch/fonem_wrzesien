from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET KEY'] = "fonem"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/opis')
def opis():
    return render_template('opis.html')


@app.route('/dodaj')
def dodaj():
    return render_template('dodaj.html')


"""if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5019, debug=True)

if __name__ == '__main__':
    app.run()"""


if __name__ == '__main__':
    app.run()
