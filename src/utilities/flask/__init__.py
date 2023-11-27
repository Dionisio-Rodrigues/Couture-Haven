from flask import Blueprint

create_blueprint = lambda name: Blueprint(name=name, import_name=__name__)
maybe_bind_id = lambda id, function: None if id is None else function(id)
