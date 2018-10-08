from flask import render_template, flash, redirect, url_for
from app import app
from app.models  import Snack
from app.forms import SnacksForm

chapati = Snack(name='chapati', kind = 'breack')
chips= Snack(name='zege', kind = 'chip yai')
andazi = Snack(name='andazi', kind = 'food')

snacks = [chapati, chips, andazi]


@app.route('/')
@app.route('/snacks')
def index():
    return render_template('index.html', title='Home', snacks=snacks)


@app.route('/snacks/new', methods=['GET', 'POST'])
def new():
    form = SnacksForm()
    if form.validate_on_submit():

        return redirect(url_for('index'))
    return render_template('new.html', title='Add or delete', form=form)
