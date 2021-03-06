"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, jsonify, make_response
from bs4 import BeautifulSoup
import requests
import urlparse
from image_getter import imgGet

#url = "https://www.walmart.com/ip/54649026"
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    
@app.route('/api/thumbnails', methods=["GET"])
def thumbnails():
    #site_url = "https://www.walmart.com/ip/54649026"
    
    #error= None
    #message="Success"
    #thumbnail=[]
    urls= { "error":"null", "message":"success", "thumbnails":imgGet()}
    #return jsonify(urls)
    url_response = make_response(jsonify(urls))  
    return url_response

    
@app.route('/thumbnails/view')
def t_view():
    """Render thumbnail view."""
    return render_template('thumbnail.html')

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
    and also to tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
