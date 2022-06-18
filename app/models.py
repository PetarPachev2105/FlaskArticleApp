from app import db

 
class Article(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   post_uri = db.Column(db.String(50), unique=True)
   title = db.Column(db.String(255), nullable=False)
   body = db.Column(db.String)
 
   def __repr__(self):
       return 'Article %r' % self.id