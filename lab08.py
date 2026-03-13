from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["bookmarkDB"]
collection = db["bookmarks"]

# Home route
@app.route("/")
def home():
    return "Bookmark Manager API Running"

# Add a new bookmark
@app.route("/add_bookmark", methods=["POST"])
def add_bookmark():
    data = request.json
    
    bookmark = {
        "title": data.get("title"),
        "url": data.get("url"),
        "tags": data.get("tags")
    }
    
    collection.insert_one(bookmark)
    
    return jsonify({"message": "Bookmark added successfully"}), 201


# Get bookmarks by tag
@app.route("/bookmarks/<tag>", methods=["GET"])
def get_bookmarks_by_tag(tag):
    
    bookmarks = list(collection.find({"tags": tag}, {"_id": 0}))
    
    return jsonify(bookmarks)


# Get all bookmarks
@app.route("/bookmarks", methods=["GET"])
def get_all_bookmarks():
    
    bookmarks = list(collection.find({}, {"_id": 0}))
    
    return jsonify(bookmarks)


if __name__ == "__main__":
    app.run(debug=True)
