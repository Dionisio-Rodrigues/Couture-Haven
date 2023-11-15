from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"

db = SQLAlchemy(app)

from src.models import category


@app.route(rule="/category", methods=["GET"])
def index():
    found_categories = [result.to_dict() for result in category.Category.query.all()]

    return {"message": "Categories found successfully.", "categories": found_categories}, 200


@app.route(rule="/category/<id>", methods=["GET"])
def view(id):
    found_category = category.Category.query.filter_by(id=id).first()

    if not found_category:
        return {"message": f"Category with ID '{id}' not found."}, 404

    found_category = found_category.to_dict()

    return {"message": "Category found successfully.", "category": found_category}, 200


@app.route(rule="/category", methods=["POST"])
def create():
    body = request.get_json()

    if "name" not in body.keys():
        return {"error": "Invalid payload", "message": "Please provide the required category fields."}, 400

    name = body["name"]

    if category.Category.query.filter_by(name=name).first():
        return {"error": "Category already exists", "message": "A category with provided name already exists."}, 409

    new_category = category.Category(name=name)

    db.session.add(new_category)
    db.session.commit()

    new_category = new_category.to_dict()

    return {"message": "Category created successfully.", "category": new_category}, 201


@app.route(rule="/category/<id>", methods=["PUT", "PATCH"])
def update(id):
    body = request.get_json()

    if "name" not in body.keys():
        return {"error": "Invalid payload", "message": "Please provide the required category fields."}, 400

    found_category = category.Category.query.filter_by(id=id).first()

    if not found_category:
        return {"message": f"Category with ID '{id}' not found."}, 404

    name = body["name"]

    if category.Category.query.filter(category.Category.id != id).filter_by(name=name).first():
        return {"error": "Category already exists", "message": "A category with provided name already exists."}, 409

    found_category.name = name

    db.session.add(found_category)
    db.session.commit()

    found_category = found_category.to_dict()

    return {"message": "Category updated successfully.", "category": found_category}, 200


@app.route(rule="/category/<id>", methods=["DELETE"])
def destroy(id):
    found_category = category.Category.query.filter_by(id=id).first()

    if not found_category:
        return {"message": f"Category with ID '{id}' not found."}, 404

    db.session.delete(found_category)
    db.session.commit()

    return {}, 204
