from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String(120))
    #price = db.Column(db.Float(precision=2))
    location = db.Column(db.String(120))
    tag = db.Column(db.String(120))
    #weather = db.Column(db.String(160))
   


    def __init__(self, name, location, tag, item_id): #, weather):
        self.name = name
       # self.price = price
        self.location = location
        self.tag = tag
        #self.weather = weather
        self.item_id = item_id
    
    def __repr__(self):
        return f"Name: {self.name} \n Available in {self.location} \n Tag:{self.tag} \n Item ID:{self.item_id}"

    # def json(self):
    #     return {
    #         'Name': self.name,
    #         'Available in': self.location,
    #         'Tag' : self.tag,
    #     }