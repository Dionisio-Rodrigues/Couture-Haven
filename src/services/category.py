from src.app import db
from src.models.category import Category


def get_all():
    return Category.query.all()


def get_by_id(id):
    return Category.query.filter_by(id=id).first()


def get_by_name(name, exception_id=None):
    if exception_id:
        return Category.query.filter(Category.id != exception_id).filter_by(name=name).first()

    return Category.query.filter_by(name=name).first()


def create(name):
    new_category = Category(name=name)

    db.session.add(new_category)
    db.session.commit()

    return new_category


def update(category, name):
    category.name = name

    db.session.add(category)
    db.session.commit()

    return category


def delete(category):
    db.session.delete(category)
    db.session.commit()
