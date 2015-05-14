import requests
from flask import render_template, request

from . import app, db
from .models import SupportTicket

# List endpoint for the starwars ship API
SWAPI = 'http://swapi.co/api/starships'


@app.route('/landing')
def landing():
    return render_template('landing.html')


@app.route('/')
def index():
    resp = requests.get(SWAPI)
    if resp.status_code is not 200:
        return render_template('500.html')
    products = resp.json()
    return render_template('index.html', products=products['results'])


@app.route('/products')
def products():
    swapi_ship_url = request.args.get('url', '')
    results = requests.get(swapi_ship_url)
    return render_template('product.html', product=results.json())


@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    if request.method == 'GET':
        tickets = db.session.query(SupportTicket).all()
        return render_template('tickets.html', tickets=tickets)
    elif request.method == 'POST':
        endpoint = request.form.get('endpoint', None)
        product_url = request.form.get('productUrl', None)
        if endpoint is not None and product_url is not None:
            support_ticket = SupportTicket()


@app.route('/tickets/<int:id>')
def ticket():
    pass


