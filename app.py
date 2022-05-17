from flask import Flask, redirect, render_template, request, json, url_for
import requests
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from models import db, ItemModel
from dotenv import load_dotenv
import os

load_dotenv()

#configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#create db table
@app.before_first_request
def create_table():
    db.create_all()

#variables for weather api
api_key = os.getenv('APIkey')
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#function to get the store locations
def get_temp_from_location(location):
    api_url = base_url + '&q=' + location +'&units=metric' + '&appid=' + api_key.format(location, api_key)
    response = requests.get(api_url)
    weather_information = response.json()
    temperature = str(weather_information['main']['temp']) + 'K' 
    return temperature

#POST request to add item to inventory
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
 
    if request.method == 'POST':
        name = request.form['name']
        tag = request.form['tag']
        location = request.form['location']

        #display weather at shop location
        temperature = get_temp_from_location(location)

        item = ItemModel( name=name, tag=tag, location = location) 
        db.session.add(item)
        db.session.commit()
        return redirect('/data',temperature=temperature)
 

#view list of available items 
@app.route('/data', methods=['GET'])
def RetrieveList():
    items = ItemModel.query.all()
    items = [{
                **item.__dict__,
                'temperature': get_temp_from_location(item.location)
                } for item in items
            ]
    
    
    return render_template('datalist.html',items = items)
 
 #search for an item  by name
@app.route('/data/<string:name>')
def Retrieveitem(name):
    item = ItemModel.query.filter_by(name=name).first()
    if item:
        return render_template('data.html', item = item, temperature=get_temp_from_location(item.location))
    return f"item with name ={name} Does not exist"

#search for an item by tag
@app.route('/data/tag/<string:tag>')
def Retrieveitemtag(tag):
    item = ItemModel.query.filter_by(tag=tag).first()
    if item:
        return render_template('tag.html', item = item, temperature=get_temp_from_location(item.location))
    return f"item with tag ={tag} Does not exist" 
 
 #delete an existing item 
@app.route('/data/<string:name>/delete', methods=['GET','POST'])
def delete(name):
    item = ItemModel.query.filter_by(name=name).first()
    if request.method == 'POST':
        if item:
            db.session.delete(item)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')
 

if __name__ == '__main__':
    app.run(debug=True)
