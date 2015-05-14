import datetime
import requests
from flask import render_template, request, Response

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
        return render_template('tickets.html', tickets=tickets,
                               now=datetime.datetime.now())
    elif request.method == 'POST':
        endpoint = request.form.get('endpoint', None)
        product_url = request.form.get('productUrl', None)
        if endpoint is not None and product_url is not None:
            support_ticket = SupportTicket(endpoint, product_url)
            db.session.add(support_ticket)
            db.session.commit()
            return Response('Hang tight, an agent will '
                            'be with you shortly!', 200)

@app.route('/tickets/<int:ticket_id>')
def ticket(ticket_id):
    return "help customer page"


