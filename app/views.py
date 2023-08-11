from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime

# Dictionary to store image information
uploaded_images = {
    1: {
        'filename': '/static/pics/Balloon.jpg',
        'title': 'Hot Air Balloon',
        'price': 19999.99,
        'description': 'Ever wondered what its like to touch the clouds? Well we have the answer. Our air balloon. is a luxurious sight-seeing vehicle. Ensure you do not use it on extremely windy or rainy days'
    },
    2: {
        'filename': '/static/pics/Mist.jpg',
        'title': 'Misty Forest',
        'price': 75.00,
        'description': 'This is quite the conversation starter. We guarantee that your guests will be intrigued by this fascinating image. '
    },
    3: {
        'filename': '/static/pics/Beachball.jpg',
        'title': 'Beachball',
        'price': 29.99,
        'description': 'Need to liven up your next beach or pool trip? Well, take one of our new and improved beachballs with you. Its fun for everyone.'
    },
    4: {
        'filename': '/static/pics/Flowers.jpg',
        'title': 'Flowers',
        'price': 14.99,
        'description': 'Have an important celebration coming up? Want to be extra romantic tonight? Or you just wanna get out of the doghouse? Try using one of our handpicked bouquet of flowers. They should help ;)'
    }
   
}

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about')
def about():
    """Render the website's about page"""
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html', uploaded_images=uploaded_images)

@app.route('/products/<int:product_id>')
def view_image(product_id):
    if product_id in uploaded_images:
        image_info = uploaded_images[product_id]
        return render_template('product_view.html', image_info=image_info,  uploaded_images=uploaded_images)
    else:
        return "Image not found." 

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

