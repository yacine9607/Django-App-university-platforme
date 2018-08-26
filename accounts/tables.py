


import django_tables2 as tables
from .models import Enseignant








class PersonTable(tables.Table):
    class Meta:
        model = Enseignant
        template_name = 'django_tables2/bootstrap.html'