from django.contrib import admin
from .models import *

# Registering all models from models.py.
admin.site.register(Article)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Upvote)

