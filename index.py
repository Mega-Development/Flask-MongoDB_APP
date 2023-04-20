# Creator: Adelso Guerra
from flask import Flask, render_template

app = Flask(__name__)

# Inicio
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/home')
def home2():
    return render_template("home.html")

# Acerca De
@app.route('/about')
def about():
    return render_template("about.html")

# Noticias
@app.route('/news')
def news():
    return render_template("news.html")

# Ventas
@app.route('/sales')
def sales():
    return render_template("sales.html")

# Entretenimiento
@app.route('/entertainment')
def entertainment():
    return render_template("entertainment.html")

# Control de Errores
# --404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# --500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
