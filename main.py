from flask import Flask
from database.db_config import init_db
from routes.book_routes import book_routes

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/"
init_db(app)
app.register_blueprint(book_routes)
app.register_blueprint(book_routes)

if __name__ == "__main__":
    app.run(debug=True)
    