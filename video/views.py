from flask import render_template


from . import app


@app.route('/')
def demo():
    return render_template('demo.html')


@app.route('/products')
def products():
    pass


@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    return render_template('tickets.html')


@app.route('/tickets/<int:id>')
def ticket():
    pass


@app.route('/landing')
def landing():
    return render_template('landing.html')

