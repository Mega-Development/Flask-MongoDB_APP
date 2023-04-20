# Creator: Mega Development
from flask import Flask, render_template, request, jsonify, redirect, url_for, Response
import database as dbase  
from product import Product

db = dbase.dbConnection()

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

# App
@app.route('/demo')
def demo():
    products = db['products']
    productsReceived = products.find()
    return render_template("demo.html", products = productsReceived)

#Method Post
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        product = Product(name, price, quantity)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name' : name,
            'price' : price,
            'quantity' : quantity
        })
        return redirect(url_for('demo'))
    else:
        return page_not_found()

#Method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('demo'))

#Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        products.update_one({'name' : product_name}, {'$set' : {'name' : name, 'price' : price, 'quantity' : quantity}})
        response = jsonify({'message' : 'Producto ' + product_name + ' actualizado correctamente'})
        return redirect(url_for('demo'))
    else:
        return page_not_found()

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
