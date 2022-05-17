from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    #price = db.Column(db.Float(precision=2))
    location = db.Column(db.String(120))
    tag = db.Column(db.String(120))
    #weather = db.Column(db.String(160))
   


    def __init__(self, name, location, tag): 
        self.name = name
        self.location = location
        self.tag = tag
       
    
    def __repr__(self):
        return f"Name: {self.name} \n Available in {self.location} \n Tag:{self.tag} \n Item ID:{self.id}"

    