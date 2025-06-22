from . import db

class Episode(db.Model):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    air_date = db.Column(db.Date)
    
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'), nullable=False)
    show = db.relationship('Show', back_populates='episodes')
    
    guests = db.relationship('Guest', back_populates='episode', cascade='all, delete-orphan')
