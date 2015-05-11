from flask import render_template


from . import app, db
from .models import SupportTicket


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    pass


@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    tickets = db.session.query(SupportTicket).all()
    return render_template('tickets.html', tickets=tickets)


@app.route('/tickets/<int:id>')
def ticket():
    pass


@app.route('/landing')
def landing():
    return render_template('landing.html')

