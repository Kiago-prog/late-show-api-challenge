from . import db

class Guest(db.Model):
    __tablename__ = 'guests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    episode = db.relationship('Episode', back_populates='guests')
