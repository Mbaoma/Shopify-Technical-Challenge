from crypt import methods
import os
from flask import Flask, redirect, render_template, request, json
import requests
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from models import db, ItemModel

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
api_key = "your-api-key"
url = "http://api.openweathermap.org/data/2.5/weather?"
#location = request.form['location']

#POST request to add item to inventory
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
 
    if request.method == 'POST':
        item_id = request.form['item_id']
        name = request.form['name']
        tag = request.form['tag']
        location = request.form['location']

        #display weather at shop location
        api_key = "your-api-key"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = url + "appid=" + api_key + "&q=" + location
        response = request.get(complete_url)
        weather_information = response.json()
        temperature = str(weather_information['main']['temp']) + 'k' 


        item = ItemModel(item_id=item_id, name=name, tag=tag, location = location) 
        db.session.add(item)
        db.session.commit()
        return redirect('/data', temperature=temperature)
 

#view list of available items 
@app.route('/data', methods=['GET'])
def RetrieveList():
    items = ItemModel.query.all()
    
    location = 'Lagos'
    api_key = "your-api-key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = url + "appid=" + api_key + "&q=" + location
    response = requests.get(complete_url)
    weather_information = response.json()
    temperature = str(weather_information['main']['temp']) + 'k' 


   
    return render_template('datalist.html',items = items, temperature=temperature)
 
 
 #search for an item  by name
@app.route('/data/<string:name>')
def Retrieveitem(name):
    item = ItemModel.query.filter_by(name=name).first()
    if item:
        return render_template('data.html', item = item)
    return f"item with name ={name} Does not exist"

#search for an item by tag
@app.route('/data/tag/<string:tag>')
def Retrieveitemtag(tag):
    item = ItemModel.query.filter_by(tag=tag).first()
    if item:
        return render_template('tag.html', item = item)
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
