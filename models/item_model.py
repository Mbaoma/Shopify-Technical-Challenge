import sqlite3
from db  import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    price = db.Column(db.Float(precision=2))
    city = db.Column(db.String(120))
    tag = db.Column(db.String(120))

    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))

    def __init__(self, name, price, city, tag, item_id):
        self.name = name
        self.price = price
        self.city = city
        self.tag = tag
        self.item_id = item_id

    def json(self):
        return {
            'Name': self.name,
            'Price (N)': self.price,
            'Available in': self.city,
            'Tag' : self.tag
        }

    #class method to find items by tag
    @classmethod
     #class method to find items by name
    def find_item_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        
    def find_item_by_tag(cls, tag):
        return cls.query.filter_by(tag=tag)
    
   

    #function to save items to database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    #function to delete items from database (db)
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
