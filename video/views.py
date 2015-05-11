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
    tickets = db.session.query(SupportTicket).all()
    return render_template('tickets.html', tickets=tickets)


@app.route('/tickets/<int:id>')
def ticket():
    pass


