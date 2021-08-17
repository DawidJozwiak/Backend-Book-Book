from django.contrib import admin

from .models import Publication
from .models import Shelves
from .models import Users
# Register your models here.


admin.site.register(Publication)
admin.site.register(Users)
admin.site.register(Shelves)