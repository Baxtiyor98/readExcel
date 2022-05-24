from import_export import resources
from .models import Person
class PersonReource(resources.ModelResource):
    class meta:
        model = Person