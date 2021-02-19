import json


class Hierarchy(object):
    def __init__(self, app_id=None, name=None, description=None, app_filter=None, children=None, image_uri=None):
        self.id = app_id
        self.name = name
        self.description = description
        self.filter = app_filter
        self.children = children
        self.imageUri = image_uri

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=False, indent=4,
        )
