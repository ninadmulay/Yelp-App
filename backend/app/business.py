from app import yelp, db
from flask import jsonify

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255))
    address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    postal_code = db.Column(db.String(20))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    stars = db.Column(db.Float)
    review_count = db.Column(db.Integer)
    #image_url = db.Column(db.Text)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    user_id = db.Column(db.Integer)  # You'll likely have a User model later
    stars = db.Column(db.Integer)
    text = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

@yelp.route('/api/businesses')
def get_businesses():
    businesses = Business.query.all()
    return jsonify([b.to_dict() for b in businesses])

@yelp.route('/api/businesses/<int:id>')
def get_business(id):
    business = Business.query.get_or_404(id)
    return jsonify(business.to_dict())

# Example route for getting reviews for a business
@yelp.route('/api/businesses/<int:business_id>/reviews')
def get_reviews(business_id):
    try:
        reviews = Review.query.filter_by(business_id=business_id).all()
        return jsonify([r.to_dict() for r in reviews])
    except:
        return jsonify({'error':'Database call failed'})