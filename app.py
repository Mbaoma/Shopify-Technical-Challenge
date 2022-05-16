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
api_key = "071534067fb322029833e7bab196a9c5"
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
        #weather= request.form['weather']
        
        item = ItemModel(item_id=item_id, name=name, tag=tag, location = location) 
        db.session.add(item)
        db.session.commit()
        return redirect('/data')
 

#view list of available items 
@app.route('/data')
def RetrieveList():
    items = ItemModel.query.all()
    return render_template('datalist.html',items = items)
 
 
 #search for an item  by name
@app.route('/data/<string:name>')
def Retrieveitem(name):
    item = ItemModel.query.filter_by(name=name).first()
    if item:
        return render_template('data.html', item = item)
    return f"item with name ={name} Does not exist"

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
 
#app.run(host='127.0.0.1', port=5000)
if __name__ == '__main__':
    app.run(debug=True)