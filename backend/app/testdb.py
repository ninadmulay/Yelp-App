from app import yelp, db
from sqlalchemy import text  # Import the text function
from flask import jsonify

@yelp.route('/testdb')
def test_database():
    try:
        db.session.execute(text('SELECT 1'))  # Wrap the query with text()
        data = {'message': 'Database connection successful from TestDB API call!'}
        return jsonify(data)
    
    except Exception as e:
        return f'Database connection failed: {str(e)}'
