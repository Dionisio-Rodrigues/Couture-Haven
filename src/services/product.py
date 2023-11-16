from src.app import db
from src.models.product import Product


def get_all():
    return Product.query.all()


def get_by_id(id):
    return Product.query.filter_by(id=id).first()


def get_by_name(name, exception_id=None):
    if exception_id:
        return Product.query.filter(Product.id != exception_id).filter_by(name=name).first()

    return Product.query.filter_by(name=name).first()


def get_by_category(category_id, exception_id=None):
    if exception_id:
        return Product.query.filter(Product.id != exception_id).filter_by(category_id=category_id).first()

    return Product.query.filter_by(category_id=category_id).first()


def save(product):

    if get_by_name(name=product.name, exception_id=product.id):
        raise Exception('It was not possible to save because the name already existed.')

    db.session.add(product)
    db.session.commit()

    return product


def delete(product):
    db.session.delete(product)
    db.session.commit()
