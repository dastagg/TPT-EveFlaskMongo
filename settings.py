X_DOMAINS = "*"

# mongo connection string
MONGO_URI = "mongodb://localhost:27017/eve-course"

RESOURCE_METHODS = ["GET", "POST", "DELETE"]
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]

# DATE_FORMAT = "%d %b %Y" NOTE: this will change how the dates are stored.
# QUERY_WHERE = "find"
# QUERY_SORT = "orderby"
# ALLOWED_FILTERS = []  # -- This would disallow all filters
# ALLOWED_FILTERS = ['lastname'] -- This would only allow filters on lastname
# SORTING = True
# MONGO_QUERY_BLACKLIST = ['$where']  -- would allow $regex to work
# PAGINGATION = False


# domain definition
people_schema = {
    "firstname": {"type": "string", "minlength": 1, "maxlength": 30,},
    "lastname": {"type": "string", "maxlength": 50, "required": True, "unique": True,},
    "middle_name": {"dependencies": ["firstname", "lastname"]},
    "born": {"type": "datetime"},
    "age": {
        "type": "integer",
        "isodd": True,
        # "coerce": int
    },
    "role": {
        "type": "list",
        "allowed": ["author", "contributor", "copy"],
        "default": ["author"],
    },
    "location": {
        "type": "dict",
        "schema": {
            "address": {"type": "string"},
            "city": {"type": "string", "required": True},
        },
    },
    "email": {"type": "email"},
    "prop1": {
        "anyof_type": ["integer", "float"],
        "anyof": [{"min": 0, "max": 10}, {"min": 100, "max": 110}],
    },
}

DOMAIN = {
    "people": {"schema": people_schema},
    "works": {"resource_methods": ["GET"], "item_methods": ["GET"]},
}
