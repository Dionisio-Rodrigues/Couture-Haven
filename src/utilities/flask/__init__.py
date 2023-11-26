from flask import Blueprint

create_blueprint = lambda name: Blueprint(name=name, import_name=__name__)
