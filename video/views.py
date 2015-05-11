from flask import render_template


from . import app


@app.route('/')
def demo():
    return render_template('demo.html')


@app.route('/landing')
def landing():
    return render_template('landing.html')
