from app import yelp
import app.testdb
import app.business

if __name__ == '__main__':
    #db.create_all()
    yelp.run(debug=True)