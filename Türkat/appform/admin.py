from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Takip)
admin.site.register(Takipçi)