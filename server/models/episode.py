from . import db

class Episode(db.Model):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'), nullable=False)
    show = db.relationship('Show', back_populates='episodes')
    
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Episode {self.number} on {self.date}>"
