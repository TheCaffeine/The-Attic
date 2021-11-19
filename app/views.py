
from flask import Blueprint,render_template,flash,request,jsonify,redirect,url_for
from flask_login import login_required,current_user
from .models import User
from . import db


views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')

@login_required
def home():
    
    return render_template('base.html', user=current_user,)
    


@views.route('/artworks')
def artworks():
    
    return render_template('artworks.html')


@views.route('/gallery')
def gallery():
    
    return render_template('gallery.html')

@views.route('/museum')
def museum():
    
    return render_template('museum.html')


@views.route('/cart')
def cart():
    
    return render_template('cart.html')



@views.route('/checkout')
def checkout():
    
    return render_template('checkout.html')


@views.route('/confirm')
def confirm():
    
    return render_template('confirmation.html')


@views.route('/shopbar')
def shopbar():
    
    return render_template('shopbar.html')