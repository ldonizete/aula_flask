from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

def teste():
    return "<p>testando 1</p>"

def teste2():
    return "<p>testando 2</p>"

app.add_url_rule("/teste", "teste", teste);
app.add_url_rule("/teste-2", "teste2", teste2);

#Escape
@app.route("/user/<name>")
def user_name(name):
    return f"Olá, {escape(name)}!"

@app.route("/blog/<int:inteiro>")
def show_blog(inteiro):
    return f"O index do blog {inteiro}"

@app.route("/blog/<float:float>")
def show_float(float):
    return f"O numero quebrado é: {float}"

@app.route("/blog/<texto>")
def show_texto(texto):
    return f"O texto é: {texto}"

if __name__ == '__main__':
    app.run()