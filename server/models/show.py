from server.app import db

class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    host = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    network = db.Column(db.String(100), nullable=True)

    # Relationship example if you have episodes (optional)
    episodes = db.relationship('Episode', backref='show', lazy=True)

    def __repr__(self):
        return f"<Show {self.title} hosted by {self.host}>"
