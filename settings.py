X_DOMAINS = "*"

# mongo connection string
MONGO_URI = "mongodb://localhost:27017/eve-course"

RESOURCE_METHODS = ["GET", "POST", "DELETE"]
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]

# domain definition
people_schema = {"firstname": {"type": "string"}, "lastname": {"type": "string"}}

DOMAIN = {
    "people": {"schema": people_schema},
    "works": {"resource_methods": ["GET"], "item_methods": ["GET"]},
}
