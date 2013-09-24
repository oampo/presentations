from jinja2.ext import Extension
from strip_index import strip_index

filters = {"strip_index" : strip_index}

class FilterLoader(Extension):
    def __init__(self, environment):
        super(FilterLoader, self).__init__(environment)
        environment.filters.update(filters)

