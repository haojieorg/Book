from run import db

class Category(db.Model):
    __table__ = 'category'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,unique=True)
    sort = db.Column(db.Integer)

class Book(db.Model):
    __table__ = 'book'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    subject = db.Column(db.String)
    author = db.Column(db.String)
    publish = db.Column(db.String)
    ISBN = db.Column(db.String)
    Images = db.Column(db.String)
    preface = db.Column(db.String)
    salas = db.Column(db.Boolean)
    selected = db.Column(db.Boolean)
    publish_date = db.Column(db.Date)
    create_date = db.Column(db.Date)


    categoryid = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('category',lazy='dynamic'))

class User(db.Model):
    __table__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    mail = db.Column(db.String)
    password = db.Column(db.String)

