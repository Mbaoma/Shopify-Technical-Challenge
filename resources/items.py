from flask import Flask, request
from flask_restful import Resource, reqparse
#from flask_jwt import jwt_required
import sqlite3
from models.item_model import ItemModel

class ItemsInShop(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
                            'price',
                            type=float,
                            required=True,
                            help='Must not be left blank'
        )
    parser.add_argument(
                            'store_id',
                            type=int,
                            required=True,
                            help='Every item needs a store id'
        )
    parser.add_argument(
                            'tag',
                            type=str,
                            required=True,
                            help='Every item needs a tag'
    )

    #@jwt_required()

    #GET request to find items by tag
    def get(self, tag):
        item = ItemModel.find_item_by_tag(tag)
        if item:
            return item.json()
        else:
            return {
                'message': "Item not found"
            }, 404

    #GET request to find items by name
    def get(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            return item.json()
        else:
            return {
                'message': "Item not found"
            }, 404
    
    #POST request to create an item using its name
    def post(self, name):
        if ItemModel.find_item_by_name(name):
            return {'message': "item '{}' already exists".format(name)}, 400

        data = ItemsInShop.parser.parse_args()
        item = ItemModel(name, data['price'], data['city'], data['tag'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {
                "message": "An error occured while inserting item"
            }, 500

        return item.json(), 201

     #DELETE request to delete an item by its name   
    def delete(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted!'}
    
    #PUT request to edit entries
    def put(self, name):
        data = ItemsInShop.parser.parse_args()

        item = ItemModel.find_item_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['city'], data['tag'], data['store_id'])
        else:
            item.price = data['price']
        
        item.save_to_db()
            
        return item.json(), 201
    
#GET request to list out all the items in the database
class ItemsList(Resource):
    def get(self):
        items = ItemModel.query.all()
        return {
            'Items': list(map(lambda x: x.json(), items)) #[item.json() for item in items]
        }, 200